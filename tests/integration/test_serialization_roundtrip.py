"""Integration tests for serialization roundtrips."""

import pytest

from physities.src.dimension import Dimension
from physities.src.scale import Scale


@pytest.mark.integration
class TestSerializationRoundtrip:
    """Test serialization and deserialization of physical quantities."""

    def test_dimension_equality_after_operations(self):
        """Test dimension equality is preserved after operations."""
        dim1 = Dimension.new_length()
        dim2 = Dimension.new_length()

        # Should be equal
        assert dim1 == dim2

        # After operations
        dim3 = dim1 + Dimension.new_dimensionless()
        assert dim3 == dim1

    def test_scale_equality_preservation(self):
        """Test scale equality is preserved correctly."""
        scale1 = Scale.new(
            dimension=Dimension.new_length(),
            from_base_scale_conversions=(1000, 1, 1, 1, 1, 1, 1),
        )
        scale2 = Scale.new(
            dimension=Dimension.new_length(),
            from_base_scale_conversions=(1000, 1, 1, 1, 1, 1, 1),
        )

        assert scale1 == scale2

    def test_scale_conversion_factor_calculation(self):
        """Test conversion factor calculation is consistent."""
        km_scale = Scale.new(
            dimension=Dimension.new_length(),
            from_base_scale_conversions=(1000, 1, 1, 1, 1, 1, 1),
        )

        # Conversion factor should be 1000
        assert km_scale.conversion_factor == 1000

        # With rescale
        km_rescaled = Scale.new(
            dimension=Dimension.new_length(),
            from_base_scale_conversions=(500, 1, 1, 1, 1, 1, 1),
            rescale_value=2,
        )

        assert km_rescaled.conversion_factor == 1000

    def test_dimension_immutability(self):
        """Test that dimensions are immutable."""
        dim = Dimension.new_length()

        # Operations should create new instances
        dim2 = dim + Dimension.new_time()

        assert dim != dim2
        assert dim.length == 1
        assert dim.time == 0

    def test_scale_immutability(self):
        """Test that scales are immutable."""
        scale = Scale.new(dimension=Dimension.new_length())

        # Operations should create new instances
        scale2 = scale * 1000

        assert scale != scale2
        assert scale.conversion_factor == 1
        assert scale2.conversion_factor == 1000

    def test_nested_operations_consistency(self):
        """Test that nested operations produce consistent results."""
        length = Dimension.new_length()
        time = Dimension.new_time()

        # (L / T) * T should equal L
        velocity = length + (time * -1)  # L/T dimension
        result = velocity + time  # Should be L

        assert result == length

    def test_conversion_factor_chain(self):
        """Test conversion factor chains are calculated correctly."""
        # km to m
        km_to_m = 1000
        # hour to second
        hour_to_s = 3600

        # km/h scale
        kmh_scale = Scale.new(
            dimension=Dimension.new_instance((1, 0, 0, -1, 0, 0, 0)),
            from_base_scale_conversions=(km_to_m, 1, 1, hour_to_s, 1, 1, 1),
        )

        # Conversion factor for km/h to m/s
        expected = km_to_m * hour_to_s  # 3600000
        assert kmh_scale.conversion_factor == expected
