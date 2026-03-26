"""Benchmarks comparing physities vs NumPy array operations."""

import pytest


# Check if numpy is available
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False


from physities.src.unit import Meter, Second


@pytest.mark.benchmark(group="vs-numpy")
@pytest.mark.skipif(not HAS_NUMPY, reason="NumPy not installed")
class TestVsNumpyBenchmarks:
    """Compare physities scalar operations vs NumPy array operations."""

    def test_numpy_scalar_add(self, benchmark):
        """Benchmark NumPy scalar addition."""
        a = np.float64(100)
        b = np.float64(200)
        benchmark(lambda: a + b)

    def test_physities_scalar_add(self, benchmark):
        """Benchmark physities scalar addition."""
        m1 = Meter(100)
        m2 = Meter(200)
        benchmark(lambda: m1 + m2)

    def test_numpy_scalar_mul(self, benchmark):
        """Benchmark NumPy scalar multiplication."""
        a = np.float64(100)
        b = np.float64(2)
        benchmark(lambda: a * b)

    def test_physities_scalar_mul(self, benchmark):
        """Benchmark physities scalar multiplication."""
        m = Meter(100)
        benchmark(lambda: m * 2)

    def test_numpy_scalar_power(self, benchmark):
        """Benchmark NumPy scalar power."""
        a = np.float64(10)
        benchmark(lambda: a ** 2)

    def test_physities_scalar_power(self, benchmark):
        """Benchmark physities scalar power."""
        m = Meter(10)
        benchmark(lambda: m ** 2)


@pytest.mark.benchmark(group="batch-operations")
@pytest.mark.skipif(not HAS_NUMPY, reason="NumPy not installed")
class TestBatchOperationsBenchmarks:
    """Benchmark batch operations (loop vs vectorized)."""

    def test_numpy_batch_add_100(self, benchmark):
        """Benchmark NumPy adding 100 values."""
        arr = np.ones(100) * 100

        def batch_add():
            return arr + arr

        benchmark(batch_add)

    def test_physities_batch_add_100(self, benchmark):
        """Benchmark physities adding 100 values (loop)."""
        values = [Meter(100) for _ in range(100)]

        def batch_add():
            result = values[0]
            for v in values[1:]:
                result = result + v
            return result

        benchmark(batch_add)

    def test_numpy_batch_mul_100(self, benchmark):
        """Benchmark NumPy multiplying 100 values by scalar."""
        arr = np.ones(100) * 100

        def batch_mul():
            return arr * 2

        benchmark(batch_mul)

    def test_physities_batch_mul_100(self, benchmark):
        """Benchmark physities multiplying 100 values by scalar (loop)."""
        values = [Meter(100) for _ in range(100)]

        def batch_mul():
            return [v * 2 for v in values]

        benchmark(batch_mul)

    def test_numpy_batch_conversion_100(self, benchmark):
        """Benchmark NumPy converting 100 values."""
        arr = np.ones(100) * 1000
        factor = 0.001

        def batch_convert():
            return arr * factor

        benchmark(batch_convert)

    def test_physities_batch_conversion_100(self, benchmark):
        """Benchmark physities converting 100 values."""
        from physities.src.unit import Kilometer

        values = [Meter(1000) for _ in range(100)]

        def batch_convert():
            return [v.convert(Kilometer) for v in values]

        benchmark(batch_convert)
