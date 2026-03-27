# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Physities is a hybrid Python/Rust library for representing and working with physical quantities and units. It provides unit conversion, dimensional analysis, and mathematical operations on physical measurements, with a high-performance Rust core.

## Development Commands

```bash
# Install dependencies
pip install -e ".[dev]"

# Build Rust extension (required after Rust changes)
maturin develop

# Run all tests
pytest tests/ -v

# Run unit tests only
pytest tests/ -v -m unit

# Run a single test file
pytest tests/unit/unit/test_unit.py -v

# Run a specific test
pytest tests/unit/unit/test_unit.py::TestUnit::test_conversion -v

# Linting
ruff check .        # Python
cargo clippy        # Rust

# Check Rust compilation
cargo check
```

## Architecture

The library uses a hybrid Python/Rust architecture:

### Python Layer (API)

1. **BaseDimension** (`physities/src/dimension/base_dimensions.py`): IntEnum of 7 SI base dimensions (LENGTH, MASS, TEMPERATURE, TIME, AMOUNT, ELECTRIC_CURRENT, LUMINOUS_INTENSITY)

2. **Dimension** (`physities/src/dimension/dimension.py`): Frozen dataclass combining base dimensions into a tuple for composite physical dimensions

3. **Scale** (`physities/src/scale/scale.py`): Frozen dataclass with dimension + conversion factors, uses Kobject for attribute validation

4. **Unit + MetaUnit** (`physities/src/unit/unit.py`): MetaUnit metaclass enables operator overloading at the class level, allowing syntax like `Meter / Second` to create new unit types dynamically

### Rust Core (Performance)

5. **PhysicalScale** (`physities_core/src/physical_scale.rs`): High-performance scale operations using ndarray
   - 15-element array: 7 dimension exponents + 7 conversion factors + 1 rescale value
   - Linear algebra operations for physical math
   - Serialization (JSON, int64 encoding)
   - NumPy interop

### Key Patterns

- **Immutability**: All Python core classes use `@dataclass(frozen=True, slots=True)`
- **Metaclass operators**: `MetaUnit` overloads `__mul__`, `__truediv__`, `__pow__` at the class level
- **Factory methods**: `Dimension.new_length()`, `Scale.new()` etc.
- **Dimensional analysis**: Scale stores separate conversion factors per base dimension
- **Unified data structure**: Rust uses single array for cache-friendly operations

### File Structure

```
physities/
├── Cargo.toml                # Rust package config
├── pyproject.toml            # Python + maturin config
├── physities_core/src/       # Rust source
│   ├── lib.rs                # PyO3 exports
│   └── physical_scale.rs     # Core implementation
├── physities/src/            # Python source
│   ├── dimension/            # Dimension handling
│   ├── scale/                # Scale implementation
│   └── unit/                 # Unit classes
└── tests/                    # Test suite
```

### Usage Example

```python
from physities.src.unit import *

Ms = Meter / Second           # Create composite unit type
Kh = Kilometer / Hour
v1 = Ms(40)                   # 40 m/s
v2 = Kh(144)                  # 144 km/h
v3 = v2.convert(Ms)           # Convert between units

# Using Rust backend directly
from physities._physities_core import PhysicalScale
scale = PhysicalScale.from_components(
    (1.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0),  # velocity dimension
    (1000.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0),  # km conversion
    1.0
)
```

## Conventions

- Conventional Commits style: `feat:`, `chore:`, `fix:`
- Tests marked with `@pytest.mark.unit`
- Test fixtures in `tests/fixtures/fixtures.py` with predefined units and scales
- Python linting with ruff, Rust with clippy
- Version sync required between `pyproject.toml` and `Cargo.toml`

## Build System

- **maturin**: Builds Rust extension as Python wheel
- **PyO3**: Python bindings for Rust
- **ndarray**: Rust N-dimensional arrays (NumPy-like)

After modifying Rust code, always run:
```bash
maturin develop
```

## Documentation

- `docs/ARCHITECTURE.md` - Detailed architecture documentation
- `docs/CONFIGURATION.md` - Build and config file explanation
- `docs/DEVELOPMENT.md` - Development workflow guide
