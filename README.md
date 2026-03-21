# Physities

A Python library for representing and working with physical quantities and units. Provides dimensional analysis, unit conversion, and mathematical operations on physical measurements.

## Installation

```bash
pip install physities
```

Or with Poetry:

```bash
poetry add physities
```

## Quick Start

```python
from physities.src.unit import Meter, Second, Kilometer, Hour

# Create composite unit types using operator syntax
MetersPerSecond = Meter / Second
KilometersPerHour = Kilometer / Hour

# Create values
v1 = MetersPerSecond(40)      # 40 m/s
v2 = KilometersPerHour(144)   # 144 km/h

# Convert between units
v3 = v2.convert(MetersPerSecond)  # 40 m/s
```

## Available Units

### Base SI Units

| Dimension          | Base Unit  |
|--------------------|------------|
| Length             | Meter      |
| Mass               | Kilogram   |
| Time               | Second     |
| Temperature        | Kelvin     |
| Amount             | Unity      |
| Electric Current   | Ampere     |
| Luminous Intensity | Candela    |

### Derived Units

#### Length
Gigameter, Megameter, Kilometer, Hectometer, Decameter, Decimeter, Centimeter, Millimeter, Micrometer, Nanometer, Foot, Yard, Inch, Mile, Furlong, Rod

#### Time
Nanosecond, Microsecond, Millisecond, Centisecond, Decisecond, Minute, Hour, Day, Week, Month, Year, Decade, Century, Millennium

#### Mass
Gigagram, Megagram, Tonne, Hectogram, Decagram, Gram, Decigram, Centigram, Milligram, Microgram, Nanogram, Pound, Ounce, Stone, Carat, Grain, Slug

#### Electric Current
Gigaampere, Megaampere, Kiloampere, Milliampere, Microampere, Nanoampere

#### Amount
Dozen, Moles, Pairs, Score

#### Area
Meter2, Kilometer2, Hectare, Centimeter2, Millimeter2, Foot2, Yard2, Inch2, Mile2, Acre

#### Volume
Meter3, Liter, Kiloliter, Milliliter, Centimeter3, Foot3, Gallon, Pint, Barrel

## Examples

### Creating and Using Units

```python
from physities.src.unit import Meter, Second, Kilogram

# Create a velocity unit
Velocity = Meter / Second
v = Velocity(10)  # 10 m/s

# Create an acceleration unit
Acceleration = Meter / (Second ** 2)
a = Acceleration(9.8)  # 9.8 m/s²

# Create a force unit (Newton)
Newton = Kilogram * Meter / (Second ** 2)
force = Newton(100)  # 100 N
```

### Unit Conversion

```python
from physities.src.unit import Kilometer, Mile, Hour

# Create speed units
Kmh = Kilometer / Hour
Mph = Mile / Hour

# Convert between units
speed_kmh = Kmh(100)
speed_mph = speed_kmh.convert(Mph)
```

### Mathematical Operations

```python
from physities.src.unit import Meter, Second

Ms = Meter / Second

v1 = Ms(10)
v2 = Ms(20)

# Addition and subtraction (same units only)
v3 = v1 + v2  # 30 m/s
v4 = v2 - v1  # 10 m/s

# Multiplication and division with scalars
v5 = v1 * 2   # 20 m/s
v6 = v2 / 2   # 10 m/s
```

### Creating Custom Units

```python
from physities.src.unit import Unit
from physities.src.scale import Scale
from physities.src.dimension import Dimension

# Define a custom unit
class Furlong(Unit):
    scale = Scale(
        dimension=Dimension.new_length(),
        from_base_scale_conversions=(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0),
        rescale_value=201.168,  # 1 furlong = 201.168 meters
    )
    value = None

# Or derive from existing units
from physities.src.unit import Meter
MyUnit = 201.168 * Meter  # Equivalent to Furlong
```

## Architecture

Physities uses a three-layer architecture:

1. **BaseDimension**: Enum of 7 SI base dimensions
2. **Dimension**: Frozen dataclass combining base dimensions into composite physical dimensions
3. **Scale**: Frozen dataclass with dimension + conversion factors
4. **Unit + MetaUnit**: MetaUnit metaclass enables operator overloading at the class level

The metaclass pattern allows elegant syntax like `Meter / Second` to create new unit types dynamically.

## API Reference

### Unit Class

The main class for working with physical quantities.

```python
class Unit:
    scale: Scale      # The scale/unit definition
    value: float      # The numeric value

    def convert(self, target: Type[Unit]) -> Unit:
        """Convert to another unit of the same dimension."""
```

### Scale Class

Defines unit conversion factors.

```python
@dataclass(frozen=True, slots=True)
class Scale:
    dimension: Dimension
    from_base_scale_conversions: tuple[float, ...]
    rescale_value: float
```

### Dimension Class

Represents physical dimensions.

```python
@dataclass(frozen=True, slots=True)
class Dimension:
    dimensions: tuple[int, ...]

    @classmethod
    def new_length(cls) -> Dimension: ...
    @classmethod
    def new_mass(cls) -> Dimension: ...
    @classmethod
    def new_time(cls) -> Dimension: ...
    @classmethod
    def new_temperature(cls) -> Dimension: ...
    @classmethod
    def new_amount(cls) -> Dimension: ...
    @classmethod
    def new_electric_current(cls) -> Dimension: ...
    @classmethod
    def new_luminous_intensity(cls) -> Dimension: ...
```

### BaseDimension Enum

The 7 SI base dimensions:

```python
class BaseDimension(Enum):
    LENGTH = 0
    MASS = 1
    TEMPERATURE = 2
    TIME = 3
    AMOUNT = 4
    ELECTRIC_CURRENT = 5
    LUMINOUS_INTENSITY = 6
```

## Development

```bash
# Install dependencies
poetry install

# Run tests
pytest

# Run linting
ruff check .
```

## License

MIT
