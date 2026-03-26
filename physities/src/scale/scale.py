from dataclasses import dataclass
from math import prod
from typing import Optional

from kobject import Kobject

from physities.src.dimension import Dimension
from physities.src.dimension.base_dimensions import BaseDimension
from physities.src.exceptions import InvalidOperationError, InvalidPowerError

# Try to import the Rust backend for high-performance operations
try:
    from physities._physities_core import PhysicalScale as RustPhysicalScale
    _HAS_RUST = True
except ImportError:
    _HAS_RUST = False
    RustPhysicalScale = None

# Enable Rust for Scale operations by default.
# Benchmarks show ~20% speedup for typical operations when accounting
# for full Python object creation overhead (frozen dataclasses, Kobject, etc.)
# Disable via Scale.disable_rust() if needed.
_USE_RUST_FOR_OPS = True


def _rust_to_scale(rust_scale: "RustPhysicalScale") -> "Scale":
    """Convert a Rust PhysicalScale to a Python Scale.

    Args:
        rust_scale: The Rust PhysicalScale instance.

    Returns:
        A Python Scale with the same data.
    """
    # Extract dimension exponents from Rust (indices 0-6)
    dim_tuple = (
        rust_scale.length,
        rust_scale.mass,
        rust_scale.temperature,
        rust_scale.time,
        rust_scale.amount,
        rust_scale.electric_current,
        rust_scale.luminous_intensity,
    )

    # Extract conversion factors (indices 7-13)
    conv_tuple = tuple(rust_scale.get_conversion(i) for i in range(7))

    # Create Dimension from exponents
    dimension = Dimension.new_instance(dim_tuple)

    return Scale(
        dimension=dimension,
        from_base_scale_conversions=conv_tuple,
        rescale_value=rust_scale.rescale_value,
    )


def _scale_to_rust(scale: "Scale") -> "RustPhysicalScale":
    """Convert a Python Scale to a Rust PhysicalScale.

    Args:
        scale: The Python Scale instance.

    Returns:
        A Rust PhysicalScale with the same data.
    """
    if not _HAS_RUST:
        raise RuntimeError("Rust backend not available")

    # Get dimension exponents
    dim_tuple = scale.dimension.dimensions_tuple

    return RustPhysicalScale.from_components(
        dim_tuple,
        scale.from_base_scale_conversions,
        float(scale.rescale_value),
    )


