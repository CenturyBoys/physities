"""Core benchmarks for physities performance tracking.

This file contains the key benchmarks that are tracked over time.
Focused on the most important operations users care about.
"""

import pytest
from physities.src.unit import Meter, Second, Kilometer, Hour, Kilogram


class TestCoreBenchmarks:
    """Core performance benchmarks."""

    def test_create_unit(self, benchmark):
        """Create a simple unit instance."""
        benchmark(lambda: Meter(100))

    def test_create_composite_type(self, benchmark):
        """Create a composite unit type (m/s)."""
        benchmark(lambda: Meter / Second)

    def test_add_units(self, benchmark):
        """Add two units of same dimension."""
        m1, m2 = Meter(100), Meter(200)
        benchmark(lambda: m1 + m2)

    def test_multiply_units(self, benchmark):
        """Multiply two units (creates new dimension)."""
        m, s = Meter(10), Second(5)
        benchmark(lambda: m * s)

    def test_divide_units(self, benchmark):
        """Divide two units (creates velocity)."""
        m, s = Meter(100), Second(10)
        benchmark(lambda: m / s)

    def test_convert_simple(self, benchmark):
        """Convert meters to kilometers."""
        m = Meter(1000)
        benchmark(lambda: m.convert(Kilometer))

    def test_convert_composite(self, benchmark):
        """Convert m/s to km/h."""
        Ms = Meter / Second
        Kh = Kilometer / Hour
        speed = Ms(10)
        benchmark(lambda: speed.convert(Kh))

    def test_power(self, benchmark):
        """Raise unit to power (m^2)."""
        m = Meter(10)
        benchmark(lambda: m ** 2)
