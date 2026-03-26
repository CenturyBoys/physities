"""Property-based tests for Unit class."""

import pytest
from hypothesis import given, strategies as st, assume

from physities.src.unit import Meter, Second, Kilogram, Unit
from physities.src.scale import Scale
from physities.src.dimension import Dimension


# Strategy for unit values
unit_value = st.floats(min_value=-1e6, max_value=1e6, allow_nan=False, allow_infinity=False)
positive_value = st.floats(min_value=0.001, max_value=1e6, allow_nan=False, allow_infinity=False)
scalar_value = st.floats(min_value=0.1, max_value=100, allow_nan=False, allow_infinity=False)


@pytest.mark.property
class TestUnitProperties:
    """Property-based tests for Unit class."""

    @given(value=unit_value)
    def test_unit_creation_preserves_value(self, value):
        """Test that unit creation preserves the value."""
        m = Meter(value)
        assert m.value == value

    @given(v1=unit_value, v2=unit_value)
    def test_addition_commutative(self, v1, v2):
        """Test that unit addition is commutative."""
        m1 = Meter(v1)
        m2 = Meter(v2)

        result1 = m1 + m2
        result2 = m2 + m1

        assert abs(result1.value - result2.value) < 1e-10

    @given(v1=unit_value, v2=unit_value, v3=unit_value)
    def test_addition_associative(self, v1, v2, v3):
        """Test that unit addition is associative."""
        m1 = Meter(v1)
        m2 = Meter(v2)
        m3 = Meter(v3)

        result1 = (m1 + m2) + m3
        result2 = m1 + (m2 + m3)

        assert abs(result1.value - result2.value) < 1e-10

    @given(value=unit_value)
    def test_addition_identity(self, value):
        """Test that adding zero is identity."""
        m = Meter(value)
        zero = Meter(0)

        result = m + zero
        assert result.value == value

    @given(value=unit_value)
    def test_subtraction_is_inverse_of_addition(self, value):
        """Test that subtracting is inverse of adding."""
        m1 = Meter(value)
        m2 = Meter(10)

        result = m1 + m2 - m2
        assert abs(result.value - value) < 1e-10

    @given(value=unit_value, scalar=scalar_value)
    def test_scalar_multiplication_reversible(self, value, scalar):
        """Test that scalar multiplication is reversible by division."""
        m = Meter(value)

        result = (m * scalar) / scalar
        assert abs(result.value - value) < 1e-10

    @given(value=positive_value, scalar=scalar_value)
    def test_scalar_division_reversible(self, value, scalar):
        """Test that scalar division is reversible by multiplication."""
        m = Meter(value)

        result = (m / scalar) * scalar
        assert abs(result.value - value) < 1e-10

    @given(v1=positive_value, v2=positive_value)
    def test_multiplication_commutative(self, v1, v2):
        """Test that unit multiplication is commutative."""
        m1 = Meter(v1)
        m2 = Second(v2)

        result1 = m1 * m2
        result2 = m2 * m1

        assert abs(result1.value - result2.value) < 1e-10

    @given(value=positive_value)
    def test_unit_times_inverse_is_dimensionless(self, value):
        """Test that unit times its inverse is dimensionless."""
        m = Meter(value)
        inv = 1 / m

        result = m * inv
        assert result.scale.is_dimensionless
        assert abs(result.value - 1.0) < 1e-10

    @given(value=positive_value, exp=st.floats(min_value=0.5, max_value=2, allow_nan=False, allow_infinity=False))
    def test_power_and_root_inverse(self, value, exp):
        """Test that power and root are inverse operations."""
        m = Meter(value)

        result = (m ** exp) ** (1 / exp)
        assert abs(result.value - value) < 1e-8

    @given(value=unit_value)
    def test_equality_reflexive(self, value):
        """Test that equality is reflexive."""
        m = Meter(value)
        assert m == m

    @given(value=unit_value)
    def test_equality_symmetric(self, value):
        """Test that equality is symmetric."""
        m1 = Meter(value)
        m2 = Meter(value)

        assert (m1 == m2) == (m2 == m1)

    @given(value=positive_value)
    def test_to_si_preserves_physical_quantity(self, value):
        """Test that to_si() preserves the physical quantity."""
        # Create a kilometer unit
        Kilometer = Meter * 1000
        km = Kilometer(value)

        # Convert to SI
        si = km.to_si()

        # The value should be 1000x larger
        assert abs(si.value - value * 1000) < 1e-10

    @given(value=positive_value)
    def test_convert_roundtrip(self, value):
        """Test that convert roundtrip returns original value."""
        Kilometer = Meter * 1000

        m = Meter(value)

        # Convert to km and back
        km = m.convert(Kilometer)
        back = km.convert(Meter)

        assert abs(back.value - value) < 1e-10

    @given(v1=unit_value, v2=unit_value, scalar=scalar_value)
    def test_distributive_property(self, v1, v2, scalar):
        """Test distributive property: scalar * (a + b) = scalar * a + scalar * b."""
        m1 = Meter(v1)
        m2 = Meter(v2)

        result1 = (m1 + m2) * scalar
        result2 = (m1 * scalar) + (m2 * scalar)

        assert abs(result1.value - result2.value) < 1e-10
