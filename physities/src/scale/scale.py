import json
from typing import Self

from physities.src.dimension import Dimension

from physities._physities_core import PhysicalScale as _RustScale


class Scale:
    """Represents a unit scale with dimension and conversion factors.

    Thin wrapper around Rust PhysicalScale.
    """

    __slots__ = ('_rust',)

    def __init__(
        self,
        *,
        dimension: Dimension,
        from_base_scale_conversions: tuple,
        rescale_value: float | int,
    ):
        self._rust = _RustScale.from_dimension(
            dimension._rust,
            from_base_scale_conversions,
            float(rescale_value),
        )

    @classmethod
    def _from_rust(cls, rust_scale: _RustScale) -> Self:
        instance = object.__new__(cls)
        instance._rust = rust_scale
        return instance

    @property
    def dimension(self) -> Dimension:
        return Dimension._from_rust(self._rust.dimension)

    @property
    def from_base_scale_conversions(self) -> tuple[float, float, float, float, float, float, float]:
        return tuple(self._rust.from_base_scale_conversions())

    @property
    def rescale_value(self) -> float:
        return self._rust.rescale_value

    @classmethod
    def new(
        cls,
        dimension: Dimension = None,
        from_base_scale_conversions: tuple = None,
        rescale_value: float = None,
    ) -> Self:
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
        return self._rust.is_dimensionless

    @property
    def conversion_factor(self) -> float:
        return self._rust.conversion_factor

    def to_rust(self) -> _RustScale:
        return self._rust

    @classmethod
    def from_rust(cls, rust_scale: _RustScale) -> Self:
        return cls._from_rust(rust_scale)

    @staticmethod
    def has_rust_backend() -> bool:
        return True

    @staticmethod
    def is_rust_enabled() -> bool:
        return True

    @staticmethod
    def enable_rust():
        pass

    @staticmethod
    def disable_rust():
        pass

    def dict(self) -> dict:
        return {
            'dimension': self.dimension.dimensions_tuple,
            'from_base_scale_conversions': self.from_base_scale_conversions,
            'rescale_value': self.rescale_value,
        }

    def to_json(self) -> str:
        return json.dumps({
            'dimension': list(self.dimension.dimensions_tuple),
            'from_base_scale_conversions': list(self.from_base_scale_conversions),
            'rescale_value': self.rescale_value,
        })

    @classmethod
    def from_dict(cls, data: dict) -> Self:
        dimension = Dimension.new_instance(tuple(data['dimension']))
        return cls(
            dimension=dimension,
            from_base_scale_conversions=tuple(data['from_base_scale_conversions']),
            rescale_value=data['rescale_value'],
        )

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        return cls.from_dict(json.loads(json_str))

    def __eq__(self, other):
        try:
            return self._rust.equals(other._rust)
        except AttributeError:
            return False

    def __hash__(self):
        return hash(self._rust)

    def __mul__(self, other):
        if isinstance(other, Scale):
            return Scale._from_rust(self._rust.multiply(other._rust))
        return Scale._from_rust(self._rust.multiply_scalar(float(other)))

    def __rmul__(self, other):
        return Scale._from_rust(self._rust.multiply_scalar(float(other)))

    def __truediv__(self, other):
        if isinstance(other, Scale):
            return Scale._from_rust(self._rust.divide(other._rust))
        return Scale._from_rust(self._rust.divide_scalar(float(other)))

    def __rtruediv__(self, other):
        return Scale._from_rust(self._rust.rdivide_scalar(float(other)))

    def __pow__(self, power, modulo=None):
        return Scale._from_rust(self._rust.power(float(power)))

    def __repr__(self):
        return f"Scale(dimension={self.dimension!r}, factor={self.conversion_factor})"

    def __str__(self):
        return f"Scale({self.dimension.show_dimension()}, factor={self.conversion_factor})"
