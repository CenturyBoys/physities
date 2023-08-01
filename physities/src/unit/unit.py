from physities.src.dimension import Dimension
from physities.src.scale.scale import Scale


class MetaUnit(type):
    scale: Scale

    def __mul__(self, other):
        new_scale = None
        if isinstance(other, (int, float)):
            new_scale = self.scale * other
        if isinstance(other, MetaUnit):
            new_scale = self.scale * other.scale
        if new_scale is None:
            raise TypeError(
                f"{self} only allows multiplication by {self}, {int}, and {float}"
            )
        return type(self)(f"Unit", (Unit,), {"scale": new_scale, "value": None})

    def __rmul__(self, other):
        try:
            to_return = MetaUnit.__mul__(self, other)
        except TypeError as e:
            raise e
        return to_return

    def __truediv__(self, other):
        new_scale = None
        if isinstance(other, (int, float)):
            new_scale = self.scale / other
        if isinstance(other, MetaUnit):
            new_scale = self.scale / other.scale
        if new_scale is None:
            raise TypeError(
                f"{self} only allows division by {self}, {int}, and {float}"
            )
        return type(self)(f"Unit", (Unit,), {"scale": new_scale, "value": None})

    def __rtruediv__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError(f"{self} can divide only {self}, {int} and {float}")
        new_scale = other / self.scale
        return type(f"Unit", (Unit,), {"scale": new_scale, "value": None})

    def __pow__(self, power, modulo=None):
        if not isinstance(power, (int, float)):
            raise TypeError(f"{self} can only be powered by {int} and {float}")
        new_scale = self.scale**power
        return type(f"Unit", (Unit,), {"scale": new_scale, "value": None})


class Unit(metaclass=MetaUnit):
    scale: Scale
    value: float

    def __init__(self, value):
        self.value = value

    def set_scale(self, scale: Scale):
        self.scale = scale
        return self

    def __mul__(self, other):
        value, scale = None, self.scale
        if isinstance(other, (int, float)):
            value = self.value * other
        if isinstance(other, type(self)):
            scale = scale * other.scale
            value = self.value * other.value
        if not value:
            raise TypeError
        new_instance = type(self)(value).set_scale(scale)
        return new_instance

    def __rmul__(self, other):
        return Unit.__mul__(self, other)

    def __truediv__(self, other):
        value, scale = None, self.scale
        if isinstance(other, (int, float)):
            value = self.value / other
        if isinstance(other, type(self)):
            scale = self.scale / other.scale
            value = self.value / other.value
        if not value:
            raise TypeError
        new_instance = type(self)(value).set_scale(scale)
        return new_instance

    def __rtruediv__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError
        new_value = other / self.value
        new_scale = 1 / self.scale
        new_instance = type(self)(new_value).set_scale(new_scale)
        return new_instance

    def __pow__(self, power, modulo=None):
        if not isinstance(power, (int, float)):
            raise TypeError
        new_value = self.value**2
        new_scale = self.scale**2
        new_instance = type(self)(new_value).set_scale(new_scale)
        return new_instance

    def to_base(self, *args):
        print(args)
