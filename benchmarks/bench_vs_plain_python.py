"""Benchmarks comparing physities vs plain Python operations."""

import pytest
from dataclasses import dataclass

from physities.src.unit import Meter, Second, Kilometer, Hour


# Plain Python implementations for comparison
@dataclass
class PlainQuantity:
    """Simple quantity without unit checking."""
    value: float
    unit: str

    def __add__(self, other):
        return PlainQuantity(self.value + other.value, self.unit)

    def __sub__(self, other):
        return PlainQuantity(self.value - other.value, self.unit)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return PlainQuantity(self.value * other, self.unit)
        return PlainQuantity(self.value * other.value, f"{self.unit}*{other.unit}")

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return PlainQuantity(self.value / other, self.unit)
        return PlainQuantity(self.value / other.value, f"{self.unit}/{other.unit}")

    def __pow__(self, exp):
        return PlainQuantity(self.value ** exp, f"{self.unit}^{exp}")


def plain_convert(value: float, factor: float) -> float:
    """Plain Python conversion."""
    return value * factor


@pytest.mark.benchmark(group="vs-plain-python")
class TestVsPlainPythonBenchmarks:
    """Compare physities performance vs plain Python."""

    def test_plain_python_addition(self, benchmark):
        """Benchmark plain Python addition."""
        q1 = PlainQuantity(100, "m")
        q2 = PlainQuantity(200, "m")
        benchmark(lambda: q1 + q2)

    def test_physities_addition(self, benchmark):
        """Benchmark physities addition."""
        m1 = Meter(100)
        m2 = Meter(200)
        benchmark(lambda: m1 + m2)

    def test_plain_python_multiplication(self, benchmark):
        """Benchmark plain Python multiplication."""
        q1 = PlainQuantity(10, "m")
        q2 = PlainQuantity(5, "s")
        benchmark(lambda: q1 * q2)

    def test_physities_multiplication(self, benchmark):
        """Benchmark physities multiplication."""
        m = Meter(10)
        s = Second(5)
        benchmark(lambda: m * s)

    def test_plain_python_conversion(self, benchmark):
        """Benchmark plain Python conversion."""
        value = 1000.0
        factor = 0.001  # m to km
        benchmark(lambda: plain_convert(value, factor))

    def test_physities_conversion(self, benchmark):
        """Benchmark physities conversion."""
        m = Meter(1000)
        benchmark(lambda: m.convert(Kilometer))

    def test_plain_python_power(self, benchmark):
        """Benchmark plain Python power."""
        q = PlainQuantity(10, "m")
        benchmark(lambda: q ** 2)

    def test_physities_power(self, benchmark):
        """Benchmark physities power."""
        m = Meter(10)
        benchmark(lambda: m ** 2)

    def test_plain_python_chain(self, benchmark):
        """Benchmark plain Python operation chain."""
        def chain():
            q1 = PlainQuantity(100, "m")
            q2 = PlainQuantity(10, "s")
            velocity = q1 / q2
            return velocity * 2

        benchmark(chain)

    def test_physities_chain(self, benchmark):
        """Benchmark physities operation chain."""
        def chain():
            m = Meter(100)
            s = Second(10)
            velocity = m / s
            return velocity * 2

        benchmark(chain)


@pytest.mark.benchmark(group="creation-overhead")
class TestCreationOverheadBenchmarks:
    """Benchmark object creation overhead."""

    def test_plain_dataclass_creation(self, benchmark):
        """Benchmark plain dataclass creation."""
        benchmark(lambda: PlainQuantity(100.0, "m"))

    def test_physities_unit_creation(self, benchmark):
        """Benchmark physities unit creation."""
        benchmark(lambda: Meter(100))

    def test_plain_float_operation(self, benchmark):
        """Benchmark plain float operation."""
        a, b = 100.0, 200.0
        benchmark(lambda: a + b)

    def test_physities_unit_operation(self, benchmark):
        """Benchmark physities unit operation."""
        m1 = Meter(100)
        m2 = Meter(200)
        benchmark(lambda: m1 + m2)
