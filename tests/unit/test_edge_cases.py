"""Edge case tests for physities."""

import pytest

from physities.src.dimension import Dimension
from physities.src.scale import Scale
from physities.src.unit import Meter, Second, Kilogram, Unit
from physities.src.exceptions import (
    DimensionMismatchError,
    InvalidConversionError,
    InvalidOperationError,
    InvalidPowerError,
)


@pytest.mark.unit
class TestDimensionEdgeCases:
    """Edge case tests for Dimension class."""

    def test_zero_power_dimension(self):
        """Test dimension with zero power."""
        dim = Dimension.new_length(power=0)
        assert dim.length == 0
        assert dim == Dimension.new_dimensionless()

    def test_negative_power_dimension(self):
        """Test dimension with negative power."""
        dim = Dimension.new_time(power=-2)
        assert dim.time == -2

    def test_fractional_power_dimension(self):
        """Test dimension with fractional power."""
        dim = Dimension.new_length(power=0.5)
        assert dim.length == 0.5

    def test_very_large_exponent(self):
        """Test dimension with very large exponent."""
        dim = Dimension.new_length(power=100)
        assert dim.length == 100

    def test_very_small_exponent(self):
        """Test dimension with very small exponent."""
        dim = Dimension.new_length(power=0.001)
        assert abs(dim.length - 0.001) < 1e-10

    def test_all_dimensions_combined(self):
        """Test combining all 7 base dimensions."""
        dim = Dimension.new_instance((1, 2, 3, 4, 5, 6, 7))
        assert dim.length == 1
        assert dim.mass == 2
        assert dim.temperature == 3
        assert dim.time == 4
        assert dim.amount == 5
        assert dim.electric_current == 6
        assert dim.luminous_intensity == 7


@pytest.mark.unit
class TestScaleEdgeCases:
    """Edge case tests for Scale class."""

    def test_scale_with_unit_conversion_factors(self):
        """Test scale with all unit conversion factors."""
        scale = Scale.new()
        assert scale.conversion_factor == 1.0

    def test_scale_with_zero_rescale_gives_zero_conversion(self):
        """Test scale behavior with extreme values."""
        scale = Scale.new(
            dimension=Dimension.new_length(),
            rescale_value=0,
        )
        assert scale.conversion_factor == 0

    def test_scale_multiplication_with_zero(self):
        """Test scale multiplication by zero."""
        scale = Scale.new(dimension=Dimension.new_length())
        result = scale * 0

        assert result.conversion_factor == 0

    def test_scale_power_of_zero(self):
        """Test scale raised to power of zero."""
        scale = Scale.new(
            dimension=Dimension.new_length(),
            from_base_scale_conversions=(1000, 1, 1, 1, 1, 1, 1),
        )

        result = scale ** 0

        assert result.is_dimensionless
        assert result.conversion_factor == 1.0

    def test_scale_negative_power(self):
        """Test scale with negative power."""
        scale = Scale.new(dimension=Dimension.new_length())
        result = scale ** -1

        assert result.dimension.length == -1

    def test_scale_fractional_power(self):
        """Test scale with fractional power."""
        scale = Scale.new(
            dimension=Dimension.new_length(power=2),
            from_base_scale_conversions=(100, 1, 1, 1, 1, 1, 1),
        )

        result = scale ** 0.5
        assert result.dimension.length == 1


