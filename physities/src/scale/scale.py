import json
from math import prod
from typing import Self

from physities.src.dimension import Dimension
from physities.src.dimension.base_dimensions import BaseDimension
from physities.src.exceptions import InvalidOperationError, InvalidPowerError

# Import the Rust backend
from physities._physities_core import PhysicalScale as _RustScale


class Scale:
    """Represents a unit scale with dimension and conversion factors.

    A Scale combines a Dimension with conversion factors that define how to
    convert from this scale to SI base units. It supports arithmetic operations
    that properly combine scales when multiplying/dividing units.

    The total conversion factor is: rescale_value * product(from_base_scale_conversions)

    This class is a thin wrapper around the Rust PhysicalScale for high performance.

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

    __slots__ = ('_rust',)

    def __init__(
        self,
        *,
        dimension: Dimension,
        from_base_scale_conversions: tuple[
            float | int,
            float | int,
            float | int,
            float | int,
            float | int,
            float | int,
            float | int,
        ],
        rescale_value: float | int,
    ):
        """Create a new Scale.

        Args:
            dimension: The physical Dimension of this scale.
            from_base_scale_conversions: A 7-element tuple of conversion factors.
            rescale_value: An additional multiplicative factor.
        """
        self._rust = _RustScale.from_dimension(
            dimension._rust,
            from_base_scale_conversions,
            float(rescale_value),
        )

    @classmethod
    def _from_rust(cls, rust_scale: _RustScale) -> Self:
        """Create a Scale from a Rust PhysicalScale (internal use)."""
        instance = object.__new__(cls)
        instance._rust = rust_scale
        return instance

    @property
    def dimension(self) -> Dimension:
        """The physical Dimension of this scale."""
        return Dimension._from_rust(self._rust.dimension)

    @property
    def from_base_scale_conversions(self) -> tuple[float, float, float, float, float, float, float]:
        """The 7-element tuple of conversion factors."""
        return tuple(self._rust.from_base_scale_conversions())

    @property
    def rescale_value(self) -> float:
        """The additional multiplicative scaling factor."""
        return self._rust.rescale_value

    @classmethod
    def new(
        cls,
        dimension: Dimension = None,
        from_base_scale_conversions: tuple[
            float, float, float, float, float, float, float
        ] = None,
        rescale_value: float = None,
    ) -> Self:
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
        return self._rust.is_dimensionless

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
        return self._rust.conversion_factor

    def to_rust(self) -> _RustScale:
        """Get the underlying Rust PhysicalScale.

        Returns:
            The Rust PhysicalScale backing this Scale.
        """
        return self._rust

    @classmethod
    def from_rust(cls, rust_scale: _RustScale) -> Self:
        """Create a Scale from a Rust PhysicalScale.

        Args:
            rust_scale: The Rust PhysicalScale instance.

        Returns:
            A Python Scale wrapping the Rust scale.
        """
        return cls._from_rust(rust_scale)

    @staticmethod
    def has_rust_backend() -> bool:
        """Check if the Rust backend is available.

        Returns:
            True - Rust backend is always available in this version.
        """
        return True

    @staticmethod
    def is_rust_enabled() -> bool:
        """Check if Rust is enabled for Scale operations.

        Returns:
            True - Rust is always enabled in this version.
        """
        return True

    @staticmethod
    def enable_rust():
        """Enable Rust for Scale operations.

        No-op in this version - Rust is always enabled.
        """
        pass

    @staticmethod
    def disable_rust():
        """Disable Rust for Scale operations.

        No-op in this version - Rust is always enabled.
        """
        pass

    # ==================== Serialization ====================

    def dict(self) -> dict:
        """Serialize the Scale to a dictionary.

        Returns:
            A dictionary with 'dimension', 'from_base_scale_conversions', and 'rescale_value'.

        Example:
            >>> scale = Scale.new(dimension=Dimension.new_length())
            >>> scale.dict()
            {'dimension': (1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
             'from_base_scale_conversions': (1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0),
             'rescale_value': 1.0}
        """
        return {
            'dimension': self.dimension.dimensions_tuple,
            'from_base_scale_conversions': self.from_base_scale_conversions,
            'rescale_value': self.rescale_value,
        }

    def to_json(self) -> str:
        """Serialize the Scale to a JSON string.

        Returns:
            A JSON string representation of the Scale.

        Example:
            >>> scale = Scale.new(dimension=Dimension.new_length())
            >>> scale.to_json()
            '{"dimension": [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], ...}'
        """
        data = {
            'dimension': list(self.dimension.dimensions_tuple),
            'from_base_scale_conversions': list(self.from_base_scale_conversions),
            'rescale_value': self.rescale_value,
        }
        return json.dumps(data)

    @classmethod
    def from_dict(cls, data: dict) -> Self:
        """Create a Scale from a dictionary.

        Args:
            data: A dictionary with 'dimension', 'from_base_scale_conversions',
                  and 'rescale_value' keys.

        Returns:
            A new Scale instance.

        Example:
            >>> data = {'dimension': (1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
            ...         'from_base_scale_conversions': (1000, 1, 1, 1, 1, 1, 1),
            ...         'rescale_value': 1.0}
            >>> scale = Scale.from_dict(data)
        """
        dimension = Dimension.new_instance(tuple(data['dimension']))
        return cls(
            dimension=dimension,
            from_base_scale_conversions=tuple(data['from_base_scale_conversions']),
            rescale_value=data['rescale_value'],
        )

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create a Scale from a JSON string.

        Args:
            json_str: A JSON string representation of the Scale.

        Returns:
            A new Scale instance.

        Example:
            >>> json_str = '{"dimension": [1, 0, 0, 0, 0, 0, 0], ...}'
            >>> scale = Scale.from_json(json_str)
        """
        data = json.loads(json_str)
        return cls.from_dict(data)

    # ==================== Arithmetic Operations ====================

    def __eq__(self, other):
        if isinstance(other, Scale):
            return self._rust.equals(other._rust)
        return False

    def __hash__(self):
        return hash(self._rust)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            rust_result = self._rust.multiply_scalar(float(other))
            return Scale._from_rust(rust_result)
        if isinstance(other, Scale):
            rust_result = self._rust.multiply(other._rust)
            return Scale._from_rust(rust_result)
        raise InvalidOperationError(
            "multiplication on Scale",
            type(other),
            (Scale, int, float),
        )

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            rust_result = self._rust.divide_scalar(float(other))
            return Scale._from_rust(rust_result)
        if isinstance(other, Scale):
            rust_result = self._rust.divide(other._rust)
            return Scale._from_rust(rust_result)
        raise InvalidOperationError(
            "division on Scale",
            type(other),
            (Scale, int, float),
        )

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            rust_result = self._rust.rdivide_scalar(float(other))
            return Scale._from_rust(rust_result)
        raise InvalidOperationError(
            "reverse division on Scale",
            type(other),
            (Scale, int, float),
        )

    def __pow__(self, power, modulo=None):
        if isinstance(power, (int, float)):
            rust_result = self._rust.power(float(power))
            return Scale._from_rust(rust_result)
        raise InvalidPowerError("Scale", power)

    def __repr__(self):
        return f"Scale(dimension={self.dimension!r}, from_base_scale_conversions={self.from_base_scale_conversions}, rescale_value={self.rescale_value})"

    def __str__(self):
        return f"Scale({self.dimension.show_dimension()}, factor={self.conversion_factor})"
