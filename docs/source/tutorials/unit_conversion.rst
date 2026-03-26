Unit Conversion
===============

This tutorial explains how to convert between different units in Physities.

Basic Conversion
----------------

Use the ``convert()`` method to convert between units of the same dimension:

.. code-block:: python

   from physities.src.unit import Meter, Kilometer, Mile

   # Create a distance in meters
   distance = Meter(5000)

   # Convert to kilometers
   km = distance.convert(Kilometer)
   print(km.value)  # 5.0

   # Convert to miles
   miles = distance.convert(Mile)
   print(f"{miles.value:.2f}")  # 3.11

Converting to SI Units
----------------------

The ``to_si()`` method converts any unit to its SI base equivalent:

.. code-block:: python

   from physities.src.unit import Kilometer, Hour, Pound

   # Length to meters
   km = Kilometer(10)
   m = km.to_si()
   print(m.value)  # 10000.0

   # Mass to kilograms
   lb = Pound(10)
   kg = lb.to_si()
   print(f"{kg.value:.2f}")  # 4.54

Composite Unit Conversion
-------------------------

Convert composite units like velocity:

.. code-block:: python

   from physities.src.unit import Meter, Kilometer, Second, Hour

   # Define unit types
   MetersPerSecond = Meter / Second
   KilometersPerHour = Kilometer / Hour

   # Create a velocity
   speed_ms = MetersPerSecond(10)

   # Convert to km/h
   speed_kmh = speed_ms.convert(KilometersPerHour)
   print(speed_kmh.value)  # 36.0

   # Convert back
   back_to_ms = speed_kmh.convert(MetersPerSecond)
   print(back_to_ms.value)  # 10.0

Conversion Equality
-------------------

Units with the same physical quantity are equal:

.. code-block:: python

   from physities.src.unit import Meter, Kilometer

   assert Meter(1000) == Kilometer(1)  # True

   # This works with composite units too
   Ms = Meter / Second
   Kh = Kilometer / Hour

   assert Ms(10) == Kh(36)  # True (within floating-point precision)

Handling Conversion Errors
--------------------------

Attempting to convert between incompatible dimensions raises an error:

.. code-block:: python

   from physities.src.unit import Meter, Second
   from physities.src.exceptions import DimensionMismatchError

   try:
       distance = Meter(100)
       # Can't convert length to time
       time = distance.convert(Second)
   except DimensionMismatchError as e:
       print(e)
       # "Cannot perform conversion: dimensions do not match..."

Conversion in Calculations
--------------------------

Conversions happen automatically when operating on compatible units:

.. code-block:: python

   from physities.src.unit import Meter, Kilometer

   # Addition automatically converts
   total = Meter(500) + Kilometer(1)  # 1500 m

   # The result uses the first operand's scale
   print(total.value)  # 1500.0
   print(total.scale.conversion_factor)  # 1.0 (meter scale)

Custom Unit Conversion
----------------------

Create custom unit types and convert between them:

.. code-block:: python

   from physities.src.unit import Meter, Unit
   from physities.src.scale import Scale
   from physities.src.dimension import Dimension

   # Define a furlong (201.168 meters)
   Furlong = Meter * 201.168

   # Convert meters to furlongs
   distance = Meter(1000)
   furlongs = distance.convert(Furlong)
   print(f"{furlongs.value:.2f}")  # 4.97

   # Convert furlongs to meters
   distance2 = Furlong(10)
   meters = distance2.convert(Meter)
   print(meters.value)  # 2011.68

Conversion Factor Reference
---------------------------

Here are some common conversion factors:

**Length**

- 1 km = 1000 m
- 1 mile = 1609.344 m
- 1 foot = 0.3048 m
- 1 inch = 0.0254 m

**Time**

- 1 minute = 60 s
- 1 hour = 3600 s
- 1 day = 86400 s

**Mass**

- 1 kg = 1000 g
- 1 pound = 0.453592 kg
- 1 ounce = 0.0283495 kg

**Temperature**

Physities uses Kelvin as the base temperature unit. Celsius and Fahrenheit
conversions require offset handling (not yet supported).

Tips for Precision
------------------

1. **Use SI units for calculations**, convert for display:

   .. code-block:: python

      # Calculate in SI
      si_result = calculation_in_si()

      # Convert for human-readable output
      display_value = si_result.convert(HumanFriendlyUnit)

2. **Be aware of floating-point precision**:

   .. code-block:: python

      # Use approximate comparison
      import math
      assert math.isclose(value1.value, value2.value, rel_tol=1e-9)

3. **Chain conversions carefully**:

   .. code-block:: python

      # Multiple conversions can accumulate small errors
      result = (value
                .convert(UnitA)
                .convert(UnitB)
                .convert(UnitC))
