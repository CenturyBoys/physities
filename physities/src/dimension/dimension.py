from typing import Self

from physities.src.dimension.base_dimensions import BaseDimension
from physities.src.exceptions import InvalidDimensionError, InvalidOperationError, InvalidPowerError

# Import the Rust backend
from physities._physities_core import PhysicalDimension as _RustDimension

SYMBOLS = {
    BaseDimension.LENGTH: "L",
    BaseDimension.MASS: "m",
    BaseDimension.TIME: "t",
    BaseDimension.TEMPERATURE: "T",
    BaseDimension.AMOUNT: "N",
    BaseDimension.ELECTRIC_CURRENT: "I",
    BaseDimension.LUMINOUS_INTENSITY: "I\u1d65",  # Iᵥ - subscript v
}

NUMBER_STR_TO_POWER_STR = {
    "0": "\u2070",
    "1": "\u00b9",
    "2": "\u00b2",
    "3": "\u00b3",
    "4": "\u2074",
    "5": "\u2075",
    "6": "\u2076",
    "7": "\u2077",
    "8": "\u2078",
    "9": "\u2079",
    ".": "\u02d1",
}


class Dimension:
    """Represents physical dimensions using the 7 SI base dimensions.

    A Dimension object stores exponents for each of the 7 SI base dimensions:
    LENGTH, MASS, TEMPERATURE, TIME, AMOUNT, ELECTRIC_CURRENT, and LUMINOUS_INTENSITY.

    Dimensions are immutable and support arithmetic operations
    that combine dimensions algebraically (e.g., velocity = length / time).

    This class is a thin wrapper around the Rust PhysicalDimension for high performance.

    Attributes:
        dimensions_tuple: A 7-element tuple of floats representing the exponent
            of each base dimension in order.

    Examples:
        >>> # Create a velocity dimension (length / time)
        >>> velocity = Dimension.new_instance((1, 0, 0, -1, 0, 0, 0))
        >>> velocity.length
        1
        >>> velocity.time
        -1

        >>> # Create using factory methods
        >>> length = Dimension.new_length()
        >>> time = Dimension.new_time()
        >>> velocity = length + (time * -1)

        >>> # Check if dimensionless
        >>> dimensionless = Dimension.new_dimensionless()
        >>> dimensionless.get_dimensions()
        []
    """

    __slots__ = ('_rust',)

    def __init__(self, *, dimensions_tuple: tuple[float, float, float, float, float, float, float]):
        """Create a new Dimension from a tuple of exponents.

        Args:
            dimensions_tuple: A 7-element tuple of exponents in order:
                (LENGTH, MASS, TEMPERATURE, TIME, AMOUNT, ELECTRIC_CURRENT, LUMINOUS_INTENSITY)
        """
        self._rust = _RustDimension(dimensions_tuple)

    @classmethod
    def _from_rust(cls, rust_dim: _RustDimension) -> Self:
        """Create a Dimension from a Rust PhysicalDimension (internal use)."""
        instance = object.__new__(cls)
        instance._rust = rust_dim
        return instance

    @property
    def dimensions_tuple(self) -> tuple[float, float, float, float, float, float, float]:
        """The 7-element tuple of dimension exponents."""
        return tuple(self._rust.dimensions_tuple)

    @property
    def length(self) -> float:
        """The length dimension exponent (L)."""
        return self._rust.length

    @property
    def mass(self) -> float:
        """The mass dimension exponent (M)."""
        return self._rust.mass

    @property
    def temperature(self) -> float:
        """The temperature dimension exponent (Theta)."""
        return self._rust.temperature

    @property
    def time(self) -> float:
        """The time dimension exponent (T)."""
        return self._rust.time

    @property
    def amount(self) -> float:
        """The amount of substance dimension exponent (N)."""
        return self._rust.amount

    @property
    def electric_current(self) -> float:
        """The electric current dimension exponent (I)."""
        return self._rust.electric_current

    @property
    def luminous_intensity(self) -> float:
        """The luminous intensity dimension exponent (J)."""
        return self._rust.luminous_intensity

    @classmethod
    def new_time(cls, power: float = None) -> Self:
        """Create a time dimension with the given power.

        Args:
            power: The exponent for the time dimension. Defaults to 1.

        Returns:
            A new Dimension with only time dimension set.

        Example:
            >>> time = Dimension.new_time()  # T^1
            >>> time_squared = Dimension.new_time(power=2)  # T^2
        """
        return cls.__new_base_unit(base_unit=BaseDimension.TIME, power=power)

    @classmethod
    def new_length(cls, power: float = None) -> Self:
        """Create a length dimension with the given power.

        Args:
            power: The exponent for the length dimension. Defaults to 1.

        Returns:
            A new Dimension with only length dimension set.

        Example:
            >>> length = Dimension.new_length()  # L^1
            >>> area = Dimension.new_length(power=2)  # L^2
        """
        return cls.__new_base_unit(base_unit=BaseDimension.LENGTH, power=power)

    @classmethod
    def new_temperature(cls, power: float = None) -> Self:
        """Create a temperature dimension with the given power.

        Args:
            power: The exponent for the temperature dimension. Defaults to 1.

        Returns:
            A new Dimension with only temperature dimension set.
        """
        return cls.__new_base_unit(base_unit=BaseDimension.TEMPERATURE, power=power)

    @classmethod
    def new_mass(cls, power: float = None) -> Self:
        """Create a mass dimension with the given power.

        Args:
            power: The exponent for the mass dimension. Defaults to 1.

        Returns:
            A new Dimension with only mass dimension set.

        Example:
            >>> mass = Dimension.new_mass()  # M^1
        """
        return cls.__new_base_unit(base_unit=BaseDimension.MASS, power=power)

    @classmethod
    def new_amount(cls, power: float = None) -> Self:
        """Create an amount of substance dimension with the given power.

        Args:
            power: The exponent for the amount dimension. Defaults to 1.

        Returns:
            A new Dimension with only amount dimension set.
        """
        return cls.__new_base_unit(base_unit=BaseDimension.AMOUNT, power=power)

    @classmethod
    def new_electric_current(cls, power: float = None) -> Self:
        """Create an electric current dimension with the given power.

        Args:
            power: The exponent for the electric current dimension. Defaults to 1.

        Returns:
            A new Dimension with only electric current dimension set.
        """
        return cls.__new_base_unit(
            base_unit=BaseDimension.ELECTRIC_CURRENT, power=power
        )

    @classmethod
    def new_luminous_intensity(cls, power: float = None) -> Self:
        """Create a luminous intensity dimension with the given power.

        Args:
            power: The exponent for the luminous intensity dimension. Defaults to 1.

        Returns:
            A new Dimension with only luminous intensity dimension set.
        """
        return cls.__new_base_unit(
            base_unit=BaseDimension.LUMINOUS_INTENSITY, power=power
        )

    @classmethod
    def new_dimensionless(cls) -> Self:
        """Create a dimensionless dimension (all exponents are zero).

        Returns:
            A new Dimension with all exponents set to zero.

        Example:
            >>> dimensionless = Dimension.new_dimensionless()
            >>> dimensionless.get_dimensions()
            []
        """
        return cls._from_rust(_RustDimension.new_dimensionless())

    @classmethod
    def __new_base_unit(cls, base_unit: BaseDimension, power: float = None):
        if power is None:
            power = 1
        elif not isinstance(power, (int, float)):
            raise InvalidDimensionError("The exponentiation must be an int or a float.")
        dimensions_tuple = [0.0 for _ in BaseDimension]
        dimensions_tuple[base_unit] = power
        return cls.new_instance(dimensions_tuple=tuple(dimensions_tuple))

    @classmethod
    def new_instance(
        cls,
        dimensions_tuple: tuple[float, float, float, float, float, float, float],
    ) -> Self:
        """Create a new Dimension from a tuple of exponents.

        Args:
            dimensions_tuple: A 7-element tuple of exponents in order:
                (LENGTH, MASS, TEMPERATURE, TIME, AMOUNT, ELECTRIC_CURRENT, LUMINOUS_INTENSITY)

        Returns:
            A new Dimension instance.

        Example:
            >>> # Velocity dimension (L^1 * T^-1)
            >>> velocity = Dimension.new_instance((1, 0, 0, -1, 0, 0, 0))
        """
        return cls(dimensions_tuple=dimensions_tuple)

    def get_dimensions(self) -> list[BaseDimension]:
        """Get the list of non-zero base dimensions.

        Returns:
            A list of BaseDimension values that have non-zero exponents.

        Example:
            >>> velocity = Dimension.new_instance((1, 0, 0, -1, 0, 0, 0))
            >>> velocity.get_dimensions()
            [<BaseDimension.LENGTH: 0>, <BaseDimension.TIME: 3>]
        """
        return [BaseDimension(i) for i in self._rust.get_dimensions()]

    def get(self, index: BaseDimension) -> float:
        """Get the exponent for a specific base dimension.

        Args:
            index: The BaseDimension to query.

        Returns:
            The exponent value for that dimension.

        Example:
            >>> velocity = Dimension.new_instance((1, 0, 0, -1, 0, 0, 0))
            >>> velocity.get(BaseDimension.LENGTH)
            1
        """
        return self._rust.get(int(index))

    @staticmethod
    def has_rust_backend() -> bool:
        """Check if the Rust backend is available.

        Returns:
            True - Rust backend is always available in this version.
        """
        return True

    @staticmethod
    def is_rust_enabled() -> bool:
        """Check if Rust is enabled for Dimension operations.

        Returns:
            True - Rust is always enabled in this version.
        """
        return True

    @staticmethod
    def enable_rust():
        """Enable Rust for Dimension operations.

        No-op in this version - Rust is always enabled.
        """
        pass

    @staticmethod
    def disable_rust():
        """Disable Rust for Dimension operations.

        No-op in this version - Rust is always enabled.
        """
        pass

    def __add__(self, other):
        if isinstance(other, Dimension):
            return Dimension._from_rust(self._rust + other._rust)
        else:
            raise InvalidOperationError("addition on Dimension", type(other), (Dimension,))

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Dimension):
            return Dimension._from_rust(self._rust - other._rust)
        else:
            raise InvalidOperationError("subtraction on Dimension", type(other), (Dimension,))

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Dimension._from_rust(self._rust * float(other))
        else:
            raise InvalidOperationError("multiplication on Dimension", type(other), (int, float))

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return Dimension._from_rust(self._rust * float(other))
        else:
            raise InvalidOperationError("multiplication on Dimension", type(other), (int, float))

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Dimension._from_rust(self._rust / float(other))
        else:
            raise InvalidOperationError("division on Dimension", type(other), (int, float))

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            return Dimension._from_rust(float(other) / self._rust)
        else:
            raise InvalidOperationError("reverse division on Dimension", type(other), (int, float))

    def __eq__(self, other):
        if isinstance(other, Dimension) or issubclass(type(other), Dimension):
            return self._rust == other._rust
        return False

    def __hash__(self):
        return hash(self._rust)

    def __pow__(self, power, modulo=None):
        raise InvalidPowerError("Dimension", power, "exponentiation with Dimension is not allowed")

    def __rpow__(self, power):
        raise InvalidPowerError("Dimension", power, "exponentiation with Dimension is not allowed")

    def show_dimension(self) -> str:
        """Generate a human-readable string representation of the dimension.

        Returns:
            A string showing the dimension in fraction notation with superscript exponents.

        Example:
            >>> velocity = Dimension.new_instance((1, 0, 0, -1, 0, 0, 0))
            >>> velocity.show_dimension()
            'L1 / t1'
        """
        numerator = ""
        denominator = ""
        for i in range(len(self.dimensions_tuple)):
            is_numerator = True
            power = self.dimensions_tuple[i]
            if power == 0:
                continue
            if power < 0:
                is_numerator = False
                power = abs(power)
            # Format integer-valued floats without decimal point
            if power == int(power):
                power_display = str(int(power))
            else:
                power_display = str(power)
            power_str = "".join([NUMBER_STR_TO_POWER_STR[c] for c in power_display])
            if is_numerator:
                numerator += f"{SYMBOLS[BaseDimension(i)]}{power_str}"
            else:
                denominator += f"{SYMBOLS[BaseDimension(i)]}{power_str}"
        if not denominator:
            to_print = f"{numerator}"
        elif not numerator:
            to_print = f"1 / {denominator}"
        else:
            to_print = f"{numerator} / {denominator}"
        return to_print

    def __repr__(self):
        return f"Dimension(dimensions_tuple={self.dimensions_tuple})"

    def __str__(self):
        return self.show_dimension()
