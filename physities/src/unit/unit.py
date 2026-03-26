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
        return hash(self.scale)

    def __eq__(self, other):
        if isinstance(other, MetaUnit) and self.scale.dimension == other.scale.dimension and self.scale.conversion_factor == other.scale.conversion_factor:
            return True
        return False

    def __mul__(self, other):
        if isinstance(other, (int, float)):
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
        if isinstance(other, (int, float)):
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
        if isinstance(other, (int, float)):
            new_scale = other / self.scale
            return type(f"Unit", (Unit,), {"scale": new_scale, "value": None})
        raise InvalidOperationError(
            f"reverse division on {self}",
            type(other),
            (type(self), int, float),
        )

    def __pow__(self, power, modulo=None):
        if isinstance(power, (int, float)):
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
        if isinstance(other, (int, float)):
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
        if isinstance(other, (int, float)):
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
        if isinstance(other, (int, float)):
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
        if isinstance(power, (int, float)):
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

