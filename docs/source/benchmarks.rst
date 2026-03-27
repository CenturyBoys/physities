Benchmarks
==========

Performance tracking for physities operations.

`View Interactive Charts </dev/bench/>`_

Understanding the Results
-------------------------

The benchmarks compare **physities** (with unit safety) against **plain Python** (raw floats).

**Values are in iterations/second** - higher is faster.

What's Being Measured
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 30 35 35

   * - Benchmark
     - Plain Python
     - Physities
   * - **Add**
     - ``100.0 + 200.0``
     - ``Meter(100) + Meter(200)``
   * - **Multiply**
     - ``10.0 * 5.0``
     - ``Meter(10) * Second(5)``
   * - **Divide**
     - ``100.0 / 10.0``
     - ``Meter(100) / Second(10)``
   * - **Convert**
     - ``value / 1000``
     - ``m.convert(Kilometer)``

Expected Overhead
~~~~~~~~~~~~~~~~~

Physities adds overhead for unit safety:

- **Simple operations** (add, multiply): ~10-50x slower than raw floats
- **Conversions**: ~10x slower than manual math
- **Unit creation**: ~200 nanoseconds per instance

This overhead is the cost of:

- Dimensional analysis (preventing ``Meter + Second``)
- Automatic conversion factors
- Type-safe operations

When It Matters
~~~~~~~~~~~~~~~

For most applications, this overhead is negligible:

- **Scientific calculations**: Usually I/O or algorithm bound, not arithmetic
- **Data pipelines**: The safety prevents costly bugs
- **Simulations**: Consider using NumPy arrays with physities for batch operations

The overhead becomes noticeable only in tight loops doing millions of operations per second.

Running Benchmarks Locally
--------------------------

.. code-block:: bash

   # Install benchmark dependencies
   pip install pytest-benchmark

   # Run core benchmarks
   pytest benchmarks/bench_core.py --benchmark-only

   # Run all detailed benchmarks
   pytest benchmarks/ --benchmark-only

   # Compare against previous run
   pytest benchmarks/ --benchmark-only --benchmark-compare
