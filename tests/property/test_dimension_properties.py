"""Property-based tests for Dimension class."""

import pytest
from hypothesis import given, strategies as st, assume

from physities.src.dimension import Dimension


# Strategy for valid dimension exponents
dimension_exponent = st.floats(min_value=-10, max_value=10, allow_nan=False, allow_infinity=False)

# Strategy for dimension tuples
dimension_tuple = st.tuples(
    dimension_exponent,
    dimension_exponent,
    dimension_exponent,
    dimension_exponent,
    dimension_exponent,
    dimension_exponent,
    dimension_exponent,
)


@pytest.mark.property
class TestDimensionProperties:
    """Property-based tests for Dimension class."""

    @given(dim_tuple=dimension_tuple)
    def test_dimension_creation_roundtrip(self, dim_tuple):
        """Test that dimension creation preserves tuple values."""
        dim = Dimension.new_instance(dimensions_tuple=dim_tuple)
        assert dim.dimensions_tuple == dim_tuple

    @given(dim_tuple1=dimension_tuple, dim_tuple2=dimension_tuple)
    def test_addition_commutative(self, dim_tuple1, dim_tuple2):
        """Test that dimension addition is commutative."""
        dim1 = Dimension.new_instance(dimensions_tuple=dim_tuple1)
        dim2 = Dimension.new_instance(dimensions_tuple=dim_tuple2)

        result1 = dim1 + dim2
        result2 = dim2 + dim1

        assert result1 == result2

    @given(dim_tuple1=dimension_tuple, dim_tuple2=dimension_tuple, dim_tuple3=dimension_tuple)
    def test_addition_associative(self, dim_tuple1, dim_tuple2, dim_tuple3):
        """Test that dimension addition is associative."""
        dim1 = Dimension.new_instance(dimensions_tuple=dim_tuple1)
        dim2 = Dimension.new_instance(dimensions_tuple=dim_tuple2)
        dim3 = Dimension.new_instance(dimensions_tuple=dim_tuple3)

        result1 = (dim1 + dim2) + dim3
        result2 = dim1 + (dim2 + dim3)

        # Check each component (floating point tolerance)
        for i in range(7):
            assert abs(result1.dimensions_tuple[i] - result2.dimensions_tuple[i]) < 1e-10

    @given(dim_tuple=dimension_tuple)
    def test_addition_identity(self, dim_tuple):
        """Test that adding dimensionless dimension is identity."""
        dim = Dimension.new_instance(dimensions_tuple=dim_tuple)
        zero = Dimension.new_dimensionless()

        result = dim + zero

        assert result == dim

    @given(dim_tuple=dimension_tuple, scalar=st.floats(min_value=-100, max_value=100, allow_nan=False, allow_infinity=False))
    def test_scalar_multiplication_distributes(self, dim_tuple, scalar):
        """Test that scalar multiplication distributes over addition."""
        dim = Dimension.new_instance(dimensions_tuple=dim_tuple)

        result = dim * scalar

        for i in range(7):
            expected = dim_tuple[i] * scalar
            assert abs(result.dimensions_tuple[i] - expected) < 1e-10

    @given(dim_tuple=dimension_tuple, scalar1=st.floats(min_value=0.1, max_value=10, allow_nan=False, allow_infinity=False),
           scalar2=st.floats(min_value=0.1, max_value=10, allow_nan=False, allow_infinity=False))
    def test_scalar_multiplication_associative(self, dim_tuple, scalar1, scalar2):
        """Test that scalar multiplication is associative."""
        dim = Dimension.new_instance(dimensions_tuple=dim_tuple)

        result1 = (dim * scalar1) * scalar2
        result2 = dim * (scalar1 * scalar2)

        for i in range(7):
            assert abs(result1.dimensions_tuple[i] - result2.dimensions_tuple[i]) < 1e-10

    @given(dim_tuple=dimension_tuple)
    def test_subtraction_is_inverse_of_addition(self, dim_tuple):
        """Test that subtraction is the inverse of addition."""
        dim = Dimension.new_instance(dimensions_tuple=dim_tuple)

        result = dim + dim - dim

        assert result == dim

    @given(power=st.floats(min_value=0.5, max_value=5, allow_nan=False, allow_infinity=False))
    def test_new_methods_with_power(self, power):
        """Test dimension creation methods with various powers."""
        length = Dimension.new_length(power=power)
        assert abs(length.length - power) < 1e-10

        time = Dimension.new_time(power=power)
        assert abs(time.time - power) < 1e-10

        mass = Dimension.new_mass(power=power)
        assert abs(mass.mass - power) < 1e-10

    @given(dim_tuple=dimension_tuple)
    def test_equality_reflexive(self, dim_tuple):
        """Test that equality is reflexive."""
        dim = Dimension.new_instance(dimensions_tuple=dim_tuple)
        assert dim == dim

    @given(dim_tuple=dimension_tuple)
    def test_equality_symmetric(self, dim_tuple):
        """Test that equality is symmetric."""
        dim1 = Dimension.new_instance(dimensions_tuple=dim_tuple)
        dim2 = Dimension.new_instance(dimensions_tuple=dim_tuple)

        assert (dim1 == dim2) == (dim2 == dim1)
