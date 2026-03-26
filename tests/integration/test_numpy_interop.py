"""Integration tests for NumPy interoperability."""

import pytest

from physities.src.unit import Meter, Second, Kilogram


@pytest.mark.integration
class TestNumpyInterop:
    """Test NumPy-like operations with physities units."""

    def test_scalar_multiplication_with_large_values(self):
        """Test handling of large numerical values."""
        # Speed of light in m/s (approximately)
        c = (Meter / Second)(299792458)

        # E = mc^2 for 1 kg
        m = Kilogram(1)
        e = m * c * c

        # Should handle large values
        assert e.value > 8e16

    def test_unit_operations_with_small_values(self):
        """Test handling of small numerical values."""
        # Planck length approximately
        length = Meter(1.616e-35)

        # Square it
        area = length * length
        assert area.value > 0
        assert area.value < 1e-69

    def test_mixed_precision_operations(self):
        """Test operations with mixed precision values."""
        Ms = Meter / Second

        # Integer and float mixing
        v1 = Ms(10)
        v2 = Ms(3.5)

        result = v1 + v2
        assert result.value == 13.5

    def test_zero_handling(self):
        """Test handling of zero values."""
        m = Meter(0)

        # Multiplication with zero
        result = m * 100
        assert result.value == 0

        # Addition with zero
        result2 = Meter(100) + m
        assert result2.value == 100

    def test_negative_values(self):
        """Test handling of negative values."""
        m = Meter(-10)

        # Absolute value operations
        squared = m * m
        assert squared.value == 100  # Negative squared is positive

        # Negative times positive
        result = m * Meter(5)
        assert result.value == -50

    def test_conversion_chain_precision(self):
        """Test precision in long conversion chains."""
        # Multiple conversions shouldn't lose precision
        Ms = Meter / Second
        Kh = (Meter * 1000) / (Second * 3600)

        speed = Ms(10)

        # Convert back and forth multiple times
        for _ in range(10):
            speed = speed.convert(Kh)
            speed = speed.convert(Ms)

        # Should still be close to original
        assert abs(speed.value - 10.0) < 1e-10
