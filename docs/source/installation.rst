Installation
============

From PyPI
---------

The easiest way to install Physities is from PyPI:

.. code-block:: bash

   pip install physities

This will install pre-built wheels for most platforms.

From Source
-----------

Physities uses a hybrid Python/Rust architecture. To build from source, you'll
need both Python and Rust toolchains.

Prerequisites
^^^^^^^^^^^^^

1. **Python 3.11+**
2. **Rust toolchain**: Install from https://rustup.rs/

   .. code-block:: bash

      curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

3. **maturin**: Python/Rust build tool

   .. code-block:: bash

      pip install maturin

Building
^^^^^^^^

Clone the repository and build:

.. code-block:: bash

   git clone https://github.com/M4tus4l3m/physities.git
   cd physities
   maturin develop --release

For development with editable install:

.. code-block:: bash

   pip install -e ".[dev]"
   maturin develop

Optional Dependencies
---------------------

Physities has optional dependency groups:

.. code-block:: bash

   # Development dependencies (testing, linting)
   pip install physities[dev]

   # Benchmark dependencies
   pip install physities[benchmark]

   # Documentation dependencies
   pip install physities[docs]

   # All optional dependencies
   pip install physities[all]

Verifying Installation
----------------------

Test your installation:

.. code-block:: python

   from physities.src.unit import Meter, Second

   # Create a velocity
   velocity = (Meter / Second)(10)
   print(velocity)  # 10 (L¹ / t¹)

   # Convert to km/h
   from physities.src.unit import Kilometer, Hour
   kmh = velocity.convert(Kilometer / Hour)
   print(kmh.value)  # 36.0