@pytest.mark.unit
class TestUnitEdgeCases:
    """Edge case tests for Unit class."""

    def test_unit_with_zero_value(self):
        """Test unit with zero value."""
        m = Meter(0)
        assert m.value == 0

        # Operations with zero
        result = m * 100
        assert result.value == 0

    def test_unit_with_negative_value(self):
        """Test unit with negative value."""
        m = Meter(-10)
        assert m.value == -10

    def test_unit_with_very_large_value(self):
        """Test unit with very large value."""
        m = Meter(1e100)
        assert m.value == 1e100

    def test_unit_with_very_small_value(self):
        """Test unit with very small positive value."""
        m = Meter(1e-100)
        assert m.value == 1e-100

    def test_unit_division_by_self_type(self):
        """Test division of unit by same unit type."""
        m1 = Meter(100)
        m2 = Meter(10)

        result = m1 / m2
        assert result.value == 10
        assert result.scale.is_dimensionless

    def test_unit_power_of_zero(self):
        """Test unit raised to power of zero."""
        m = Meter(100)
        result = m ** 0

        assert result.value == 1
        assert result.scale.is_dimensionless

    def test_unit_power_of_one(self):
        """Test unit raised to power of one."""
        m = Meter(100)
        result = m ** 1

        assert result.value == 100
        assert result.scale.dimension.length == 1

    def test_unit_conversion_to_same_unit(self):
        """Test converting unit to itself."""
        m = Meter(100)
        result = m.convert(Meter)

        assert result.value == 100

    def test_unit_equality_with_different_scales(self):
        """Test unit equality when values differ but physical quantity same."""
        Kilometer = Meter * 1000
        m = Meter(1000)
        km = Kilometer(1)

        assert m == km

    def test_composite_unit_creation_chain(self):
        """Test creating composite unit through chain of operations."""
        # Newton = kg * m / s^2
        Newton = Kilogram * Meter / (Second ** 2)

        # Pascal = N / m^2 = kg / (m * s^2)
        Pascal = Newton / (Meter ** 2)

        p = Pascal(100)
        assert p.value == 100
        assert p.scale.dimension.mass == 1
        assert p.scale.dimension.length == -1
        assert p.scale.dimension.time == -2


@pytest.mark.unit
class TestExceptionEdgeCases:
    """Edge case tests for exception handling."""

    def test_dimension_mismatch_in_addition(self):
        """Test DimensionMismatchError in addition."""
        m = Meter(10)
        s = Second(10)

        with pytest.raises(DimensionMismatchError) as exc_info:
            m + s

        assert "addition" in str(exc_info.value)

    def test_dimension_mismatch_in_subtraction(self):
        """Test DimensionMismatchError in subtraction."""
        m = Meter(10)
        s = Second(10)

        with pytest.raises(DimensionMismatchError) as exc_info:
            m - s

        assert "subtraction" in str(exc_info.value)

    def test_dimension_mismatch_in_conversion(self):
        """Test DimensionMismatchError in conversion."""
        m = Meter(10)

        with pytest.raises(DimensionMismatchError) as exc_info:
            m.convert(Second)

        assert "conversion" in str(exc_info.value)

    def test_invalid_conversion_target(self):
        """Test InvalidConversionError with invalid target."""
        m = Meter(10)

        with pytest.raises(InvalidConversionError):
            m.convert("not a unit")

    def test_invalid_operation_with_string(self):
        """Test InvalidOperationError with string operand."""
        m = Meter(10)

        with pytest.raises(InvalidOperationError):
            m * "string"

    def test_invalid_power_with_string(self):
        """Test InvalidPowerError with string exponent."""
        m = Meter(10)

        with pytest.raises(InvalidPowerError):
            m ** "two"

    def test_invalid_power_with_list(self):
        """Test InvalidPowerError with list exponent."""
        m = Meter(10)

        with pytest.raises(InvalidPowerError):
            m ** [2]

    def test_invalid_operation_addition_with_number(self):
        """Test InvalidOperationError when adding number to unit."""
        m = Meter(10)

        with pytest.raises(InvalidOperationError):
            m + 5


@pytest.mark.unit
class TestBoundaryConditions:
    """Test boundary conditions and limits."""

    def test_repeated_operations_precision(self):
        """Test that repeated operations don't accumulate errors."""
        m = Meter(1.0)

        # Multiply and divide by same number many times
        for _ in range(100):
            m = m * 2
            m = m / 2

        assert abs(m.value - 1.0) < 1e-10

    def test_conversion_chain_precision(self):
        """Test precision in conversion chains."""
        Kilometer = Meter * 1000
        Centimeter = Meter / 100

        # Start with 1 km
        val = Kilometer(1)

        # Convert through chain
        val = val.convert(Meter)
        val = val.convert(Centimeter)
        val = val.convert(Kilometer)

        assert abs(val.value - 1.0) < 1e-10

    def test_high_dimension_power(self):
        """Test high power operations on dimensions."""
        dim = Dimension.new_length()

        result = dim * 10
        assert result.length == 10

    def test_floating_point_dimension_equality(self):
        """Test dimension equality with floating point values."""
        dim1 = Dimension.new_instance((1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0))
        dim2 = Dimension.new_instance((1, 0, 0, 0, 0, 0, 0))

        assert dim1 == dim2
