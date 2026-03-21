# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Physities is a Python library for representing and working with physical quantities and units. It provides unit conversion, dimensional analysis, and mathematical operations on physical measurements.

## Development Commands

```bash
# Install dependencies
poetry install

# Run all tests
pytest

# Run unit tests only
pytest -m unit

# Run a single test file
pytest tests/unit/unit/test_unit.py

# Run a specific test
pytest tests/unit/unit/test_unit.py::TestUnitOperations::test_name -v
```

## Architecture

The library uses a three-layer architecture with a metaclass pattern:

1. **BaseDimension** (`physities/src/dimension/base_dimensions.py`): Enum of 7 SI base dimensions (LENGTH, MASS, TEMPERATURE, TIME, AMOUNT, ELECTRIC_CURRENT, LUMINOUS_INTENSITY)

2. **Dimension** (`physities/src/dimension/dimension.py`): Frozen dataclass combining base dimensions into a tuple for composite physical dimensions

3. **Scale** (`physities/src/scale/scale.py`): Frozen dataclass with dimension + conversion factors, uses Kobject for attribute validation

4. **Unit + MetaUnit** (`physities/src/unit/unit.py`): MetaUnit metaclass enables operator overloading at the class level, allowing syntax like `Meter / Second` to create new unit types dynamically

### Key Patterns

- **Immutability**: All core classes use `@dataclass(frozen=True, slots=True)`
- **Metaclass operators**: `MetaUnit` overloads `__mul__`, `__truediv__`, `__pow__` at the class level
- **Factory methods**: `Dimension.new_length()`, `Scale.new()` etc.
- **Dimensional analysis**: Scale stores separate conversion factors per base dimension

### Usage Example

```python
from physities.src.unit import *

Ms = Meter / Second           # Create composite unit type
Kh = Kilometer / Hour
v1 = Ms(40)                   # 40 m/s
v2 = Kh(144)                  # 144 km/h
v3 = v2.convert(Ms)           # Convert between units
```

## Conventions

- Conventional Commits style: `feat:`, `chore:`, `fix:`
- Tests marked with `@pytest.mark.unit`
- Test fixtures in `tests/fixtures/fixtures.py` with predefined units and scales
