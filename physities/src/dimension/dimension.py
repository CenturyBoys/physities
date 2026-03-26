from dataclasses import dataclass
from typing import Optional, Self

from physities.src.dimension.base_dimensions import BaseDimension
from physities.src.exceptions import InvalidDimensionError, InvalidOperationError, InvalidPowerError

# Try to import the Rust backend for high-performance operations
try:
    from physities._physities_core import PhysicalScale as RustPhysicalScale
    _HAS_RUST = True
except ImportError:
    _HAS_RUST = False
    RustPhysicalScale = None

# Enable Rust for Dimension operations by default.
# Benchmarks show ~40% speedup when accounting for full Python
# object creation overhead (frozen dataclasses).
# Disable via Dimension.disable_rust() if needed.
_USE_RUST_FOR_OPS = True


def _dimension_to_rust(dim: "Dimension") -> "RustPhysicalScale":
    """Convert a Python Dimension to a Rust PhysicalScale.

    Only the dimension exponents are set; conversion factors default to 1.0.
    """
    if not _HAS_RUST:
        raise RuntimeError("Rust backend not available")

    return RustPhysicalScale.from_components(
        dim.dimensions_tuple,
        (1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0),  # default conversions
        1.0,  # default rescale
    )


def _rust_to_dimension(rust_scale: "RustPhysicalScale") -> "Dimension":
    """Convert a Rust PhysicalScale to a Python Dimension.

    Only extracts dimension exponents, ignores conversion factors.
    """
    dim_tuple = (
        rust_scale.length,
        rust_scale.mass,
        rust_scale.temperature,
        rust_scale.time,
        rust_scale.amount,
        rust_scale.electric_current,
        rust_scale.luminous_intensity,
    )
    return Dimension(dimensions_tuple=dim_tuple)

SYMBOLS = {
    BaseDimension.LENGTH: "L",
    BaseDimension.MASS: "m",
    BaseDimension.TIME: "t",
    BaseDimension.TEMPERATURE: "T",
    BaseDimension.AMOUNT: "N",
    BaseDimension.ELECTRIC_CURRENT: "I",
    BaseDimension.LUMINOUS_INTENSITY: "Iᵥ",
}

NUMBER_STR_TO_POWER_STR = {
    "0": "⁰",
    "1": "¹",
    "2": "²",
    "3": "³",
    "4": "⁴",
    "5": "⁵",
    "6": "⁶",
    "7": "⁷",
    "8": "⁸",
    "9": "⁹",
    ".": "ˑ",
}


