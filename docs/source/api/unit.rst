Unit Module
===========

.. module:: physities.src.unit.unit

The unit module provides the core classes for working with physical quantities.

MetaUnit
--------

.. autoclass:: MetaUnit
   :members:
   :special-members: __mul__, __truediv__, __pow__, __eq__
   :show-inheritance:

Unit
----

.. autoclass:: Unit
   :members:
   :special-members: __init__, __add__, __sub__, __mul__, __truediv__, __pow__, __eq__
   :show-inheritance:

Pre-defined Units
-----------------

The following units are available in ``physities.src.unit``:

Base SI Units
^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Unit
     - Dimension
     - Description
   * - ``Meter``
     - Length
     - SI base unit of length
   * - ``Kilogram``
     - Mass
     - SI base unit of mass
   * - ``Second``
     - Time
     - SI base unit of time
   * - ``Kelvin``
     - Temperature
     - SI base unit of temperature
   * - ``Ampere``
     - Electric Current
     - SI base unit of current
   * - ``Unity``
     - Amount
     - Dimensionless unit
   * - ``Candela``
     - Luminous Intensity
     - SI base unit of luminosity

Length Units
^^^^^^^^^^^^

``Gigameter``, ``Megameter``, ``Kilometer``, ``Hectometer``, ``Decameter``,
``Decimeter``, ``Centimeter``, ``Millimeter``, ``Micrometer``, ``Nanometer``,
``Foot``, ``Yard``, ``Inch``, ``Mile``, ``Furlong``, ``Rod``

Time Units
^^^^^^^^^^

``Nanosecond``, ``Microsecond``, ``Millisecond``, ``Centisecond``, ``Decisecond``,
``Minute``, ``Hour``, ``Day``, ``Week``, ``Month``, ``Year``, ``Decade``,
``Century``, ``Millennium``

Mass Units
^^^^^^^^^^

``Gigagram``, ``Megagram``, ``Tonne``, ``Hectogram``, ``Decagram``, ``Gram``,
``Decigram``, ``Centigram``, ``Milligram``, ``Microgram``, ``Nanogram``,
``Pound``, ``Ounce``, ``Stone``, ``Carat``, ``Grain``, ``Slug``

Area Units
^^^^^^^^^^

``Meter2``, ``Kilometer2``, ``Hectare``, ``Centimeter2``, ``Millimeter2``,
``Foot2``, ``Yard2``, ``Inch2``, ``Mile2``, ``Acre``

Volume Units
^^^^^^^^^^^^

``Meter3``, ``Liter``, ``Kiloliter``, ``Milliliter``, ``Centimeter3``,
``Foot3``, ``Gallon``, ``Pint``, ``Barrel``

Usage Examples
--------------

Creating and Using Units
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from physities.src.unit import Meter, Second, Kilogram

   # Simple quantities
   distance = Meter(100)
   time = Second(10)

   # Composite units
   Velocity = Meter / Second
   speed = Velocity(10)

   # Operations
   total_distance = distance + Meter(50)
   doubled = speed * 2

Unit Conversion
^^^^^^^^^^^^^^^

.. code-block:: python

   from physities.src.unit import Meter, Kilometer

   m = Meter(1000)
   km = m.convert(Kilometer)
   print(km.value)  # 1.0

Creating Custom Units
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from physities.src.unit import Meter, Unit
   from physities.src.scale import Scale
   from physities.src.dimension import Dimension

   # Using multiplication
   Furlong = Meter * 201.168

   # Using Scale directly
   class Angstrom(Unit):
       scale = Scale.new(
           dimension=Dimension.new_length(),
           from_base_scale_conversions=(1e-10, 1, 1, 1, 1, 1, 1),
       )
       value = None
