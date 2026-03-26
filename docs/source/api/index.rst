API Reference
=============

This section provides detailed API documentation for Physities.

Core Modules
------------

.. toctree::
   :maxdepth: 2

   unit
   scale
   dimension

Module Overview
---------------

**physities.src.unit**
    The main module for working with physical quantities. Contains the ``Unit``
    base class, ``MetaUnit`` metaclass, and pre-defined unit types like ``Meter``,
    ``Second``, ``Kilogram``, etc.

**physities.src.scale**
    Defines the ``Scale`` class that combines a ``Dimension`` with conversion
    factors for unit definitions.

**physities.src.dimension**
    Defines the ``Dimension`` class for representing physical dimensions and
    the ``BaseDimension`` enum for the 7 SI base dimensions.

**physities.src.exceptions**
    Custom exception classes for error handling:

    - ``PhysitiesError``: Base exception for all physities errors
    - ``DimensionMismatchError``: Incompatible dimensions in operation
    - ``InvalidConversionError``: Invalid unit conversion
    - ``InvalidOperationError``: Invalid arithmetic operation
    - ``InvalidPowerError``: Invalid power/exponent operation
