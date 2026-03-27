#!/usr/bin/env python3
"""Physities Cookbook - Common patterns and recipes.

This module provides practical examples of using Physities for common
physics and engineering calculations.
"""

from physities.src.unit import (
    Meter, Kilometer, Mile, Foot, Inch,
    Second, Minute, Hour,
    Kilogram, Gram, Pound,
    Kelvin,
    Ampere,
)
from physities.src.dimension import Dimension
from physities.src.scale import Scale


# =============================================================================
# Basic Unit Operations
# =============================================================================

def example_basic_units():
    """Basic unit creation and operations."""
    print("=== Basic Unit Operations ===\n")

    # Create simple quantities
    distance = Meter(100)
    time = Second(10)

    print(f"Distance: {distance}")
    print(f"Time: {time}")

    # Calculate velocity
    velocity = distance / time
    print(f"Velocity: {velocity}")

    # Arithmetic
    d1 = Meter(50)
    d2 = Meter(30)
    print(f"Sum: {d1 + d2}")
    print(f"Difference: {d1 - d2}")
    print()


# =============================================================================
# Unit Conversion
# =============================================================================

def example_conversions():
    """Unit conversion examples."""
    print("=== Unit Conversions ===\n")

    # Length conversions
    km = Kilometer(10)
    m = km.convert(Meter)
    miles = km.convert(Mile)
    print(f"{km.value} km = {m.value} m = {miles.value:.2f} miles")

    # Speed conversions
    Ms = Meter / Second
    Kh = Kilometer / Hour

    speed_ms = Ms(10)
    speed_kmh = speed_ms.convert(Kh)
    print(f"{speed_ms.value} m/s = {speed_kmh.value} km/h")

    # To SI
    ft = Foot(100)
    m_si = ft.to_si()
    print(f"{ft.value} feet = {m_si.value:.2f} meters")
    print()


# =============================================================================
# Physics Calculations
# =============================================================================

def example_kinematics():
    """Kinematics calculations."""
    print("=== Kinematics ===\n")

    # Define unit types
    Velocity = Meter / Second
    Acceleration = Meter / (Second ** 2)

    # Initial conditions
    v0 = Velocity(0)      # Initial velocity
    a = Acceleration(9.8)  # Acceleration (gravity)
    t = Second(5)          # Time

    # v = v0 + a*t
    v = v0 + a * t
    print(f"Final velocity after {t.value}s: {v}")

    # s = v0*t + 0.5*a*t^2
    s = v0 * t + (a * t * t) * 0.5
    print(f"Distance fallen: {s}")
    print()


def example_force_and_energy():
    """Force and energy calculations."""
    print("=== Force and Energy ===\n")

    # Define unit types
    Newton = Kilogram * Meter / (Second ** 2)
    Joule = Newton * Meter
    Watt = Joule / Second

    # F = m * a
    mass = Kilogram(10)
    acceleration = (Meter / (Second ** 2))(9.8)
    force = mass * acceleration
    print(f"Weight of {mass}: {force}")

    # Work = F * d
    distance = Meter(5)
    work = force * distance
    print(f"Work to lift {distance}: {work}")

    # Power = Work / time
    time = Second(2)
    power = work / time
    print(f"Power required: {power}")
    print()


def example_density():
    """Density calculations."""
    print("=== Density ===\n")

    # Define volume unit
    Meter3 = Meter ** 3
    Liter = Meter3 / 1000

    # Density = mass / volume
    mass = Kilogram(1000)
    volume = Meter3(1)

    density = mass / volume
    print(f"Density: {density}")

    # Calculate mass from density and volume
    water_density = (Kilogram / Meter3)(1000)
    tank_volume = Liter(500)
    water_mass = water_density * tank_volume
    print(f"Mass of {tank_volume.value} liters of water: {water_mass.to_si()}")
    print()


# =============================================================================
# Custom Units
# =============================================================================

def example_custom_units():
    """Creating custom units."""
    print("=== Custom Units ===\n")

    # Create a Furlong (1/8 mile)
    Furlong = Mile / 8
    furlongs = Furlong(10)
    meters = furlongs.convert(Meter)
    print(f"10 furlongs = {meters.value:.2f} meters")

    # Create a knot (nautical miles per hour)
    NauticalMile = Meter * 1852
    Knot = NauticalMile / Hour

    speed_knots = Knot(10)
    speed_ms = speed_knots.convert(Meter / Second)
    print(f"10 knots = {speed_ms.value:.2f} m/s")

    # Using Scale directly for precise control
    Angstrom_scale = Scale.new(
        dimension=Dimension.new_length(),
        from_base_scale_conversions=(1e-10, 1, 1, 1, 1, 1, 1),
    )

    # Create a unit class
    from physities.src.unit import Unit

    class Angstrom(Unit):
        scale = Angstrom_scale
        value = None

    # Use the custom unit
    wavelength = Angstrom(5500)  # Green light
    nm = wavelength.to_si()
    print(f"5500 Angstroms = {nm.value * 1e9:.1f} nm")
    print()


# =============================================================================
# Dimensional Analysis
# =============================================================================

def example_dimensional_analysis():
    """Dimensional analysis examples."""
    print("=== Dimensional Analysis ===\n")

    # Check dimensions
    velocity = Meter / Second
    print(f"Velocity dimension: L={velocity.scale.dimension.length}, "
          f"T={velocity.scale.dimension.time}")

    # Force = mass * acceleration
    Newton = Kilogram * Meter / (Second ** 2)
    print(f"Force dimension: L={Newton.scale.dimension.length}, "
          f"M={Newton.scale.dimension.mass}, T={Newton.scale.dimension.time}")

    # Energy = force * distance
    Joule = Newton * Meter
    print(f"Energy dimension: L={Joule.scale.dimension.length}, "
          f"M={Joule.scale.dimension.mass}, T={Joule.scale.dimension.time}")

    # Dimensionless ratio
    ratio = Meter(100) / Meter(50)
    print(f"Ratio is dimensionless: {ratio.scale.is_dimensionless}")
    print()


# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":
    example_basic_units()
    example_conversions()
    example_kinematics()
    example_force_and_energy()
    example_density()
    example_custom_units()
    example_dimensional_analysis()
