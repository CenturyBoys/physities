import numbers
from typing import Self

from physities.src.exceptions import (
    DimensionMismatchError,
    InvalidConversionError,
    InvalidOperationError,
    InvalidPowerError,
)
from physities.src.scale.scale import Scale


class MetaUnit(type):
    """Metaclass enabling operator overloading on Unit classes.

    MetaUnit allows Unit types (not instances) to be combined using arithmetic
    operators to create new composite unit types. This enables syntax like
    ``Meter / Second`` to create a velocity unit type.

    Attributes:
        scale: The Scale defining this unit type's dimension and conversion factors.

    Examples:
        >>> # Create composite unit types
        >>> Velocity = Meter / Second
        >>> Acceleration = Meter / (Second ** 2)
        >>> Force = Kilogram * Acceleration

        >>> # Scale a unit type
        >>> Kilometer = Meter * 1000
    """

    scale: Scale

    def __hash__(self):
        if hasattr(self, 'scale') and self.scale is not None:
            return hash(self.scale)
        return hash(id(self))

    def __eq__(self, other):
        if not isinstance(other, MetaUnit):
            return False
        if not hasattr(self, 'scale') or not hasattr(other, 'scale'):
            return False
        if self.scale is None or other.scale is None:
            return False
        return (self.scale.dimension == other.scale.dimension and
                self.scale.conversion_factor == other.scale.conversion_factor)

    def __mul__(self, other):
        if isinstance(other, numbers.Real):
            new_scale = self.scale * other
            return type(self)(f"Unit", (Unit,), {"scale": new_scale, "value": None})
        if isinstance(other, MetaUnit):
            new_scale = self.scale * other.scale
            return type(f"Unit", (Unit,), {"scale": new_scale, "value": None})
        raise InvalidOperationError(
            f"multiplication on {self}",
            type(other),
            (type(self), int, float),
        )

    def __rmul__(self, other):
        try:
            to_return = MetaUnit.__mul__(self, other)
        except TypeError as e:
            raise e
        return to_return

    def __truediv__(self, other):
        if isinstance(other, numbers.Real):
            new_scale = self.scale / other
            return type(f"Unit", (Unit,), {"scale": new_scale, "value": None})
        if isinstance(other, MetaUnit):
            new_scale = self.scale / other.scale
            return type(f"Unit", (Unit,), {"scale": new_scale, "value": None})
        raise InvalidOperationError(
            f"division on {self}",
            type(other),
            (type(self), int, float),
        )

    def __rtruediv__(self, other):
        if isinstance(other, numbers.Real):
            new_scale = other / self.scale
            return type(f"Unit", (Unit,), {"scale": new_scale, "value": None})
        raise InvalidOperationError(
            f"reverse division on {self}",
            type(other),
            (type(self), int, float),
        )

    def __pow__(self, power, modulo=None):
        if isinstance(power, numbers.Real):
            new_scale = self.scale**power
            return type(f"Unit", (Unit,), {"scale": new_scale, "value": None})
        raise InvalidPowerError(self, power)

    def __add__(self, other):
        raise InvalidOperationError(
            "addition on unit types",
            type(other),
        )

    def __sub__(self, other):
        raise InvalidOperationError(
            "subtraction on unit types",
            type(other),
        )

    def __radd__(self, other):
        raise InvalidOperationError(
            "addition on unit types",
            type(other),
        )

    def __rsub__(self, other):
        raise InvalidOperationError(
            "subtraction on unit types",
            type(other),
        )


