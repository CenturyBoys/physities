"""Benchmarks for unit conversions."""

import pytest

from physities.src.unit import Meter, Second, Kilometer, Hour


@pytest.mark.benchmark(group="conversions")
class TestConversionBenchmarks:
    """Benchmark unit conversion operations."""

    def test_simple_conversion(self, benchmark):
        """Benchmark simple unit conversion (m to km)."""
        m = Meter(1000)
        benchmark(lambda: m.convert(Kilometer))

    def test_composite_conversion(self, benchmark):
        """Benchmark composite unit conversion (m/s to km/h)."""
        Ms = Meter / Second
        Kh = Kilometer / Hour

        speed = Ms(10)
        benchmark(lambda: speed.convert(Kh))

    def test_to_si_conversion(self, benchmark):
        """Benchmark conversion to SI units."""
        km = Kilometer(100)
        benchmark(lambda: km.to_si())

    def test_repeated_conversion(self, benchmark):
        """Benchmark repeated conversions back and forth."""
        Ms = Meter / Second
        Kh = Kilometer / Hour

        def convert_chain():
            speed = Ms(10)
            speed = speed.convert(Kh)
            speed = speed.convert(Ms)
            return speed

        benchmark(convert_chain)


@pytest.mark.benchmark(group="unit-creation")
class TestUnitCreationBenchmarks:
    """Benchmark unit creation operations."""

    def test_simple_unit_creation(self, benchmark):
        """Benchmark creating a simple unit."""
        benchmark(lambda: Meter(100))

    def test_composite_unit_type_creation(self, benchmark):
        """Benchmark creating a composite unit type."""
        benchmark(lambda: Meter / Second)

    def test_composite_unit_instance_creation(self, benchmark):
        """Benchmark creating a composite unit instance."""
        Ms = Meter / Second
        benchmark(lambda: Ms(100))

    def test_complex_unit_type_creation(self, benchmark):
        """Benchmark creating a complex unit type (Newton)."""
        from physities.src.unit import Kilogram

        benchmark(lambda: Kilogram * Meter / (Second ** 2))


@pytest.mark.benchmark(group="arithmetic")
class TestArithmeticBenchmarks:
    """Benchmark arithmetic operations."""

    def test_unit_addition(self, benchmark):
        """Benchmark unit addition."""
        m1 = Meter(100)
        m2 = Meter(200)
        benchmark(lambda: m1 + m2)

    def test_unit_subtraction(self, benchmark):
        """Benchmark unit subtraction."""
        m1 = Meter(200)
        m2 = Meter(100)
        benchmark(lambda: m1 - m2)

    def test_unit_multiplication(self, benchmark):
        """Benchmark unit multiplication."""
        m = Meter(10)
        s = Second(5)
        benchmark(lambda: m * s)

    def test_unit_division(self, benchmark):
        """Benchmark unit division."""
        m = Meter(100)
        s = Second(10)
        benchmark(lambda: m / s)

    def test_scalar_multiplication(self, benchmark):
        """Benchmark scalar multiplication."""
        m = Meter(100)
        benchmark(lambda: m * 2)

    def test_unit_power(self, benchmark):
        """Benchmark unit power operation."""
        m = Meter(10)
        benchmark(lambda: m ** 2)
