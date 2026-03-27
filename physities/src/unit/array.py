"""NumPy array support for batch unit operations.

This module provides high-performance batch operations on arrays of values
with the same unit type. Operations are vectorized using NumPy for speed.

Example:
    >>> from physities.src.unit import Meter, Kilometer
    >>> from physities.src.unit.array import UnitArray
    >>>
    >>> # Create array of distances
    >>> distances = UnitArray(Meter, [100, 200, 300, 400, 500])
    >>>
    >>> # Batch operations
    >>> doubled = distances * 2
    >>> total = distances.sum()
    >>> mean = distances.mean()
    >>>
    >>> # Convert all values at once
    >>> km_distances = distances.convert(Kilometer)
"""

from __future__ import annotations

import numpy as np
from numpy.typing import ArrayLike, NDArray
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from physities.src.unit.unit import MetaUnit, Unit
    from physities.src.scale.scale import Scale


class UnitArray:
    """Array of values with a common unit type.

    UnitArray provides NumPy-accelerated batch operations for physical quantities.
    All values in the array share the same unit (Scale), enabling efficient
    vectorized computation.

    Attributes:
        unit_type: The Unit class (e.g., Meter, Second) for all values.
        values: NumPy array of numeric values.
        scale: The Scale defining the unit's dimension and conversion factors.

    Examples:
        >>> # Create from list
        >>> temps = UnitArray(Kelvin, [273.15, 293.15, 310.15])

        >>> # Create from NumPy array
        >>> speeds = UnitArray(MetersPerSecond, np.linspace(0, 100, 1000))

        >>> # Arithmetic (vectorized)
        >>> doubled = speeds * 2
        >>> shifted = temps + Kelvin(10)  # Broadcasts scalar

        >>> # Reductions
        >>> total = speeds.sum()      # Returns single Unit
        >>> avg = temps.mean()        # Returns single Unit
        >>> std = speeds.std()        # Returns single Unit

        >>> # Convert all values
        >>> mph = speeds.convert(MilesPerHour)
    """

    __slots__ = ('_unit_type', '_values', '_scale')

    def __init__(self, unit_type: MetaUnit, values: ArrayLike):
        """Create a UnitArray.

        Args:
            unit_type: The Unit class (e.g., Meter, Second).
            values: Array-like of numeric values.
        """
        self._unit_type = unit_type
        self._values = np.asarray(values, dtype=np.float64)
        self._scale = unit_type.scale

    @classmethod
    def from_units(cls, units: list[Unit]) -> UnitArray:
        """Create UnitArray from a list of Unit instances.

        All units must have the same scale (unit type).

        Args:
            units: List of Unit instances.

        Returns:
            UnitArray containing all values.

        Raises:
            ValueError: If units have different scales.
        """
        if not units:
            raise ValueError("Cannot create UnitArray from empty list")

        first_scale = units[0].scale
        values = []
        for u in units:
            if u.scale != first_scale:
                raise ValueError("All units must have the same scale")
            values.append(u.value)

        return cls(type(units[0]), values)

    @property
    def unit_type(self) -> MetaUnit:
        """The Unit class for all values."""
        return self._unit_type

    @property
    def values(self) -> NDArray[np.float64]:
        """NumPy array of numeric values."""
        return self._values

    @property
    def scale(self) -> Scale:
        """The Scale defining the unit."""
        return self._scale

    @property
    def shape(self) -> tuple[int, ...]:
        """Shape of the underlying array."""
        return self._values.shape

    @property
    def size(self) -> int:
        """Total number of elements."""
        return self._values.size

    def __len__(self) -> int:
        return len(self._values)

    def __repr__(self) -> str:
        dim = self._scale.dimension.show_dimension() or "Scalar"
        return f"UnitArray({dim}, shape={self.shape})"

    def __getitem__(self, index) -> Unit | UnitArray:
        """Index or slice the array.

        Returns:
            Single Unit for scalar index, UnitArray for slice.
        """
        result = self._values[index]
        if np.ndim(result) == 0:
            # Scalar - return Unit
            unit = self._unit_type(float(result))
            unit.scale = self._scale
            return unit
        else:
            # Array - return UnitArray
            return UnitArray._from_values(self._unit_type, self._scale, result)

    @classmethod
    def _from_values(cls, unit_type: MetaUnit, scale: Scale, values: NDArray) -> UnitArray:
        """Internal: create UnitArray with explicit scale."""
        arr = object.__new__(cls)
        arr._unit_type = unit_type
        arr._scale = scale
        arr._values = values
        return arr

    # =========================================================================
    # Arithmetic operations (vectorized)
    # =========================================================================

    def __add__(self, other) -> UnitArray:
        """Add arrays or broadcast scalar Unit."""
        if isinstance(other, UnitArray):
            if self._scale.dimension != other._scale.dimension:
                raise ValueError("Cannot add arrays with different dimensions")
            # Convert other to same scale
            factor = other._scale.conversion_factor / self._scale.conversion_factor
            new_values = self._values + other._values * factor
            return UnitArray._from_values(self._unit_type, self._scale, new_values)

        # Import here to avoid circular import
        from physities.src.unit.unit import Unit
        if isinstance(other, Unit):
            if self._scale.dimension != other.scale.dimension:
                raise ValueError("Cannot add Unit with different dimension")
            factor = other.scale.conversion_factor / self._scale.conversion_factor
            new_values = self._values + other.value * factor
            return UnitArray._from_values(self._unit_type, self._scale, new_values)

        raise TypeError(f"Cannot add UnitArray and {type(other)}")

    def __radd__(self, other) -> UnitArray:
        return self.__add__(other)

    def __sub__(self, other) -> UnitArray:
        """Subtract arrays or broadcast scalar Unit."""
        if isinstance(other, UnitArray):
            if self._scale.dimension != other._scale.dimension:
                raise ValueError("Cannot subtract arrays with different dimensions")
            factor = other._scale.conversion_factor / self._scale.conversion_factor
            new_values = self._values - other._values * factor
            return UnitArray._from_values(self._unit_type, self._scale, new_values)

        from physities.src.unit.unit import Unit
        if isinstance(other, Unit):
            if self._scale.dimension != other.scale.dimension:
                raise ValueError("Cannot subtract Unit with different dimension")
            factor = other.scale.conversion_factor / self._scale.conversion_factor
            new_values = self._values - other.value * factor
            return UnitArray._from_values(self._unit_type, self._scale, new_values)

        raise TypeError(f"Cannot subtract UnitArray and {type(other)}")

    def __mul__(self, other) -> UnitArray:
        """Multiply by scalar or array."""
        if isinstance(other, (int, float, np.number)):
            new_values = self._values * other
            return UnitArray._from_values(self._unit_type, self._scale, new_values)

        if isinstance(other, np.ndarray):
            new_values = self._values * other
            return UnitArray._from_values(self._unit_type, self._scale, new_values)

        if isinstance(other, UnitArray):
            new_scale = self._scale * other._scale
            new_values = self._values * other._values
            # Create a generic unit type for the result
            from physities.src.unit.unit import Unit
            new_type = type("Unit", (Unit,), {"scale": new_scale, "value": None})
            return UnitArray._from_values(new_type, new_scale, new_values)

        raise TypeError(f"Cannot multiply UnitArray by {type(other)}")

    def __rmul__(self, other) -> UnitArray:
        return self.__mul__(other)

    def __truediv__(self, other) -> UnitArray:
        """Divide by scalar or array."""
        if isinstance(other, (int, float, np.number)):
            new_values = self._values / other
            return UnitArray._from_values(self._unit_type, self._scale, new_values)

        if isinstance(other, np.ndarray):
            new_values = self._values / other
            return UnitArray._from_values(self._unit_type, self._scale, new_values)

        if isinstance(other, UnitArray):
            new_scale = self._scale / other._scale
            new_values = self._values / other._values
            from physities.src.unit.unit import Unit
            new_type = type("Unit", (Unit,), {"scale": new_scale, "value": None})
            return UnitArray._from_values(new_type, new_scale, new_values)

        raise TypeError(f"Cannot divide UnitArray by {type(other)}")

    def __pow__(self, power: float) -> UnitArray:
        """Raise to power."""
        if not isinstance(power, (int, float)):
            raise TypeError("Power must be a number")
        new_scale = self._scale ** power
        new_values = self._values ** power
        from physities.src.unit.unit import Unit
        new_type = type("Unit", (Unit,), {"scale": new_scale, "value": None})
        return UnitArray._from_values(new_type, new_scale, new_values)

    # =========================================================================
    # Reduction operations
    # =========================================================================

    def sum(self) -> Unit:
        """Sum all values. Returns a single Unit."""
        total = float(np.sum(self._values))
        unit = self._unit_type(total)
        unit.scale = self._scale
        return unit

    def mean(self) -> Unit:
        """Mean of all values. Returns a single Unit."""
        avg = float(np.mean(self._values))
        unit = self._unit_type(avg)
        unit.scale = self._scale
        return unit

    def std(self) -> Unit:
        """Standard deviation. Returns a single Unit."""
        s = float(np.std(self._values))
        unit = self._unit_type(s)
        unit.scale = self._scale
        return unit

    def min(self) -> Unit:
        """Minimum value. Returns a single Unit."""
        m = float(np.min(self._values))
        unit = self._unit_type(m)
        unit.scale = self._scale
        return unit

    def max(self) -> Unit:
        """Maximum value. Returns a single Unit."""
        m = float(np.max(self._values))
        unit = self._unit_type(m)
        unit.scale = self._scale
        return unit

    # =========================================================================
    # Conversion
    # =========================================================================

    def convert(self, target_unit: MetaUnit) -> UnitArray:
        """Convert all values to a different unit.

        Args:
            target_unit: The target unit type.

        Returns:
            New UnitArray with converted values.

        Raises:
            ValueError: If dimensions don't match.
        """
        if self._scale.dimension != target_unit.scale.dimension:
            raise ValueError("Cannot convert to unit with different dimension")

        factor = self._scale.conversion_factor / target_unit.scale.conversion_factor
        new_values = self._values * factor
        return UnitArray._from_values(target_unit, target_unit.scale, new_values)

    def to_si(self) -> UnitArray:
        """Convert all values to SI base units.

        Returns:
            New UnitArray with values in SI units.
        """
        from physities.src.scale.scale import Scale
        from physities.src.unit.unit import Unit

        new_values = self._values * self._scale.conversion_factor
        new_scale = Scale.new(dimension=self._scale.dimension)
        new_type = type("Unit", (Unit,), {"scale": new_scale, "value": None})
        return UnitArray._from_values(new_type, new_scale, new_values)

    def to_numpy(self) -> NDArray[np.float64]:
        """Get raw NumPy array of values (no unit info)."""
        return self._values.copy()

    def to_list(self) -> list[Unit]:
        """Convert to list of Unit instances."""
        result = []
        for v in self._values.flat:
            unit = self._unit_type(float(v))
            unit.scale = self._scale
            result.append(unit)
        return result
