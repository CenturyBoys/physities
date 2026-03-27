Physities Documentation
=======================

.. image:: https://github.com/CenturyBoys/physities/actions/workflows/publish.yml/badge.svg
   :target: https://github.com/CenturyBoys/physities/actions/workflows/publish.yml
   :alt: CI

.. image:: https://codecov.io/gh/CenturyBoys/physities/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/CenturyBoys/physities
   :alt: codecov

.. image:: https://badge.fury.io/py/physities.svg
   :target: https://pypi.org/project/physities/
   :alt: PyPI

**Physities** is a high-performance Python library for representing and working with
physical quantities and units. It features dimensional analysis, unit conversion,
and mathematical operations on physical measurements, powered by a Rust core for
optimal performance.

Features
--------

- **Type-safe operations**: Automatic dimensional analysis prevents unit errors
- **Elegant syntax**: Create composite units with operators (``Meter / Second``)
- **Unit conversion**: Convert between compatible units with dimension checking
- **High performance**: Rust backend using ndarray for linear algebra
- **NumPy interoperability**: Works seamlessly with NumPy arrays

Quick Example
-------------

.. code-block:: python

   from physities.src.unit import Meter, Second, Kilometer, Hour

   # Create composite unit types
   MetersPerSecond = Meter / Second
   KilometersPerHour = Kilometer / Hour

   # Create values
   v1 = MetersPerSecond(40)      # 40 m/s
   v2 = KilometersPerHour(144)   # 144 km/h

   # Convert between units
   v3 = v2.convert(MetersPerSecond)  # 40 m/s

   # Comparison works across compatible units
   assert v1 == v2  # True: 40 m/s == 144 km/h

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   installation
   quickstart

.. toctree::
   :maxdepth: 2
   :caption: Tutorials

   tutorials/index
   tutorials/basic_usage
   tutorials/unit_conversion

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   api/index
   api/unit
   api/scale
   api/dimension

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
