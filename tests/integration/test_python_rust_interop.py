"""Integration tests for Python/Rust interoperability."""

import pytest

from physities.src.dimension import Dimension
from physities.src.scale import Scale
from physities.src.unit import Meter, Second, Kilometer, Kilogram

# Try to import Rust backend
try:
    from physities._physities_core import PhysicalScale
    HAS_RUST = True
except ImportError:
    HAS_RUST = False


@pytest.mark.integration
class TestPythonRustInterop:
    """Test interoperability between Python layer and Rust core."""

    def test_scale_operations_consistency(self):
        """Verify Python Scale operations produce consistent results."""
        # Create velocity scale
        velocity_dim = Dimension.new_instance((1, 0, 0, -1, 0, 0, 0))
        velocity_scale = Scale.new(
            dimension=velocity_dim,
            from_base_scale_conversions=(1000, 1, 1, 1, 1, 1, 1),
        )

        # Operations should be consistent
        squared = velocity_scale * velocity_scale
        assert squared.dimension.length == 2
        assert squared.dimension.time == -2

        # Division should undo multiplication
        original = squared / velocity_scale
        assert original == velocity_scale

    def test_unit_conversion_accuracy(self):
        """Test unit conversion maintains numerical accuracy."""
        # Create a speed value
        Ms = Meter / Second
        Kh = Kilometer / (Second * 60 * 60)

        # 36 km/h should equal 10 m/s
        speed_kmh = Kh(36)
        speed_ms = speed_kmh.convert(Ms)

        assert abs(speed_ms.value - 10.0) < 1e-10

    def test_composite_unit_creation(self):
        """Test creating composite units through operations."""
        # Newton = kg * m / s^2
        Newton = Kilogram * Meter / (Second ** 2)

        # Create a force
        force = Newton(100)
        assert force.value == 100

        # Check dimensions
        assert force.scale.dimension.mass == 1
        assert force.scale.dimension.length == 1
        assert force.scale.dimension.time == -2

    def test_scale_power_operations(self):
        """Test power operations on scales."""
        meter_scale = Scale.new(dimension=Dimension.new_length())

        # Square meter
        meter2_scale = meter_scale ** 2
        assert meter2_scale.dimension.length == 2

        # Cube meter
        meter3_scale = meter_scale ** 3
        assert meter3_scale.dimension.length == 3

        # Square root (fractional power)
        sqrt_meter2 = meter2_scale ** 0.5
        assert abs(sqrt_meter2.dimension.length - 1.0) < 1e-10

    def test_dimensionless_operations(self):
        """Test operations that result in dimensionless quantities."""
        # Ratio of lengths should be dimensionless
        ratio = Meter(100) / Meter(10)

        assert ratio.scale.is_dimensionless
        assert ratio.value == 10.0

    def test_unit_arithmetic_precision(self):
        """Test arithmetic operations maintain precision."""
        Ms = Meter / Second

        v1 = Ms(1.0)
        v2 = Ms(2.0)
        v3 = Ms(3.0)

        # Addition
        total = v1 + v2 + v3
        assert abs(total.value - 6.0) < 1e-15

        # Subtraction
        diff = v3 - v1
        assert abs(diff.value - 2.0) < 1e-15

        # Multiplication with scalar
        doubled = v2 * 2
        assert abs(doubled.value - 4.0) < 1e-15

        # Division by scalar
        halved = v2 / 2
        assert abs(halved.value - 1.0) < 1e-15


@pytest.mark.integration
class TestRustBackendIntegration:
    """Test Rust backend integration methods."""

    def test_has_rust_backend(self):
        """Test has_rust_backend() returns correct value."""
        assert Scale.has_rust_backend() == HAS_RUST

    @pytest.mark.skipif(not HAS_RUST, reason="Rust backend not available")
    def test_to_rust_and_from_rust(self):
        """Test converting Scale to/from Rust PhysicalScale."""
        # Create a Python Scale
        velocity_dim = Dimension.new_instance((1, 0, 0, -1, 0, 0, 0))
        py_scale = Scale.new(
            dimension=velocity_dim,
            from_base_scale_conversions=(1000, 1, 1, 3600, 1, 1, 1),
            rescale_value=1.0,
        )

        # Convert to Rust
        rust_scale = py_scale.to_rust()
        assert rust_scale is not None
        assert rust_scale.length == 1.0
        assert rust_scale.time == -1.0

        # Convert back to Python
        py_scale_back = Scale.from_rust(rust_scale)
        assert py_scale == py_scale_back

    @pytest.mark.skipif(not HAS_RUST, reason="Rust backend not available")
    def test_rust_multiply_scale(self):
        """Test Scale multiplication uses Rust backend."""
        m_scale = Meter.scale
        s_scale = Second.scale

        # This should use Rust internally
        velocity_scale = m_scale / s_scale

        assert velocity_scale.dimension.length == 1.0
        assert velocity_scale.dimension.time == -1.0

    @pytest.mark.skipif(not HAS_RUST, reason="Rust backend not available")
    def test_rust_power_operation(self):
        """Test Scale power uses Rust backend."""
        m_scale = Meter.scale

        # This should use Rust internally
        m2_scale = m_scale ** 2

        assert m2_scale.dimension.length == 2.0

    @pytest.mark.skipif(not HAS_RUST, reason="Rust backend not available")
    def test_rust_scalar_operations(self):
        """Test scalar multiplication/division uses Rust backend."""
        m_scale = Meter.scale

        # Scalar multiplication
        km_scale = m_scale * 1000
        assert km_scale.conversion_factor == 1000.0

        # Scalar division
        mm_scale = m_scale / 1000
        assert abs(mm_scale.conversion_factor - 0.001) < 1e-15

        # Reverse division (1 / scale)
        inv_m_scale = 1 / m_scale
        assert inv_m_scale.dimension.length == -1.0

    @pytest.mark.skipif(not HAS_RUST, reason="Rust backend not available")
    def test_rust_serialization(self):
        """Test Rust PhysicalScale serialization."""
        m_scale = Meter.scale
        rust_scale = m_scale.to_rust()

        # JSON serialization
        json_str = rust_scale.to_json()
        restored = PhysicalScale.from_json(json_str)
        assert rust_scale.equals(restored)

        # Int64 encoding
        encoded = rust_scale.to_dimension_int64()
        restored_from_int = PhysicalScale.from_dimension_int64(encoded)
        assert rust_scale.same_dimension(restored_from_int)