class Unit(metaclass=MetaUnit):
    """Base class for physical quantity values with units.

    Unit represents a physical quantity with both a numeric value and a unit
    (defined by its Scale). It supports arithmetic operations that properly
    handle unit conversions and dimensional analysis.

    Attributes:
        scale: The Scale defining this unit's dimension and conversion factors.
        value: The numeric value in this unit.

    Examples:
        >>> # Create values with units
        >>> distance = Meter(100)
        >>> time = Second(10)

        >>> # Arithmetic operations
        >>> velocity = distance / time  # Creates a m/s value
        >>> doubled = velocity * 2
        >>> total = Meter(50) + Meter(30)

        >>> # Unit conversion
        >>> km = Meter(1000).convert(Kilometer)  # 1 km

        >>> # Equality across units
        >>> Meter(1000) == Kilometer(1)  # True
    """

    scale: Scale
    value: float | int

    def __init__(self, value: float | int):
        """Create a new Unit instance with the given value.

        Args:
            value: The numeric value in this unit.
        """
        self.value = value

    def __eq__(self, other):
        if isinstance(other, Unit) and self.scale.dimension == other.scale.dimension:
            if self.value == other.convert(self).value:
                return True
        return False

    def __repr__(self):
        dimension = self.scale.dimension.show_dimension()
        if not dimension:
            return f"{self.value} (Scalar)"
        return f"{self.value} ({dimension})"

    def __str__(self):
        return f"{self.value}"

    def __add__(self, other):
        if isinstance(other, Unit):
            if self.scale.dimension == other.scale.dimension:
                new_value = self.value + other.convert(self).value
                new_instance = type(self)(new_value)
                new_instance.scale = self.scale
                return new_instance
            raise DimensionMismatchError(
                self.scale.dimension, other.scale.dimension, "addition"
            )
        raise InvalidOperationError("addition", type(other), (Unit,))

    def __sub__(self, other):
        if isinstance(other, Unit):
            if self.scale.dimension == other.scale.dimension:
                new_value = self.value - other.convert(self).value
                new_instance = type(self)(new_value)
                new_instance.scale = self.scale
                return new_instance
            raise DimensionMismatchError(
                self.scale.dimension, other.scale.dimension, "subtraction"
            )
        raise InvalidOperationError("subtraction", type(other), (Unit,))

    def __mul__(self, other):
        if isinstance(other, numbers.Real):
            new_value = self.value * other
            new_instance = type(self)(new_value)
            new_instance.scale = self.scale
            return new_instance
        if isinstance(other, Unit):
            new_scale = self.scale * other.scale
            new_value = self.value * other.value
            if new_scale.is_dimensionless:
                new_value *= new_scale.conversion_factor
                new_scale = Scale.new()
            new_instance = type(self)(new_value)
            new_instance.scale = new_scale
            return new_instance
        raise InvalidOperationError(
            f"multiplication on {type(self).__name__}",
            type(other),
            (Unit, int, float),
        )

    def __rmul__(self, other):
        try:
            to_return = Unit.__mul__(self, other)
        except TypeError as e:
            raise e
        return to_return

    def __truediv__(self, other):
        if isinstance(other, numbers.Real):
            new_value = self.value / other
            new_instance = type(self)(new_value)
            new_instance.scale = self.scale
            return new_instance
        if isinstance(other, Unit):
            new_scale = self.scale / other.scale
            new_value = self.value / other.value
            if new_scale.is_dimensionless:
                new_value *= new_scale.conversion_factor
                new_scale = Scale.new()
            new_instance = type(self)(new_value)
            new_instance.scale = new_scale
            return new_instance
        raise InvalidOperationError(
            f"division on {type(self).__name__}",
            type(other),
            (Unit, int, float),
        )

    def __rtruediv__(self, other):
        if isinstance(other, numbers.Real):
            new_value = other / self.value
            new_scale = 1 / self.scale
            new_instance = type(self)(new_value)
            new_instance.scale = new_scale
            return new_instance
        raise InvalidOperationError(
            f"reverse division on {type(self).__name__}",
            type(other),
            (Unit, int, float),
        )

    def __pow__(self, power, modulo=None):
        if isinstance(power, numbers.Real):
            new_value = self.value**power
            new_instance = type(self)(new_value)
            new_scale = self.scale**power
            new_instance.scale = new_scale
            return new_instance
        raise InvalidPowerError(type(self).__name__, power)

    def to_si(self) -> Self:
        """Convert this value to SI base units.

        Returns:
            A new Unit instance with the value in SI base units.

        Example:
            >>> km = Kilometer(5)
            >>> m = km.to_si()
            >>> m.value
            5000.0
        """
        new_value = self.value * self.scale.conversion_factor
        new_instance = type(self)(new_value)
        new_scale = Scale.new(dimension=self.scale.dimension)
        new_instance.scale = new_scale
        return new_instance

    def convert(self, unit: MetaUnit | Self) -> Self:
        """Convert this value to a different unit with the same dimension.

        Args:
            unit: The target unit type or instance to convert to.

        Returns:
            A new Unit instance with the value in the target unit.

        Raises:
            DimensionMismatchError: If the dimensions don't match.
            InvalidConversionError: If the target is not a valid unit.

        Example:
            >>> speed_ms = (Meter / Second)(10)
            >>> speed_kmh = speed_ms.convert(Kilometer / Hour)
            >>> speed_kmh.value
            36.0
        """
        if isinstance(unit, (MetaUnit, Unit)):
            if self.scale.dimension == unit.scale.dimension:
                new_value = (
                    self.value * self.scale.conversion_factor / unit.scale.conversion_factor
                )
                new_instance = type(self)(new_value)
                new_instance.scale = unit.scale
                return new_instance
            raise DimensionMismatchError(
                self.scale.dimension, unit.scale.dimension, "conversion"
            )
        raise InvalidConversionError(type(self).__name__, type(unit).__name__)

    # =========================================================================
    # Serialization for Database Storage
    # =========================================================================

    def to_dict(self) -> dict:
        """Serialize to a dictionary for database/JSON storage.

        Returns:
            Dictionary with 'value', 'si_value', and 'scale' information.

        Example:
            >>> m = Meter(100)
            >>> m.to_dict()
            {'value': 100, 'si_value': 100.0, 'dimension_int64': 1, 'scale_json': '...'}
        """
        rust_scale = self.scale.to_rust()
        return {
            "value": self.value,
            "si_value": self.value * self.scale.conversion_factor,
            "dimension_int64": rust_scale.to_dimension_int64(),
            "scale_json": rust_scale.to_json(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Unit":
        """Deserialize from a dictionary.

        Args:
            data: Dictionary with serialization data.

        Returns:
            A new Unit instance.

        Example:
            >>> data = {'si_value': 100.0, 'dimension_int64': 1}
            >>> unit = Unit.from_dict(data)
        """
        from physities._physities_core import PhysicalScale as RustScale

        if "scale_json" in data:
            rust_scale = RustScale.from_json(data["scale_json"])
            scale = Scale.from_rust(rust_scale)
            value = data.get("value", data.get("si_value", 0))
        elif "dimension_int64" in data:
            rust_scale = RustScale.from_dimension_int64(data["dimension_int64"])
            scale = Scale.from_rust(rust_scale)
            value = data.get("si_value", data.get("value", 0))
        else:
            raise ValueError("Missing 'scale_json' or 'dimension_int64' in data")

        instance = cls(value)
        instance.scale = scale
        return instance

    def to_tuple(self) -> tuple:
        """Compact serialization as (si_value, dimension_int64).

        Best for database columns: store as two columns (FLOAT8, INT8).
        Values are always stored in SI base units for consistency.

        Returns:
            Tuple of (si_value, dimension_int64).

        Example:
            >>> velocity = (Meter / Second)(10)
            >>> velocity.to_tuple()
            (10.0, 61441)
        """
        si_value = self.value * self.scale.conversion_factor
        dim_int = self.scale.to_rust().to_dimension_int64()
        return (si_value, dim_int)

    @classmethod
    def from_tuple(cls, data: tuple) -> "Unit":
        """Deserialize from compact tuple format.

        Args:
            data: Tuple of (si_value, dimension_int64).

        Returns:
            A new Unit instance in SI base units.

        Example:
            >>> unit = Unit.from_tuple((10.0, 61441))  # 10 m/s
        """
        si_value, dim_int = data

        from physities._physities_core import PhysicalScale as RustScale
        rust_scale = RustScale.from_dimension_int64(dim_int)
        scale = Scale.from_rust(rust_scale)

        instance = cls(si_value)
        instance.scale = scale
        return instance

