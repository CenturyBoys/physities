"""Core benchmarks for physities performance tracking.

Compares:
1. Plain Python vs Physities (overhead of unit safety)
2. Single operations vs Batch operations (UnitArray speedup)

Values are in iterations/second (higher = faster).
"""

import numpy as np
import pytest
from physities.src.unit import Meter, Second, Kilometer, Hour, UnitArray


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
# PHYSITIES: Single operations with unit safety
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
    benchmark.name = "Physities: convert"
    m = Meter(1000)
    benchmark(lambda: m.convert(Kilometer))


# =============================================================================
# BATCH: NumPy baseline (raw arrays, no units)
# =============================================================================

def test_numpy_add_1000(benchmark):
    """NumPy: add two arrays of 1000 elements."""
    benchmark.name = "NumPy: arr + arr (1000)"
    a = np.random.rand(1000)
    b = np.random.rand(1000)
    benchmark(lambda: a + b)


def test_numpy_multiply_1000(benchmark):
    """NumPy: multiply two arrays of 1000 elements."""
    benchmark.name = "NumPy: arr * arr (1000)"
    a = np.random.rand(1000)
    b = np.random.rand(1000)
    benchmark(lambda: a * b)


def test_numpy_sum_1000(benchmark):
    """NumPy: sum 1000 elements."""
    benchmark.name = "NumPy: sum(arr) (1000)"
    a = np.random.rand(1000)
    benchmark(lambda: np.sum(a))


# =============================================================================
# BATCH: UnitArray operations (units + arrays)
# =============================================================================

def test_unitarray_add_1000(benchmark):
    """UnitArray: add scalar to 1000 elements."""
    benchmark.name = "UnitArray: arr + m (1000)"
    arr = UnitArray(Meter, np.random.rand(1000) * 100)
    m = Meter(10)
    benchmark(lambda: arr + m)


def test_unitarray_multiply_1000(benchmark):
    """UnitArray: multiply 1000 elements by scalar."""
    benchmark.name = "UnitArray: arr * 2 (1000)"
    arr = UnitArray(Meter, np.random.rand(1000) * 100)
    benchmark(lambda: arr * 2)


def test_unitarray_sum_1000(benchmark):
    """UnitArray: sum 1000 elements."""
    benchmark.name = "UnitArray: sum(arr) (1000)"
    arr = UnitArray(Meter, np.random.rand(1000) * 100)
    benchmark(lambda: arr.sum())


def test_unitarray_convert_1000(benchmark):
    """UnitArray: convert 1000 elements."""
    benchmark.name = "UnitArray: convert (1000)"
    arr = UnitArray(Meter, np.random.rand(1000) * 1000)
    benchmark(lambda: arr.convert(Kilometer))


# =============================================================================
# COMPARISON: Loop vs Batch
# =============================================================================

def test_loop_add_100(benchmark):
    """Loop: add 100 units individually."""
    benchmark.name = "Loop: 100x (m + m)"
    values = [Meter(i) for i in range(100)]
    m = Meter(10)
    def loop_add():
        return [v + m for v in values]
    benchmark(loop_add)


def test_batch_add_100(benchmark):
    """Batch: add to 100 elements at once."""
    benchmark.name = "Batch: arr + m (100)"
    arr = UnitArray(Meter, list(range(100)))
    m = Meter(10)
    benchmark(lambda: arr + m)