@dataclass(frozen=True, slots=True)
class Scale(Kobject):
    """Represents a unit scale with dimension and conversion factors.

    A Scale combines a Dimension with conversion factors that define how to
    convert from this scale to SI base units. It supports arithmetic operations
    that properly combine scales when multiplying/dividing units.

    The total conversion factor is: rescale_value * product(from_base_scale_conversions)

    Attributes:
        dimension: The physical Dimension of this scale.
        from_base_scale_conversions: A 7-element tuple of conversion factors,
            one for each base dimension. Each factor converts from this scale
            to the SI base unit for that dimension.
        rescale_value: An additional multiplicative factor for the conversion.

    Examples:
        >>> # Create a kilometer scale (1 km = 1000 m)
        >>> km_scale = Scale.new(
        ...     dimension=Dimension.new_length(),
        ...     from_base_scale_conversions=(1000, 1, 1, 1, 1, 1, 1),
        ... )
        >>> km_scale.conversion_factor
        1000

        >>> # Create a velocity scale (km/h)
        >>> velocity_dim = Dimension.new_instance((1, 0, 0, -1, 0, 0, 0))
        >>> kmh_scale = Scale.new(
        ...     dimension=velocity_dim,
        ...     from_base_scale_conversions=(1000, 1, 1, 3600, 1, 1, 1),
        ... )

        >>> # Combine scales
        >>> meter_scale = Scale.new(dimension=Dimension.new_length())
        >>> second_scale = Scale.new(dimension=Dimension.new_time())
        >>> ms_scale = meter_scale / second_scale
    """

    dimension: Dimension
    from_base_scale_conversions: tuple[
        float | int,
        float | int,
        float | int,
        float | int,
        float | int,
        float | int,
        float | int,
    ]
    rescale_value: float | int

    @classmethod
    def new(
        cls,
        dimension: Dimension = None,
        from_base_scale_conversions: tuple[
            float, float, float, float, float, float, float
        ] = None,
        rescale_value: float = None,
    ):
        """Create a new Scale with default SI values.

        Args:
            dimension: The physical dimension. Defaults to dimensionless.
            from_base_scale_conversions: Conversion factors for each base dimension.
                Defaults to (1, 1, 1, 1, 1, 1, 1) for SI units.
            rescale_value: Additional scaling factor. Defaults to 1.

        Returns:
            A new Scale instance.

        Example:
            >>> # Dimensionless SI scale
            >>> scale = Scale.new()

            >>> # Kilometer scale
            >>> km = Scale.new(
            ...     dimension=Dimension.new_length(),
            ...     from_base_scale_conversions=(1000, 1, 1, 1, 1, 1, 1),
            ... )
        """
        if from_base_scale_conversions is None:
            from_base_scale_conversions = (1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
        if rescale_value is None:
            rescale_value = 1
        if dimension is None:
            dimension = Dimension.new_dimensionless()

        return cls(
            dimension=dimension,
            from_base_scale_conversions=from_base_scale_conversions,
            rescale_value=rescale_value,
        )

    @property
    def is_dimensionless(self) -> bool:
        """Check if this scale represents a dimensionless quantity.

        Returns:
            True if all dimension exponents are zero, False otherwise.
        """
        if not self.dimension.get_dimensions():
            return True
        return False

    def to_rust(self) -> Optional["RustPhysicalScale"]:
        """Convert this Scale to a Rust PhysicalScale for high-performance operations.

        Returns:
            A RustPhysicalScale if the Rust backend is available, None otherwise.

        Example:
            >>> scale = Scale.new(dimension=Dimension.new_length())
            >>> rust_scale = scale.to_rust()
            >>> if rust_scale:
            ...     print(rust_scale.conversion_factor)
        """
        if _HAS_RUST:
            return _scale_to_rust(self)
        return None

    @staticmethod
    def from_rust(rust_scale: "RustPhysicalScale") -> "Scale":
        """Create a Scale from a Rust PhysicalScale.

        Args:
            rust_scale: The Rust PhysicalScale instance.

        Returns:
            A Python Scale with the same data.
        """
        return _rust_to_scale(rust_scale)

    @staticmethod
    def has_rust_backend() -> bool:
        """Check if the Rust backend is available.

        Returns:
            True if the Rust PhysicalScale is available for high-performance operations.
        """
        return _HAS_RUST

    @staticmethod
    def is_rust_enabled() -> bool:
        """Check if Rust is enabled for Scale operations.

        Returns:
            True if Rust is being used for operations.
        """
        return _HAS_RUST and _USE_RUST_FOR_OPS

    @staticmethod
    def enable_rust():
        """Enable Rust for Scale operations.

        Rust is faster for:
        - Batch processing with PhysicalScale directly
        - NumPy array interop
        - Serialization (JSON, int64 encoding)

        For single operations, pure Python is faster due to conversion overhead.
        """
        global _USE_RUST_FOR_OPS
        if _HAS_RUST:
            _USE_RUST_FOR_OPS = True

    @staticmethod
    def disable_rust():
        """Disable Rust for Scale operations (default).

        Pure Python is faster for single operations due to conversion overhead.
        """
        global _USE_RUST_FOR_OPS
        _USE_RUST_FOR_OPS = False

    @property
    def conversion_factor(self) -> float:
        """Calculate the total conversion factor to SI base units.

        Returns:
            The product of rescale_value and all base conversion factors.

        Example:
            >>> km = Scale.new(
            ...     dimension=Dimension.new_length(),
            ...     from_base_scale_conversions=(1000, 1, 1, 1, 1, 1, 1),
            ... )
            >>> km.conversion_factor
            1000.0
        """
        return self.rescale_value * prod(self.from_base_scale_conversions)

    @staticmethod
    def __get_annulled_dimension(
        dimension_1: Dimension, dimension_2: Dimension, result_dimension: Dimension
    ) -> list[
        BaseDimension,
        BaseDimension,
        BaseDimension,
        BaseDimension,
        BaseDimension,
        BaseDimension,
        BaseDimension,
    ]:
        set_1 = set(dimension_1.get_dimensions())
        set_2 = set(dimension_2.get_dimensions())
        set_3 = set(result_dimension.get_dimensions())
        return list((set_1 - set_3).union(set_2 - set_3))

    @staticmethod
    def __fit_scale_and_dimension(
        dimension_instance: Dimension,
        from_base_scale_conversions: tuple[
            float, float, float, float, float, float, float
        ],
        value: float,
        rescale_value: float,
    ):
        dimension = dimension_instance.get_dimensions()
        if len(dimension) == 1:
            index = dimension.pop()
            from_base_scale_conversions_list = list(from_base_scale_conversions)
            from_base_scale_conversions_list[index] *= rescale_value
            new_from_base_scale_conversions = tuple(from_base_scale_conversions_list)
            return 1, new_from_base_scale_conversions
        return rescale_value * value, from_base_scale_conversions

    def __eq__(self, other):
        if isinstance(other, Scale):
            if self.dimension == other.dimension and self.conversion_factor == other.conversion_factor:
                return True
        return False

    def __mul__(self, other):
        # Use Rust backend when enabled (disabled by default for single ops)
        if _USE_RUST_FOR_OPS:
            if isinstance(other, (int, float)):
                rust_result = _scale_to_rust(self).multiply_scalar(float(other))
                return _rust_to_scale(rust_result)
            if isinstance(other, Scale):
                rust_result = _scale_to_rust(self).multiply(_scale_to_rust(other))
                return _rust_to_scale(rust_result)

        # Fallback to pure Python implementation
        if isinstance(other, (int, float)):
            new_value, new_from_base_scale_conversions = self.__fit_scale_and_dimension(
                dimension_instance=self.dimension,
                from_base_scale_conversions=self.from_base_scale_conversions,
                rescale_value=other,
                value=self.rescale_value,
            )
            return Scale(
                dimension=self.dimension,
                from_base_scale_conversions=new_from_base_scale_conversions,
                rescale_value=new_value,
            )
        if isinstance(other, Scale):
            new_dimension = self.dimension + other.dimension
            new_from_base_scale_conversions_list = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
            rescale_factor = 1
            for i in BaseDimension:
                xxx = (
                    self.from_base_scale_conversions[i]
                    * other.from_base_scale_conversions[i]
                )
                if new_dimension.get(i) == 0 and (
                    self.dimension.get(i) != 0 or other.dimension.get(i) != 0
                ):
                    rescale_factor *= xxx
                    new_from_base_scale_conversions_list[i] = 1
                else:
                    new_from_base_scale_conversions_list[i] = xxx
            new_value, new_from_base_scale_conversions = self.__fit_scale_and_dimension(
                dimension_instance=new_dimension,
                from_base_scale_conversions=tuple(new_from_base_scale_conversions_list),
                rescale_value=self.rescale_value,
                value=rescale_factor,
            )
            return Scale(
                dimension=new_dimension,
                from_base_scale_conversions=new_from_base_scale_conversions,
                rescale_value=new_value,
            )
        raise InvalidOperationError(
            "multiplication on Scale",
            type(other),
            (Scale, int, float),
        )

    def __rmul__(self, other):
        try:
            to_return = Scale.__mul__(self, other)
        except TypeError as e:
            raise e
        return to_return

    def __truediv__(self, other):
        # Use Rust backend when enabled (disabled by default for single ops)
        if _USE_RUST_FOR_OPS:
            if isinstance(other, (int, float)):
                rust_result = _scale_to_rust(self).divide_scalar(float(other))
                return _rust_to_scale(rust_result)
            if isinstance(other, Scale):
                rust_result = _scale_to_rust(self).divide(_scale_to_rust(other))
                return _rust_to_scale(rust_result)

        # Fallback to pure Python implementation
        if isinstance(other, (int, float)):
            new_value, new_from_base_scale_conversions = self.__fit_scale_and_dimension(
                dimension_instance=self.dimension,
                from_base_scale_conversions=self.from_base_scale_conversions,
                rescale_value=1 / other,
                value=self.rescale_value,
            )
            return Scale(
                dimension=self.dimension,
                from_base_scale_conversions=new_from_base_scale_conversions,
                rescale_value=new_value,
            )
        if isinstance(other, Scale):
            new_dimension = self.dimension - other.dimension
            new_from_base_scale_conversions_list = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
            rescale_factor = 1
            for i in BaseDimension:
                xxx = (
                    self.from_base_scale_conversions[i]
                    / other.from_base_scale_conversions[i]
                )
                if new_dimension.get(i) == 0 and (
                    self.dimension.get(i) != 0 or other.dimension.get(i) != 0
                ):
                    rescale_factor *= xxx
                    new_from_base_scale_conversions_list[i] = 1
                else:
                    new_from_base_scale_conversions_list[i] = xxx
            new_value, new_from_base_scale_conversions = self.__fit_scale_and_dimension(
                dimension_instance=new_dimension,
                from_base_scale_conversions=tuple(new_from_base_scale_conversions_list),
                rescale_value=self.rescale_value,
                value=rescale_factor,
            )
            return Scale(
                dimension=new_dimension,
                from_base_scale_conversions=new_from_base_scale_conversions,
                rescale_value=new_value,
            )
        raise InvalidOperationError(
            "division on Scale",
            type(other),
            (Scale, int, float),
        )

    def __rtruediv__(self, other):
        # Use Rust backend when enabled (disabled by default for single ops)
        if _USE_RUST_FOR_OPS and isinstance(other, (int, float)):
            rust_result = _scale_to_rust(self).rdivide_scalar(float(other))
            return _rust_to_scale(rust_result)

        # Fallback to pure Python implementation
        if isinstance(other, (int, float)):
            new_dimension = self.dimension * -1
            new_rescale_value = 1 / self.rescale_value
            new_from_base_scale_conversions_list = [
                1 / self.from_base_scale_conversions[i] for i in BaseDimension
            ]
            new_value, new_from_base_scale_conversions = self.__fit_scale_and_dimension(
                dimension_instance=new_dimension,
                from_base_scale_conversions=tuple(new_from_base_scale_conversions_list),
                rescale_value=new_rescale_value,
                value=other,
            )
            return Scale(
                dimension=new_dimension,
                from_base_scale_conversions=new_from_base_scale_conversions,
                rescale_value=new_value,
            )
        raise InvalidOperationError(
            "reverse division on Scale",
            type(other),
            (Scale, int, float),
        )

    def __pow__(self, power, modulo=None):
        # Use Rust backend when enabled (disabled by default for single ops)
        if _USE_RUST_FOR_OPS and isinstance(power, (int, float)):
            rust_result = _scale_to_rust(self).power(float(power))
            return _rust_to_scale(rust_result)

        # Fallback to pure Python implementation
        if isinstance(power, (int, float)):
            new_dimension = self.dimension * power
            new_from_base_scale_conversions = tuple(
                i**power for i in self.from_base_scale_conversions
            )
            new_rescale_value = self.rescale_value**power
            return Scale(
                dimension=new_dimension,
                from_base_scale_conversions=new_from_base_scale_conversions,
                rescale_value=new_rescale_value,
            )
        raise InvalidPowerError("Scale", power)
