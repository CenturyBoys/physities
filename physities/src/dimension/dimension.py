from typing import Self

from physities.src.dimension.base_dimensions import BaseDimension

from physities._physities_core import PhysicalDimension as _RustDimension

SYMBOLS = {
    BaseDimension.LENGTH: "L",
    BaseDimension.MASS: "m",
    BaseDimension.TIME: "t",
    BaseDimension.TEMPERATURE: "T",
    BaseDimension.AMOUNT: "N",
    BaseDimension.ELECTRIC_CURRENT: "I",
    BaseDimension.LUMINOUS_INTENSITY: "I\u1d65",
}

NUMBER_STR_TO_POWER_STR = {
    "0": "\u2070", "1": "\u00b9", "2": "\u00b2", "3": "\u00b3", "4": "\u2074",
    "5": "\u2075", "6": "\u2076", "7": "\u2077", "8": "\u2078", "9": "\u2079",
    ".": "\u02d1",
}


class Dimension:
    """Represents physical dimensions using the 7 SI base dimensions.

    Thin wrapper around Rust PhysicalDimension.
    """

    __slots__ = ('_rust',)

    def __init__(self, *, dimensions_tuple: tuple[float, float, float, float, float, float, float]):
        self._rust = _RustDimension(dimensions_tuple)

    @classmethod
    def _from_rust(cls, rust_dim: _RustDimension) -> Self:
        instance = object.__new__(cls)
        instance._rust = rust_dim
        return instance

    @property
    def dimensions_tuple(self) -> tuple[float, float, float, float, float, float, float]:
        return tuple(self._rust.dimensions_tuple)

    @property
    def length(self) -> float:
        return self._rust.length

    @property
    def mass(self) -> float:
        return self._rust.mass

    @property
    def temperature(self) -> float:
        return self._rust.temperature

    @property
    def time(self) -> float:
        return self._rust.time

    @property
    def amount(self) -> float:
        return self._rust.amount

    @property
    def electric_current(self) -> float:
        return self._rust.electric_current

    @property
    def luminous_intensity(self) -> float:
        return self._rust.luminous_intensity

    @classmethod
    def new_time(cls, power: float = None) -> Self:
        return cls._from_rust(_RustDimension.new_time(power))

    @classmethod
    def new_length(cls, power: float = None) -> Self:
        return cls._from_rust(_RustDimension.new_length(power))

    @classmethod
    def new_temperature(cls, power: float = None) -> Self:
        return cls._from_rust(_RustDimension.new_temperature(power))

    @classmethod
    def new_mass(cls, power: float = None) -> Self:
        return cls._from_rust(_RustDimension.new_mass(power))

    @classmethod
    def new_amount(cls, power: float = None) -> Self:
        return cls._from_rust(_RustDimension.new_amount(power))

    @classmethod
    def new_electric_current(cls, power: float = None) -> Self:
        return cls._from_rust(_RustDimension.new_electric_current(power))

    @classmethod
    def new_luminous_intensity(cls, power: float = None) -> Self:
        return cls._from_rust(_RustDimension.new_luminous_intensity(power))

    @classmethod
    def new_dimensionless(cls) -> Self:
        return cls._from_rust(_RustDimension.new_dimensionless())

    @classmethod
    def new_instance(cls, dimensions_tuple: tuple) -> Self:
        return cls(dimensions_tuple=dimensions_tuple)

    def get_dimensions(self) -> list[BaseDimension]:
        return [BaseDimension(i) for i in self._rust.get_dimensions()]

    def get(self, index: BaseDimension) -> float:
        return self._rust.get(int(index))

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

    def __add__(self, other):
        return Dimension._from_rust(self._rust + other._rust)

    def __radd__(self, other):
        return Dimension._from_rust(other._rust + self._rust)

    def __sub__(self, other):
        return Dimension._from_rust(self._rust - other._rust)

    def __rsub__(self, other):
        return Dimension._from_rust(other._rust - self._rust)

    def __mul__(self, other):
        return Dimension._from_rust(self._rust * float(other))

    def __rmul__(self, other):
        return Dimension._from_rust(float(other) * self._rust)

    def __truediv__(self, other):
        return Dimension._from_rust(self._rust / float(other))

    def __rtruediv__(self, other):
        return Dimension._from_rust(float(other) / self._rust)

    def __eq__(self, other):
        try:
            return self._rust == other._rust
        except AttributeError:
            return False

    def __hash__(self):
        return hash(self._rust)

    def __pow__(self, power, modulo=None):
        raise TypeError("unsupported operand type(s) for ** or pow()")

    def __rpow__(self, power):
        raise TypeError("unsupported operand type(s) for ** or pow()")

    def show_dimension(self) -> str:
        return self._rust.show_dimension()

    def __repr__(self):
        return f"Dimension(dimensions_tuple={self.dimensions_tuple})"

    def __str__(self):
        return self.show_dimension()
