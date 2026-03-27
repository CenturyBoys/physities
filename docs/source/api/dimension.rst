Dimension Module
================

.. module:: physities.src.dimension.dimension

The dimension module provides classes for representing physical dimensions.

BaseDimension
-------------

.. module:: physities.src.dimension.base_dimensions

.. autoclass:: BaseDimension
   :members:
   :show-inheritance:

The 7 SI base dimensions:

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Name
     - Value
     - Description
   * - ``LENGTH``
     - 0
     - Length (meters)
   * - ``MASS``
     - 1
     - Mass (kilograms)
   * - ``TEMPERATURE``
     - 2
     - Thermodynamic temperature (kelvin)
   * - ``TIME``
     - 3
     - Time (seconds)
   * - ``AMOUNT``
     - 4
     - Amount of substance (moles)
   * - ``ELECTRIC_CURRENT``
     - 5
     - Electric current (amperes)
   * - ``LUMINOUS_INTENSITY``
     - 6
     - Luminous intensity (candelas)

Dimension
---------

.. module:: physities.src.dimension.dimension

.. autoclass:: Dimension
   :members:
   :special-members: __add__, __sub__, __mul__, __eq__
   :show-inheritance:

Usage Examples
--------------

Creating Dimensions
^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from physities.src.dimension import Dimension

   # Using factory methods
   length = Dimension.new_length()
   time = Dimension.new_time()
   mass = Dimension.new_mass()

   # With power
   area = Dimension.new_length(power=2)  # L²
   inverse_time = Dimension.new_time(power=-1)  # T⁻¹

   # Dimensionless
   dimensionless = Dimension.new_dimensionless()

   # From tuple
   velocity = Dimension.new_instance((1, 0, 0, -1, 0, 0, 0))  # L/T

Dimension Operations
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from physities.src.dimension import Dimension

   length = Dimension.new_length()
   time = Dimension.new_time()

   # Addition combines exponents (for multiplication of quantities)
   velocity = length + (time * -1)  # L¹T⁻¹

   # Subtraction (for division of quantities)
   acceleration = velocity - time  # L¹T⁻²

   # Scalar multiplication (for powers)
   area = length * 2  # L²
   volume = length * 3  # L³

Accessing Dimension Properties
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from physities.src.dimension import Dimension

   # Create a force dimension (M·L·T⁻²)
   force = Dimension.new_instance((1, 1, 0, -2, 0, 0, 0))

   # Access individual exponents
   print(force.length)  # 1
   print(force.mass)    # 1
   print(force.time)    # -2

   # Get non-zero dimensions
   dims = force.get_dimensions()
   # [BaseDimension.LENGTH, BaseDimension.MASS, BaseDimension.TIME]

   # Display string
   print(force.show_dimension())  # "Lm / t²"

Common Derived Dimensions
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from physities.src.dimension import Dimension

   # Velocity: L/T
   velocity = Dimension.new_instance((1, 0, 0, -1, 0, 0, 0))

   # Acceleration: L/T²
   acceleration = Dimension.new_instance((1, 0, 0, -2, 0, 0, 0))

   # Force: M·L/T²
   force = Dimension.new_instance((1, 1, 0, -2, 0, 0, 0))

   # Energy: M·L²/T²
   energy = Dimension.new_instance((2, 1, 0, -2, 0, 0, 0))

   # Power: M·L²/T³
   power = Dimension.new_instance((2, 1, 0, -3, 0, 0, 0))

   # Pressure: M/(L·T²)
   pressure = Dimension.new_instance((-1, 1, 0, -2, 0, 0, 0))
