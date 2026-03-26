Basic Usage
===========

This tutorial covers the fundamental concepts and usage patterns of Physities.

Understanding Dimensions
------------------------

Physical quantities have dimensions that describe what they measure. Physities
uses the 7 SI base dimensions:

1. **Length** (L) - meters
2. **Mass** (M) - kilograms
3. **Time** (T) - seconds
4. **Temperature** (Θ) - kelvin
5. **Amount** (N) - moles
6. **Electric Current** (I) - amperes
7. **Luminous Intensity** (J) - candelas

Each physical quantity can be expressed as a combination of these base dimensions.
For example:

- Velocity: L·T⁻¹ (length per time)
- Force: M·L·T⁻² (mass times acceleration)
- Energy: M·L²·T⁻² (force times distance)

Creating Dimensions
^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from physities.src.dimension import Dimension

   # Create base dimensions
   length = Dimension.new_length()
   time = Dimension.new_time()
   mass = Dimension.new_mass()

   # Create composite dimensions
   velocity = Dimension.new_instance((1, 0, 0, -1, 0, 0, 0))  # L/T
   # Order: LENGTH, MASS, TEMPERATURE, TIME, AMOUNT, CURRENT, LUMINOSITY

   # Check dimension properties
   print(velocity.length)  # 1
   print(velocity.time)    # -1

Understanding Scales
--------------------

A Scale combines a Dimension with conversion factors that define how to convert
to SI base units.

.. code-block:: python

   from physities.src.scale import Scale
   from physities.src.dimension import Dimension

   # Meter scale (SI base unit)
   meter_scale = Scale.new(dimension=Dimension.new_length())

   # Kilometer scale (1 km = 1000 m)
   km_scale = Scale.new(
       dimension=Dimension.new_length(),
       from_base_scale_conversions=(1000, 1, 1, 1, 1, 1, 1),
   )

   print(km_scale.conversion_factor)  # 1000.0

Working with Units
------------------

Units are the primary way to work with physical quantities. They combine a
numeric value with a Scale.

Creating Unit Values
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from physities.src.unit import Meter, Kilometer, Second

   # Create simple values
   distance = Meter(100)
   time = Second(10)

   # Access the value and scale
   print(distance.value)  # 100
   print(distance.scale.dimension.length)  # 1

Creating Custom Unit Types
^^^^^^^^^^^^^^^^^^^^^^^^^^

Create new unit types by combining existing ones:

.. code-block:: python

   from physities.src.unit import Meter, Second, Kilogram

   # Velocity
   MeterPerSecond = Meter / Second

   # Acceleration
   MeterPerSecondSquared = Meter / (Second ** 2)

   # Force
   Newton = Kilogram * MeterPerSecondSquared

   # Energy
   Joule = Newton * Meter

   # Create values
   v = MeterPerSecond(10)
   a = MeterPerSecondSquared(9.8)
   F = Newton(100)
   E = Joule(500)

Arithmetic Operations
---------------------

Addition and Subtraction
^^^^^^^^^^^^^^^^^^^^^^^^

Units of the same dimension can be added or subtracted:

.. code-block:: python

   from physities.src.unit import Meter, Kilometer

   d1 = Meter(100)
   d2 = Meter(50)

   total = d1 + d2   # 150 m
   diff = d1 - d2    # 50 m

   # Works with different scales of same dimension
   d3 = Kilometer(1)  # 1000 m
   mixed = d1 + d3    # Converts and adds

Multiplication and Division
^^^^^^^^^^^^^^^^^^^^^^^^^^^

These operations combine dimensions:

.. code-block:: python

   from physities.src.unit import Meter, Second, Kilogram

   # Division creates new dimensions
   distance = Meter(100)
   time = Second(10)
   velocity = distance / time  # 10 m/s

   # Multiplication creates new dimensions
   mass = Kilogram(5)
   force = mass * (velocity / time)  # Force in Newtons

   # Scalar multiplication preserves dimension
   doubled = velocity * 2  # 20 m/s

Powers
^^^^^^

Raise units to powers:

.. code-block:: python

   from physities.src.unit import Meter

   length = Meter(10)
   area = length ** 2    # 100 m²
   volume = length ** 3  # 1000 m³

   # Fractional powers
   side = area ** 0.5    # 10 m

   # Inverse
   inverse = length ** -1  # 1/m

Dimensionless Quantities
------------------------

When operations cancel out dimensions, you get a dimensionless result:

.. code-block:: python

   from physities.src.unit import Meter

   d1 = Meter(100)
   d2 = Meter(50)

   ratio = d1 / d2
   print(ratio.value)  # 2.0
   print(ratio.scale.is_dimensionless)  # True

Best Practices
--------------

1. **Use descriptive unit type names**:

   .. code-block:: python

      Velocity = Meter / Second
      Acceleration = Meter / (Second ** 2)

2. **Check dimensions before operations**:

   .. code-block:: python

      from physities.src.exceptions import DimensionMismatchError

      try:
          result = Meter(10) + Second(5)
      except DimensionMismatchError:
          print("Incompatible dimensions!")

3. **Convert to consistent units early**:

   .. code-block:: python

      # Convert all to SI first
      si_value = km_value.to_si()
