"""Shared fixtures for benchmark tests."""

import pytest

from physities.src.dimension import Dimension
from physities.src.scale import Scale
from physities.src.unit import Meter, Second, Kilogram, Unit


@pytest.fixture
def length_dimension():
    """Create a length dimension."""
    return Dimension.new_length()


@pytest.fixture
def velocity_dimension():
    """Create a velocity dimension (L/T)."""
    return Dimension.new_instance((1, 0, 0, -1, 0, 0, 0))


@pytest.fixture
def force_dimension():
    """Create a force dimension (M*L/T^2)."""
    return Dimension.new_instance((1, 1, 0, -2, 0, 0, 0))


@pytest.fixture
def meter_scale(length_dimension):
    """Create a meter scale."""
    return Scale.new(dimension=length_dimension)


@pytest.fixture
def kilometer_scale(length_dimension):
    """Create a kilometer scale."""
    return Scale.new(
        dimension=length_dimension,
        from_base_scale_conversions=(1000, 1, 1, 1, 1, 1, 1),
    )


@pytest.fixture
def meter_per_second_scale(velocity_dimension):
    """Create a m/s scale."""
    return Scale.new(dimension=velocity_dimension)


@pytest.fixture
def MeterPerSecond():
    """Create a m/s unit type."""
    return Meter / Second


@pytest.fixture
def Newton():
    """Create a Newton unit type."""
    return Kilogram * Meter / (Second ** 2)
