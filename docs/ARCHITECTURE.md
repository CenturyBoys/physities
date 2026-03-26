# Physities Architecture

This document describes the architecture, design decisions, and implementation approaches used in physities.

## Overview

Physities is a hybrid Python/Rust library for working with physical quantities and units. It combines Python's expressiveness for the user-facing API with Rust's performance for core operations.

```mermaid
graph TB
    subgraph Python["Python API Layer"]
        Unit["Unit<br/>MetaUnit"]
        Scale["Scale<br/>(Kobject)"]
        Dimension["Dimension<br/>(frozen)"]
        BaseDimension["BaseDimension<br/>(IntEnum)"]

        Unit --> Scale
        Scale --> Dimension
        Dimension --> BaseDimension
    end

    subgraph Rust["Rust Core Layer"]
        PhysicalScale["PhysicalScale"]
        NDArray["ndarray Array1&lt;f64&gt;<br/>(15 elements)"]

        PhysicalScale --> NDArray
    end

    subgraph Dependencies["Rust Dependencies"]
        PyO3["PyO3<br/>Bindings"]
        ndarray["ndarray<br/>Linear Algebra"]
        serde["serde<br/>JSON"]
    end

    Python --> Rust
    Rust --> Dependencies

    style Python fill:#3572A5,color:#fff
    style Rust fill:#dea584,color:#000
    style Dependencies fill:#f0f0f0,color:#000
```

## Core Concepts

### Physical Dimensions

Physical quantities have dimensions composed of 7 SI base dimensions:

| Index | Dimension           | Symbol | Example          |
|-------|---------------------|--------|------------------|
| 0     | Length              | L      | meter            |
| 1     | Mass                | M      | kilogram         |
| 2     | Temperature         | Θ      | kelvin           |
| 3     | Time                | T      | second           |
| 4     | Amount of Substance | N      | mole             |
| 5     | Electric Current    | I      | ampere           |
| 6     | Luminous Intensity  | Iᵥ     | candela          |

A dimension is represented as a tuple of exponents. For example:
- Length: `(1, 0, 0, 0, 0, 0, 0)`
- Velocity (L/T): `(1, 0, 0, -1, 0, 0, 0)`
- Force (M·L/T²): `(1, 1, 0, -2, 0, 0, 0)`

### Scale and Conversion

A **Scale** combines:
1. **Dimension exponents** - What physical quantity it represents
2. **Conversion factors** - Per-dimension conversion to SI units
3. **Rescale value** - Additional scalar multiplier

For example, kilometers per hour:
- Dimension: `(1, 0, 0, -1, 0, 0, 0)` (velocity)
- Conversion: `(1000, 1, 1, 3600, 1, 1, 1)` (km→m, hour→seconds)
- Rescale: `1.0`

### Units

**Units** are Python classes with a `Scale` attached. The **MetaUnit** metaclass enables operator overloading at the class level, allowing syntax like:

```python
Velocity = Meter / Second  # Creates a new Unit class
```

## Design Decisions

### 1. Unified Data Structure (Rust)

**Decision**: Store all scale data in a single 15-element array.

```rust
pub struct PhysicalScale {
    data: Array1<f64>,  // 15 elements
    // [0..7]  = dimension exponents
    // [7..14] = conversion factors
    // [14]    = rescale value
}
```

**Rationale**:
- **Cache efficiency**: Contiguous memory access pattern
- **SIMD-friendly**: Enables vectorized operations
- **Single allocation**: Reduces memory fragmentation
- **NumPy compatibility**: Direct interop via ndarray

### 2. Operations as Linear Algebra

**Decision**: Implement physical operations as vector operations.

| Physical Operation | Implementation |
|-------------------|----------------|
| `A * B` (multiply) | `exponents_a + exponents_b` |
| `A / B` (divide) | `exponents_a - exponents_b` |
| `A ** n` (power) | `n * exponents` |
| Conversion factor | `product(conversions) * rescale` |
| Dimension equality | `exponents_a == exponents_b` |

**Rationale**:
- Leverages ndarray's optimized implementations
- Enables potential GPU acceleration
- Simplifies implementation and reasoning

### 3. Dimension Annulation Handling

**Decision**: When dimensions cancel out during operations, conversion factors are moved to rescale.

```python
# Example: m/s * s = m
velocity_scale = Scale(dim=(1,0,0,-1,...), conv=(1,1,1,1,...))
time_scale = Scale(dim=(0,0,0,1,...), conv=(1,1,1,1,...))
result = velocity_scale * time_scale
# Result: dim=(1,0,0,0,...), conv=(1,1,1,1,...), rescale=1
```

**Rationale**:
- Preserves conversion accuracy
- Ensures `(a * b).conversion_factor == a.conv * b.conv`
- Simplifies unit comparison