@dataclass(frozen=True, slots=True)
class Dimension:
    """Represents physical dimensions using the 7 SI base dimensions.

    A Dimension object stores exponents for each of the 7 SI base dimensions:
    LENGTH, MASS, TEMPERATURE, TIME, AMOUNT, ELECTRIC_CURRENT, and LUMINOUS_INTENSITY.

    Dimensions are immutable (frozen dataclass) and support arithmetic operations
    that combine dimensions algebraically (e.g., velocity = length / time).

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

    dimensions_tuple: tuple[
        float,
        float,
        float,
        float,
        float,
        float,
        float,
    ]

    @property
    def length(self) -> float:
        """The length dimension exponent (L)."""
        return self.dimensions_tuple[BaseDimension.LENGTH]

    @property
    def mass(self) -> float:
        """The mass dimension exponent (M)."""
        return self.dimensions_tuple[BaseDimension.MASS]

    @property
    def temperature(self) -> float:
        """The temperature dimension exponent (Θ)."""
        return self.dimensions_tuple[BaseDimension.TEMPERATURE]

    @property
    def time(self) -> float:
        """The time dimension exponent (T)."""
        return self.dimensions_tuple[BaseDimension.TIME]

    @property
    def amount(self) -> float:
        """The amount of substance dimension exponent (N)."""
        return self.dimensions_tuple[BaseDimension.AMOUNT]

    @property
    def electric_current(self) -> float:
        """The electric current dimension exponent (I)."""
        return self.dimensions_tuple[BaseDimension.ELECTRIC_CURRENT]

    @property
    def luminous_intensity(self) -> float:
        """The luminous intensity dimension exponent (J)."""
        return self.dimensions_tuple[BaseDimension.LUMINOUS_INTENSITY]

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
        return Dimension(dimensions_tuple=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0))

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
        return Dimension(dimensions_tuple=dimensions_tuple)

    def get_dimensions(self) -> list[BaseDimension]:
        """Get the list of non-zero base dimensions.

        Returns:
            A list of BaseDimension values that have non-zero exponents.

        Example:
            >>> velocity = Dimension.new_instance((1, 0, 0, -1, 0, 0, 0))
            >>> velocity.get_dimensions()
            [<BaseDimension.LENGTH: 0>, <BaseDimension.TIME: 3>]
        """
        return [
            BaseDimension(i)
            for i in range(len(self.dimensions_tuple))
            if self.dimensions_tuple[i] != 0
        ]

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
        return self.dimensions_tuple[index]

    def to_rust(self) -> Optional["RustPhysicalScale"]:
        """Convert this Dimension to a Rust PhysicalScale.

        Returns:
            A RustPhysicalScale if Rust backend is available, None otherwise.
        """
        if _HAS_RUST:
            return _dimension_to_rust(self)
        return None

    @staticmethod
    def from_rust(rust_scale: "RustPhysicalScale") -> "Dimension":
        """Create a Dimension from a Rust PhysicalScale.

        Args:
            rust_scale: The Rust PhysicalScale instance.

        Returns:
            A Python Dimension with the dimension exponents.
        """
        return _rust_to_dimension(rust_scale)

    @staticmethod
    def has_rust_backend() -> bool:
        """Check if the Rust backend is available.

        Returns:
            True if Rust acceleration is available.
        """
        return _HAS_RUST

    @staticmethod
    def is_rust_enabled() -> bool:
        """Check if Rust is enabled for Dimension operations.

        Returns:
            True if Rust is being used for operations.
        """
        return _HAS_RUST and _USE_RUST_FOR_OPS

    @staticmethod
    def enable_rust():
        """Enable Rust for Dimension operations.

        Use this for batch processing where conversion overhead is amortized.
        For single operations, pure Python is faster due to conversion overhead.
        """
        global _USE_RUST_FOR_OPS
        if _HAS_RUST:
            _USE_RUST_FOR_OPS = True

    @staticmethod
    def disable_rust():
        """Disable Rust for Dimension operations (default).

        Pure Python is faster for single operations due to conversion overhead.
        """
        global _USE_RUST_FOR_OPS
        _USE_RUST_FOR_OPS = False

    def __add__(self, other):
        if isinstance(other, Dimension):
            # Use Rust backend when enabled (disabled by default for performance)
            if _USE_RUST_FOR_OPS:
                rust_result = _dimension_to_rust(self).add_dimensions(_dimension_to_rust(other))
                return _rust_to_dimension(rust_result)

            # Fallback to Python
            dimensions_tuple = tuple(
                sum(i) for i in zip(self.dimensions_tuple, other.dimensions_tuple)
            )
            return Dimension(dimensions_tuple=dimensions_tuple)
        else:
            raise InvalidOperationError("addition on Dimension", type(other), (Dimension,))

    def __radd__(self, other):
        try:
            to_return = self.__add__(other)
        except TypeError as e:
            raise e
        return to_return

    def __sub__(self, other):
        if isinstance(other, Dimension):
            # Use Rust backend when enabled (disabled by default for performance)
            if _USE_RUST_FOR_OPS:
                rust_result = _dimension_to_rust(self).subtract_dimensions(_dimension_to_rust(other))
                return _rust_to_dimension(rust_result)

            # Fallback to Python
            negative_other_dimensions_tuple = tuple(-i for i in other.dimensions_tuple)
            dimensions_tuple = tuple(
                sum(i)
                for i in zip(self.dimensions_tuple, negative_other_dimensions_tuple)
            )
            return Dimension(dimensions_tuple=dimensions_tuple)
        else:
            raise InvalidOperationError("subtraction on Dimension", type(other), (Dimension,))

    def __rsub__(self, other):
        try:
            to_return = self.__sub__(other)
        except TypeError as e:
            raise e
        return to_return

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            # Use Rust backend when enabled (disabled by default for performance)
            if _USE_RUST_FOR_OPS:
                rust_result = _dimension_to_rust(self).multiply_dimensions(float(other))
                return _rust_to_dimension(rust_result)

            # Fallback to Python
            dimensions_tuple = tuple(other * i for i in self.dimensions_tuple)
            return Dimension(dimensions_tuple=dimensions_tuple)
        else:
            raise InvalidOperationError("multiplication on Dimension", type(other), (int, float))

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            # Use Rust backend when enabled (disabled by default for performance)
            if _USE_RUST_FOR_OPS:
                rust_result = _dimension_to_rust(self).multiply_dimensions(float(other))
                return _rust_to_dimension(rust_result)

            # Fallback to Python
            dimensions_tuple = tuple(other * i for i in self.dimensions_tuple)
            return Dimension(dimensions_tuple=dimensions_tuple)
        else:
            raise InvalidOperationError("multiplication on Dimension", type(other), (int, float))

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            # Use Rust backend when enabled (disabled by default for performance)
            if _USE_RUST_FOR_OPS:
                rust_result = _dimension_to_rust(self).divide_dimensions(float(other))
                return _rust_to_dimension(rust_result)

            # Fallback to Python
            dimensions_tuple = tuple(i / other for i in self.dimensions_tuple)
            return Dimension(dimensions_tuple=dimensions_tuple)
        else:
            raise InvalidOperationError("division on Dimension", type(other), (int, float))

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            dimensions_tuple = tuple(other / i for i in self.dimensions_tuple)
            return Dimension(dimensions_tuple=dimensions_tuple)
        else:
            raise InvalidOperationError("reverse division on Dimension", type(other), (int, float))

    def __eq__(self, other):
        if isinstance(other, Dimension) or issubclass(type(other), Dimension):
            if other.dimensions_tuple == self.dimensions_tuple:
                return True
        return False

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
            'L¹ / t¹'
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
            power_str = "".join([NUMBER_STR_TO_POWER_STR[i] for i in str(power)])
            if is_numerator:
                numerator += f"{SYMBOLS[BaseDimension(i)]}{power_str}"
            else:
                denominator += f"{SYMBOLS[BaseDimension(i)]}{power_str}"
        if not denominator:
            to_print = f"{numerator}"
            print()
        elif not numerator:
            to_print = f"1 / {denominator}"
            print()
        else:
            to_print = f"{numerator} / {denominator}"
        # print(to_print)
        return to_print
