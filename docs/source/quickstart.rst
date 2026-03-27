Quickstart
==========

This guide covers the basics of using Physities for physical quantity calculations.

Creating Units
--------------

Physities provides pre-defined base units that you can use directly or combine
to create composite units:

.. code-block:: python

   from physities.src.unit import Meter, Second, Kilogram, Kelvin

   # Create simple quantities
   distance = Meter(100)
   time = Second(10)
   mass = Kilogram(5)

Composite Units
---------------

Create composite unit types using arithmetic operators:

.. code-block:: python

   from physities.src.unit import Meter, Second, Kilogram

   # Velocity: length / time
   Velocity = Meter / Second
   speed = Velocity(10)  # 10 m/s

   # Acceleration: length / time^2
   Acceleration = Meter / (Second ** 2)
   accel = Acceleration(9.8)  # 9.8 m/s²

   # Force (Newton): mass * length / time^2
   Newton = Kilogram * Meter / (Second ** 2)
   force = Newton(100)  # 100 N

Unit Conversion
---------------

Convert between units of the same dimension:

.. code-block:: python

   from physities.src.unit import Meter, Kilometer, Second, Hour

   # Define unit types
   Ms = Meter / Second
   Kh = Kilometer / Hour

   # Create and convert
   speed_ms = Ms(10)           # 10 m/s
   speed_kh = speed_ms.convert(Kh)  # 36 km/h

   # Convert to SI base units
   km = Kilometer(5)
   m = km.to_si()  # 5000 m

Arithmetic Operations
---------------------

Perform arithmetic with proper dimensional handling:

.. code-block:: python

   from physities.src.unit import Meter, Second

   # Addition and subtraction (same units only)
   d1 = Meter(100)
   d2 = Meter(50)
   total = d1 + d2   # 150 m
   diff = d1 - d2    # 50 m

   # Multiplication creates new dimensions
   length = Meter(10)
   time = Second(5)
   velocity = length / time  # 2 m/s

   # Scalar multiplication
   doubled = velocity * 2  # 4 m/s

   # Powers
   area = Meter(10) ** 2  # 100 m²

Unit Equality
-------------

Units with the same physical quantity are equal, regardless of scale:

.. code-block:: python

   from physities.src.unit import Meter, Kilometer

   assert Meter(1000) == Kilometer(1)  # True
   assert Meter(500) + Meter(500) == Kilometer(1)  # True

Error Handling
--------------

Physities prevents invalid operations with descriptive exceptions:

.. code-block:: python

   from physities.src.unit import Meter, Second
   from physities.src.exceptions import DimensionMismatchError

   try:
       # Can't add different dimensions
       Meter(10) + Second(5)
   except DimensionMismatchError as e:
       print(e)  # "Cannot perform addition: dimensions do not match..."

Available Units
---------------

Physities includes many pre-defined units:

**Length**: Meter, Kilometer, Centimeter, Millimeter, Foot, Yard, Mile, Inch, etc.

**Time**: Second, Minute, Hour, Day, Week, Month, Year, Millisecond, etc.

**Mass**: Kilogram, Gram, Milligram, Tonne, Pound, Ounce, etc.

**Temperature**: Kelvin

**Electric Current**: Ampere, Milliampere, etc.

**Amount**: Unity, Moles, Dozen, etc.

**Area**: Meter2, Kilometer2, Hectare, etc.

**Volume**: Meter3, Liter, Milliliter, Gallon, etc.

Import them from ``physities.src.unit``:

.. code-block:: python

   from physities.src.unit import (
       Meter, Kilometer, Mile,
       Second, Hour,
       Kilogram, Gram, Pound,
       Kelvin,
       Ampere,
       # ... and more
   )