### 4. Metaclass Pattern for Units

**Decision**: Use Python metaclass (`MetaUnit`) for class-level operators.

```python
class MetaUnit(type):
    def __mul__(cls, other):
        # Allows: Meter * Second
        ...
    def __truediv__(cls, other):
        # Allows: Meter / Second
        ...
```

**Rationale**:
- Enables natural syntax: `Velocity = Meter / Second`
- Type-level operations (not instance-level)
- Dynamic unit creation without boilerplate

### 5. Hybrid Python/Rust Architecture

**Decision**: Keep Python API unchanged, add Rust for performance-critical paths.

**Rationale**:
- **Backwards compatibility**: Existing code continues to work
- **Gradual adoption**: Users can opt-in to Rust backend
- **Flexibility**: Complex logic in Python, hot paths in Rust
- **Testing**: All 47 existing tests pass unchanged

### 6. Int64 Dimension Encoding

**Decision**: Compact encoding of dimensions into 64-bit integer.

```
int64 (64 bits):
├── bits 0-3:   LENGTH exponent     (4 bits, range -8 to +7)
├── bits 4-7:   MASS exponent       (4 bits)
├── bits 8-11:  TEMPERATURE         (4 bits)
├── bits 12-15: TIME exponent       (4 bits)
├── bits 16-19: AMOUNT exponent     (4 bits)
├── bits 20-23: ELECTRIC_CURRENT    (4 bits)
├── bits 24-27: LUMINOUS_INTENSITY  (4 bits)
└── bits 28-63: reserved            (36 bits)
```

**Rationale**:
- Compact storage for databases
- Fast equality comparison (single integer compare)
- Suitable for hash keys
- Supports exponents -8 to +7 (covers most physical quantities)

## Module Structure

```mermaid
graph TD
    subgraph Root["physities/"]
        Cargo["Cargo.toml"]
        PyProject["pyproject.toml"]

        subgraph RustCore["physities_core/src/"]
            LibRS["lib.rs"]
            PhysicalScaleRS["physical_scale.rs"]
        end

        subgraph PythonPkg["physities/"]
            Init["__init__.py"]

            subgraph Src["src/"]
                subgraph DimMod["dimension/"]
                    BaseDim["base_dimensions.py"]
                    DimPy["dimension.py"]
                end

                subgraph ScaleMod["scale/"]
                    ScalePy["scale.py"]
                end

                subgraph UnitMod["unit/"]
                    UnitPy["unit.py"]
                    UnitInit["__init__.py"]
                end
            end
        end

        subgraph Tests["tests/"]
            UnitTests["unit/"]
        end
    end

    LibRS --> PhysicalScaleRS
    Init --> UnitMod
    UnitPy --> ScalePy
    ScalePy --> DimPy
    DimPy --> BaseDim

    style RustCore fill:#dea584
    style PythonPkg fill:#3572A5,color:#fff
```

## Class Diagram

```mermaid
classDiagram
    class BaseDimension {
        <<IntEnum>>
        LENGTH = 0
        MASS = 1
        TEMPERATURE = 2
        TIME = 3
        AMOUNT = 4
        ELECTRIC_CURRENT = 5
        LUMINOUS_INTENSITY = 6
    }

    class Dimension {
        <<frozen dataclass>>
        +tuple dimensions_tuple
        +length() float
        +mass() float
        +time() float
        +temperature() float
        +new_length() Dimension
        +new_mass() Dimension
        +new_time() Dimension
        +new_dimensionless() Dimension
        +show_dimension() str
    }

    class Scale {
        <<frozen dataclass>>
        +Dimension dimension
        +tuple from_base_scale_conversions
        +float rescale_value
        +conversion_factor() float
        +is_dimensionless() bool
        +new() Scale
    }

    class MetaUnit {
        <<metaclass>>
        +Scale scale
        +__mul__(other) MetaUnit
        +__truediv__(other) MetaUnit
        +__pow__(power) MetaUnit
    }

    class Unit {
        +Scale scale
        +float value
        +convert(target) Unit
        +to_si() Unit
        +__add__(other) Unit
        +__sub__(other) Unit
        +__mul__(other) Unit
        +__truediv__(other) Unit
    }

    class PhysicalScale {
        <<Rust/PyO3>>
        +Array~f64~ data
        +multiply(other) PhysicalScale
        +divide(other) PhysicalScale
        +power(exp) PhysicalScale
        +conversion_factor() float
        +to_json() str
        +to_dimension_int64() i64
    }

    Dimension --> BaseDimension : uses
    Scale --> Dimension : contains
    Unit --> Scale : has
    MetaUnit --> Scale : creates
    Unit ..|> MetaUnit : instance of

    PhysicalScale ..> Scale : optimizes
```

## Data Flow

### Unit Creation

