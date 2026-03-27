"""Core benchmarks for physities performance tracking.

Compares physities operations against plain Python equivalents
to show the overhead of type-safe unit handling.

Values are in iterations/second (higher = faster).
"""

import pytest
from physities.src.unit import Meter, Second, Kilometer, Hour


# =============================================================================
# BASELINE: Plain Python (what you'd write without physities)
# =============================================================================

class TestBaseline:
    """Plain Python baseline - no unit safety."""

    def test_python_float_add(self, benchmark):
        """Baseline: add two floats."""
        a, b = 100.0, 200.0
        benchmark(lambda: a + b)

    def test_python_float_multiply(self, benchmark):
        """Baseline: multiply two floats."""
        a, b = 10.0, 5.0
        benchmark(lambda: a * b)

    def test_python_float_divide(self, benchmark):
        """Baseline: divide two floats."""
        a, b = 100.0, 10.0
        benchmark(lambda: a / b)

    def test_python_convert(self, benchmark):
        """Baseline: manual conversion (m to km)."""
        value = 1000.0
        benchmark(lambda: value / 1000)


# =============================================================================
# PHYSITIES: Same operations with unit safety
# =============================================================================

class TestPhysities:
    """Physities operations - with unit safety."""

    def test_unit_add(self, benchmark):
        """Add two Meter values."""
        m1, m2 = Meter(100), Meter(200)
        benchmark(lambda: m1 + m2)

    def test_unit_multiply(self, benchmark):
        """Multiply Meter * Second."""
        m, s = Meter(10), Second(5)
        benchmark(lambda: m * s)

    def test_unit_divide(self, benchmark):
        """Divide Meter / Second (velocity)."""
        m, s = Meter(100), Second(10)
        benchmark(lambda: m / s)

    def test_unit_convert(self, benchmark):
        """Convert Meter to Kilometer."""
        m = Meter(1000)
        benchmark(lambda: m.convert(Kilometer))


# =============================================================================
# UNIT CREATION: Cost of creating unit instances
# =============================================================================

class TestCreation:
    """Unit creation overhead."""

    def test_create_simple(self, benchmark):
        """Create Meter(100)."""
        benchmark(lambda: Meter(100))

    def test_create_composite_type(self, benchmark):
        """Create Meter/Second type."""
        benchmark(lambda: Meter / Second)
