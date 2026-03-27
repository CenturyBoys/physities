Scale Module
============

.. module:: physities.src.scale.scale

The scale module provides the ``Scale`` class for defining unit conversion factors.

Scale
-----

.. autoclass:: Scale
   :members:
   :special-members: __mul__, __truediv__, __pow__, __eq__
   :show-inheritance:

Usage Examples
--------------

Creating Scales
^^^^^^^^^^^^^^^

.. code-block:: python

   from physities.src.scale import Scale
   from physities.src.dimension import Dimension

   # SI meter scale (conversion factor = 1)
   meter_scale = Scale.new(dimension=Dimension.new_length())

   # Kilometer scale (1 km = 1000 m)
   km_scale = Scale.new(
       dimension=Dimension.new_length(),
       from_base_scale_conversions=(1000, 1, 1, 1, 1, 1, 1),
   )

   print(km_scale.conversion_factor)  # 1000.0

Scale Operations
^^^^^^^^^^^^^^^^

.. code-block:: python

   from physities.src.scale import Scale
   from physities.src.dimension import Dimension

   meter = Scale.new(dimension=Dimension.new_length())
   second = Scale.new(dimension=Dimension.new_time())

   # Combine scales
   velocity = meter / second  # m/s scale
   print(velocity.dimension.length)  # 1
   print(velocity.dimension.time)    # -1

   # Scale multiplication
   kilometer = meter * 1000
   print(kilometer.conversion_factor)  # 1000.0

   # Scale power
   area = meter ** 2
   print(area.dimension.length)  # 2

Checking Dimensionless
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from physities.src.scale import Scale
   from physities.src.dimension import Dimension

   # Dimensionless scale
   dimensionless = Scale.new()
   print(dimensionless.is_dimensionless)  # True

   # Length scale
   meter = Scale.new(dimension=Dimension.new_length())
   print(meter.is_dimensionless)  # False

   # Division produces dimensionless
   ratio = meter / meter
   print(ratio.is_dimensionless)  # True