```mermaid
sequenceDiagram
    participant User as User Code
    participant Meta as MetaUnit
    participant Scale as Scale
    participant Dim as Dimension

    User->>Meta: Meter / Second
    Meta->>Scale: Scale.__truediv__
    Scale->>Dim: Dimension.__sub__
    Dim-->>Scale: new Dimension (1,0,0,-1,...)
    Scale-->>Meta: new Scale object
    Meta-->>User: Velocity Unit class
```

### Value Conversion (with Rust)

```mermaid
sequenceDiagram
    participant User as User Code
    participant Unit as Unit.convert()
    participant Scale as Scale
    participant Rust as PhysicalScale (Rust)

    User->>Unit: km_h.convert(m_s)
    Unit->>Scale: scale.conversion_factor
    Scale->>Rust: PhysicalScale.conversion_factor()
    Rust-->>Scale: f64 value
    Scale-->>Unit: conversion ratio
    Unit-->>User: converted value
```

## Performance Characteristics

### Memory Layout

```mermaid
block-beta
    columns 1

    block:header:1
        A["PhysicalScale (120 bytes)"]
    end

    block:metadata:1
        B["Array1&lt;f64&gt; metadata (pointer, shape, strides) ~24B"]
    end

    block:dimensions:1
        C["Dimension Exponents (7 × 8 bytes = 56 bytes)<br/>[L] [M] [Θ] [T] [N] [I] [Iᵥ]"]
    end

    block:conversions:1
        D["Conversion Factors (7 × 8 bytes = 56 bytes)<br/>[cL] [cM] [cΘ] [cT] [cN] [cI] [cIᵥ]"]
    end

    block:rescale:1
        E["Rescale Value (8 bytes)"]
    end

    style header fill:#dea584
    style dimensions fill:#98D8C8
    style conversions fill:#F7DC6F
    style rescale fill:#BB8FCE
```

Alternative representation:

```mermaid
graph LR
    subgraph PhysicalScale["PhysicalScale Array (15 × f64)"]
        subgraph Dims["Indices 0-6: Dimensions"]
            D0["[0] L"]
            D1["[1] M"]
            D2["[2] Θ"]
            D3["[3] T"]
            D4["[4] N"]
            D5["[5] I"]
            D6["[6] Iᵥ"]
        end

        subgraph Convs["Indices 7-13: Conversions"]
            C0["[7] cL"]
            C1["[8] cM"]
            C2["[9] cΘ"]
            C3["[10] cT"]
            C4["[11] cN"]
            C5["[12] cI"]
            C6["[13] cIᵥ"]
        end

        subgraph Rescale["Index 14"]
            R["[14] rescale"]
        end
    end

    style Dims fill:#98D8C8
    style Convs fill:#F7DC6F
    style Rescale fill:#BB8FCE
```

### Complexity

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| multiply/divide | O(1) | O(1) - single alloc |
| power | O(1) | O(1) |
| conversion_factor | O(1) | O(1) |
| to_json | O(1) | O(n) - string |
| to_dimension_int64 | O(1) | O(1) |

## Extension Points

### Adding New Dimensions

The current 7-dimension model is based on SI. To add dimensions:

1. Update `BaseDimension` enum
2. Extend array size in Rust (15 → 17 for 8 dimensions)
3. Update serialization format

### Custom Serialization

The `PhysicalScale` provides multiple serialization options:

```python
# JSON (full fidelity)
scale.to_json()  # "[1.0,0.0,...,1000.0,...]"

# Int64 (dimensions only, compact)
scale.to_dimension_int64()  # 61441

# Dict (human readable)
scale.to_dict()  # {"dimensions": [...], "conversions": [...], "rescale": 1.0}
```

### NumPy Integration

```python
import numpy as np
from physities._physities_core import PhysicalScale

# Get raw array
arr = scale.as_numpy()  # numpy.ndarray shape (15,)

# Create from array
scale = PhysicalScale.from_numpy(arr)
```

## Testing Strategy

### Unit Tests (Python)

- Test all Python classes independently
- Verify operator behavior
- Check edge cases (zero, negative, fractional exponents)

### Integration Tests

- Test Python-Rust interop
- Verify serialization roundtrips
- Compare Python and Rust results

### Property Tests (recommended)

```python
from hypothesis import given, strategies as st

@given(st.floats(), st.floats())
def test_multiply_associative(a, b):
    # (scale_a * scale_b) * scale_c == scale_a * (scale_b * scale_c)
    ...
```

## Future Considerations

1. **GPU Acceleration**: ndarray supports GPU backends
2. **Uncertainty Propagation**: Add uncertainty tracking to values
3. **Unit Registry**: Global registry for custom units
4. **Caching**: Memoize common unit combinations
5. **Type Hints**: Full typing for IDE support
