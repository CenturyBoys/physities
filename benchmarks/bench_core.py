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

def test_baseline_add(benchmark):
    """Baseline: add two floats."""
    benchmark.name = "Python: a + b"
    a, b = 100.0, 200.0
    benchmark(lambda: a + b)


def test_baseline_multiply(benchmark):
    """Baseline: multiply two floats."""
    benchmark.name = "Python: a * b"
    a, b = 10.0, 5.0
    benchmark(lambda: a * b)


def test_baseline_divide(benchmark):
    """Baseline: divide two floats."""
    benchmark.name = "Python: a / b"
    a, b = 100.0, 10.0
    benchmark(lambda: a / b)


def test_baseline_convert(benchmark):
    """Baseline: manual conversion."""
    benchmark.name = "Python: v / 1000"
    value = 1000.0
    benchmark(lambda: value / 1000)


# =============================================================================
# PHYSITIES: Same operations with unit safety
# =============================================================================

def test_physities_add(benchmark):
    """Add two Meter values."""
    benchmark.name = "Physities: m1 + m2"
    m1, m2 = Meter(100), Meter(200)
    benchmark(lambda: m1 + m2)


def test_physities_multiply(benchmark):
    """Multiply Meter * Second."""
    benchmark.name = "Physities: m * s"
    m, s = Meter(10), Second(5)
    benchmark(lambda: m * s)


def test_physities_divide(benchmark):
    """Divide Meter / Second."""
    benchmark.name = "Physities: m / s"
    m, s = Meter(100), Second(10)
    benchmark(lambda: m / s)


def test_physities_convert(benchmark):
    """Convert Meter to Kilometer."""
    benchmark.name = "Physities: m.convert(km)"
    m = Meter(1000)
    benchmark(lambda: m.convert(Kilometer))


# =============================================================================
# CREATION: Cost of creating units
# =============================================================================

def test_create_unit(benchmark):
    """Create a unit instance."""
    benchmark.name = "Create: Meter(100)"
    benchmark(lambda: Meter(100))


def test_create_type(benchmark):
    """Create a composite unit type."""
    benchmark.name = "Create: Meter / Second"
    benchmark(lambda: Meter / Second)
