"""Property-based tests for Scale class."""

import pytest
from hypothesis import given, strategies as st, assume

from physities.src.dimension import Dimension
from physities.src.scale import Scale


# Strategy for conversion factors (must be positive)
positive_float = st.floats(min_value=0.001, max_value=1000, allow_nan=False, allow_infinity=False)

# Strategy for rescale values
rescale_value = st.floats(min_value=0.001, max_value=1000, allow_nan=False, allow_infinity=False)

# Strategy for conversion factor tuples
conversion_tuple = st.tuples(
    positive_float,
    positive_float,
    positive_float,
    positive_float,
    positive_float,
    positive_float,
    positive_float,
)


@pytest.mark.property
class TestScaleProperties:
    """Property-based tests for Scale class."""

    @given(conversions=conversion_tuple, rescale=rescale_value)
    def test_scale_creation_preserves_values(self, conversions, rescale):
        """Test that scale creation preserves conversion factors."""
        dim = Dimension.new_dimensionless()
        scale = Scale.new(
            dimension=dim,
            from_base_scale_conversions=conversions,
            rescale_value=rescale,
        )

        assert scale.from_base_scale_conversions == conversions
        assert scale.rescale_value == rescale

    @given(scalar=positive_float)
    def test_multiplication_by_scalar_is_reversible(self, scalar):
        """Test that multiplying and dividing by scalar returns original."""
        scale = Scale.new(dimension=Dimension.new_length())

        result = (scale * scalar) / scalar

        # Check conversion factors are approximately equal
        assert abs(result.conversion_factor - scale.conversion_factor) < 1e-10

    @given(scalar=positive_float)
    def test_division_by_scalar_is_reversible(self, scalar):
        """Test that dividing and multiplying by scalar returns original."""
        scale = Scale.new(dimension=Dimension.new_length())

        result = (scale / scalar) * scalar

        assert abs(result.conversion_factor - scale.conversion_factor) < 1e-10

    @given(exp=st.floats(min_value=-3, max_value=3, allow_nan=False, allow_infinity=False))
    def test_power_identity(self, exp):
        """Test power of 1 returns equivalent scale."""
        scale = Scale.new(dimension=Dimension.new_length())

        result = scale ** 1

        assert result.conversion_factor == scale.conversion_factor

    @given(exp=st.floats(min_value=0.5, max_value=2, allow_nan=False, allow_infinity=False))
    def test_power_and_root_are_inverse(self, exp):
        """Test that power and root are inverse operations."""
        assume(exp != 0)
        scale = Scale.new(
            dimension=Dimension.new_length(),
            from_base_scale_conversions=(100, 1, 1, 1, 1, 1, 1),
        )

        result = (scale ** exp) ** (1 / exp)

        assert abs(result.conversion_factor - scale.conversion_factor) < 1e-8

    def test_multiplication_associative(self):
        """Test that scale multiplication is associative."""
        scale1 = Scale.new(dimension=Dimension.new_length())
        scale2 = Scale.new(dimension=Dimension.new_time())
        scale3 = Scale.new(dimension=Dimension.new_mass())

        result1 = (scale1 * scale2) * scale3
        result2 = scale1 * (scale2 * scale3)

        assert result1.conversion_factor == result2.conversion_factor

    def test_inverse_multiplication_gives_dimensionless(self):
        """Test that scale * inverse equals dimensionless."""
        scale = Scale.new(
            dimension=Dimension.new_length(),
            from_base_scale_conversions=(1000, 1, 1, 1, 1, 1, 1),
        )

        result = scale * (1 / scale)

        assert result.is_dimensionless

    @given(conversions=conversion_tuple)
    def test_conversion_factor_is_product(self, conversions):
        """Test that conversion_factor is product of components."""
        from math import prod

        dim = Dimension.new_dimensionless()
        scale = Scale.new(
            dimension=dim,
            from_base_scale_conversions=conversions,
            rescale_value=1.0,
        )

        expected = prod(conversions)
        assert abs(scale.conversion_factor - expected) < 1e-10

    @given(scalar1=positive_float, scalar2=positive_float)
    def test_scalar_multiplication_commutative(self, scalar1, scalar2):
        """Test that scalar multiplication order doesn't matter."""
        scale = Scale.new(dimension=Dimension.new_length())

        result1 = (scale * scalar1) * scalar2
        result2 = (scale * scalar2) * scalar1

        assert abs(result1.conversion_factor - result2.conversion_factor) < 1e-10

    def test_dimensionless_is_identity_for_multiplication(self):
        """Test that multiplying by dimensionless scale is identity."""
        scale = Scale.new(
            dimension=Dimension.new_length(),
            from_base_scale_conversions=(1000, 1, 1, 1, 1, 1, 1),
        )
        dimensionless = Scale.new()

        result = scale * dimensionless

        assert result.conversion_factor == scale.conversion_factor
        assert result.dimension == scale.dimension
