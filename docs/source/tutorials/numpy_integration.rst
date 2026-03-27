NumPy Integration
=================

Physities works seamlessly with NumPy arrays, allowing you to perform
vectorized operations while preserving unit information.

Basic Usage
-----------

Create arrays of units by multiplying a NumPy array with a unit:

.. code-block:: python

    import numpy as np
    from physities.src.unit import Meter, Second

    # Create array of meters
    distances = np.array([1.0, 2.0, 3.0, 4.0, 5.0]) * Meter(1)
    print(distances)  # [1.0 (L¹) 2.0 (L¹) 3.0 (L¹) 4.0 (L¹) 5.0 (L¹)]

NumPy Functions
---------------

Standard NumPy functions work with unit arrays:

.. code-block:: python

    # Sum preserves the unit
    total = np.sum(distances)
    print(total)        # 15.0 (L¹)
    print(total.value)  # 15.0

    # Mean preserves the unit
    avg = np.mean(distances)
    print(avg)          # 3.0 (L¹)

    # Min/Max
    print(np.min(distances))  # 1.0 (L¹)
    print(np.max(distances))  # 5.0 (L¹)

Array Operations with Scale Propagation
---------------------------------------

When you multiply arrays of units, the scales combine correctly:

.. code-block:: python

    # Meter * Meter = Meter²
    lengths = np.array([2.0, 3.0, 4.0]) * Meter(1)
    widths = np.array([5.0, 6.0, 7.0]) * Meter(1)

    areas = lengths * widths
    print(areas)  # [10.0 (L²) 18.0 (L²) 28.0 (L²)]
    print(areas[0].scale.dimension.length)  # 2.0

Velocity Example
----------------

Calculate velocities from distance and time arrays:

.. code-block:: python

    from physities.src.unit import Meter, Second, Kilometer, Hour

    # Distances in meters
    distances = np.array([100, 200, 300, 400]) * Meter(1)

    # Times in seconds
    times = np.array([10, 20, 30, 40]) * Second(1)

    # Velocities (m/s)
    velocities = distances / times
    print(velocities)  # [10.0 (L¹/t¹) 10.0 (L¹/t¹) ...]

    # Convert to km/h
    Kmh = Kilometer / Hour
    for v in velocities:
        print(v.convert(Kmh))  # 36.0 km/h each

Extracting Values
-----------------

To get a plain NumPy array of values:

.. code-block:: python

    distances = np.array([1.0, 2.0, 3.0]) * Meter(1)

    # Extract values
    values = np.array([d.value for d in distances])
    print(values)  # [1. 2. 3.]

    # Or use list comprehension with conversion
    Km = Meter * 1000
    km_values = np.array([d.convert(Km).value for d in distances])
    print(km_values)  # [0.001 0.002 0.003]

Limitations
-----------

Some NumPy functions that require special methods may not work:

- ``np.std()`` - requires ``conjugate`` method
- ``np.var()`` - requires ``conjugate`` method
- Complex number operations

For these cases, extract values first:

.. code-block:: python

    distances = np.array([1.0, 2.0, 3.0]) * Meter(1)
    values = np.array([d.value for d in distances])
    std = np.std(values)  # Works on plain array
