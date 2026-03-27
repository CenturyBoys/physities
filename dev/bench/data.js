window.BENCHMARK_DATA = {
  "lastUpdate": 1774570623593,
  "repoUrl": "https://github.com/CenturyBoys/physities",
  "entries": {
    "Physities Benchmarks": [
      {
        "commit": {
          "author": {
            "email": "im.ximit@gmail.com",
            "name": "Marco Sievers de Almeida",
            "username": "XimitGaia"
          },
          "committer": {
            "email": "im.ximit@gmail.com",
            "name": "Marco Sievers de Almeida",
            "username": "XimitGaia"
          },
          "distinct": true,
          "id": "e756516ab1c4768eda0bcc95827701275521ce5c",
          "message": "fix: remove skip-fetch-gh-pages now that branch exists\n\nThe gh-pages branch now exists, so we can fetch it normally\nto compare benchmark results.\n\nCo-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>",
          "timestamp": "2026-03-26T21:15:41-03:00",
          "tree_id": "5221dea67739293ba78ad664bf8144185871cf24",
          "url": "https://github.com/CenturyBoys/physities/commit/e756516ab1c4768eda0bcc95827701275521ce5c"
        },
        "date": 1774570622868,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/bench_conversions.py::TestConversionBenchmarks::test_simple_conversion",
            "value": 849582.9905485413,
            "unit": "iter/sec",
            "range": "stddev: 3.732227506320771e-7",
            "extra": "mean: 1.1770480472476743 usec\nrounds: 73282"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestConversionBenchmarks::test_composite_conversion",
            "value": 784969.6982857595,
            "unit": "iter/sec",
            "range": "stddev: 0.000001689461913569687",
            "extra": "mean: 1.2739345253502525 usec\nrounds: 98435"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestConversionBenchmarks::test_to_si_conversion",
            "value": 86054.52607286106,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014365849792084664",
            "extra": "mean: 11.620539274753721 usec\nrounds: 28848"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestConversionBenchmarks::test_repeated_conversion",
            "value": 419599.37154871324,
            "unit": "iter/sec",
            "range": "stddev: 0.0000010610463173841947",
            "extra": "mean: 2.3832256857513077 usec\nrounds: 101021"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestUnitCreationBenchmarks::test_simple_unit_creation",
            "value": 4969430.922921366,
            "unit": "iter/sec",
            "range": "stddev: 2.9052805343473775e-8",
            "extra": "mean: 201.2302848173956 nsec\nrounds: 193051"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestUnitCreationBenchmarks::test_composite_unit_type_creation",
            "value": 33651.984860747136,
            "unit": "iter/sec",
            "range": "stddev: 0.000036674328440173484",
            "extra": "mean: 29.715929213032407 usec\nrounds: 11358"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestUnitCreationBenchmarks::test_composite_unit_instance_creation",
            "value": 4854399.562647817,
            "unit": "iter/sec",
            "range": "stddev: 3.425614505378379e-8",
            "extra": "mean: 205.9987001676197 nsec\nrounds: 197278"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestUnitCreationBenchmarks::test_complex_unit_type_creation",
            "value": 11963.578730081352,
            "unit": "iter/sec",
            "range": "stddev: 0.000028996338244595444",
            "extra": "mean: 83.58702881150346 usec\nrounds: 5831"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestArithmeticBenchmarks::test_unit_addition",
            "value": 523329.82827350457,
            "unit": "iter/sec",
            "range": "stddev: 5.315482415150349e-7",
            "extra": "mean: 1.910840823461292 usec\nrounds: 102892"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestArithmeticBenchmarks::test_unit_subtraction",
            "value": 518767.4407191189,
            "unit": "iter/sec",
            "range": "stddev: 5.150107883138764e-7",
            "extra": "mean: 1.9276460346350828 usec\nrounds: 123077"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestArithmeticBenchmarks::test_unit_multiplication",
            "value": 39105.13666846284,
            "unit": "iter/sec",
            "range": "stddev: 0.000002374986360044416",
            "extra": "mean: 25.572088098760464 usec\nrounds: 8831"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestArithmeticBenchmarks::test_unit_division",
            "value": 38505.827080595496,
            "unit": "iter/sec",
            "range": "stddev: 0.000002685562332626011",
            "extra": "mean: 25.970095328868723 usec\nrounds: 19931"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestArithmeticBenchmarks::test_scalar_multiplication",
            "value": 1693555.1021965921,
            "unit": "iter/sec",
            "range": "stddev: 6.02888412443132e-8",
            "extra": "mean: 590.473849184444 nsec\nrounds: 77858"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestArithmeticBenchmarks::test_unit_power",
            "value": 69191.64816393585,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015244778462756773",
            "extra": "mean: 14.452611356080128 usec\nrounds: 21310"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestVsNumpyBenchmarks::test_numpy_scalar_add",
            "value": 7928121.540856908,
            "unit": "iter/sec",
            "range": "stddev: 1.6461926901304348e-8",
            "extra": "mean: 126.13328325588547 nsec\nrounds: 191205"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestVsNumpyBenchmarks::test_physities_scalar_add",
            "value": 527429.9137769921,
            "unit": "iter/sec",
            "range": "stddev: 5.697453490805845e-7",
            "extra": "mean: 1.8959865071718702 usec\nrounds: 85823"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestVsNumpyBenchmarks::test_numpy_scalar_mul",
            "value": 8077954.226327009,
            "unit": "iter/sec",
            "range": "stddev: 1.6930898180797236e-8",
            "extra": "mean: 123.79371954608891 nsec\nrounds: 198453"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestVsNumpyBenchmarks::test_physities_scalar_mul",
            "value": 1345833.9642015598,
            "unit": "iter/sec",
            "range": "stddev: 2.825664148303748e-7",
            "extra": "mean: 743.0337074256169 nsec\nrounds: 186220"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestVsNumpyBenchmarks::test_numpy_scalar_power",
            "value": 6655352.851200906,
            "unit": "iter/sec",
            "range": "stddev: 1.9532146763282253e-8",
            "extra": "mean: 150.25499359059643 nsec\nrounds: 198060"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestVsNumpyBenchmarks::test_physities_scalar_power",
            "value": 65951.35216198857,
            "unit": "iter/sec",
            "range": "stddev: 0.000003827020100456573",
            "extra": "mean: 15.162691396285815 usec\nrounds: 22537"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestBatchOperationsBenchmarks::test_numpy_batch_add_100",
            "value": 1412503.7044455567,
            "unit": "iter/sec",
            "range": "stddev: 2.631221317294663e-7",
            "extra": "mean: 707.96274505526 nsec\nrounds: 193424"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestBatchOperationsBenchmarks::test_physities_batch_add_100",
            "value": 6039.588211004899,
            "unit": "iter/sec",
            "range": "stddev: 0.000005661896691406794",
            "extra": "mean: 165.57420225734475 usec\nrounds: 5671"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestBatchOperationsBenchmarks::test_numpy_batch_mul_100",
            "value": 961463.1511226685,
            "unit": "iter/sec",
            "range": "stddev: 1.495392897111767e-7",
            "extra": "mean: 1.0400814621260575 usec\nrounds: 172981"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestBatchOperationsBenchmarks::test_physities_batch_mul_100",
            "value": 20521.565621416656,
            "unit": "iter/sec",
            "range": "stddev: 0.000003111065209820675",
            "extra": "mean: 48.72922555949547 usec\nrounds: 15814"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestBatchOperationsBenchmarks::test_numpy_batch_conversion_100",
            "value": 1029490.9685489498,
            "unit": "iter/sec",
            "range": "stddev: 3.5240745488999117e-7",
            "extra": "mean: 971.3538346135113 nsec\nrounds: 108969"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestBatchOperationsBenchmarks::test_physities_batch_conversion_100",
            "value": 10566.556686570313,
            "unit": "iter/sec",
            "range": "stddev: 0.00000534214459741031",
            "extra": "mean: 94.6382089892123 usec\nrounds: 9144"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_plain_python_addition",
            "value": 3273966.353720003,
            "unit": "iter/sec",
            "range": "stddev: 6.508170516952912e-8",
            "extra": "mean: 305.43991353600273 nsec\nrounds: 149656"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_physities_addition",
            "value": 526287.8003545565,
            "unit": "iter/sec",
            "range": "stddev: 6.333558666086349e-7",
            "extra": "mean: 1.900101046093614 usec\nrounds: 86416"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_plain_python_multiplication",
            "value": 2070708.7058589102,
            "unit": "iter/sec",
            "range": "stddev: 5.14529147357727e-8",
            "extra": "mean: 482.92644792122303 nsec\nrounds: 77197"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_physities_multiplication",
            "value": 39711.15350284306,
            "unit": "iter/sec",
            "range": "stddev: 0.0000028965389211288652",
            "extra": "mean: 25.18184217258777 usec\nrounds: 13293"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_plain_python_conversion",
            "value": 8748113.003772039,
            "unit": "iter/sec",
            "range": "stddev: 7.732644772711215e-9",
            "extra": "mean: 114.31036608338619 nsec\nrounds: 45723"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_physities_conversion",
            "value": 835091.1816833358,
            "unit": "iter/sec",
            "range": "stddev: 4.3751798130613893e-7",
            "extra": "mean: 1.1974740267095731 usec\nrounds: 101431"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_plain_python_power",
            "value": 2243550.437625739,
            "unit": "iter/sec",
            "range": "stddev: 5.355379791817045e-8",
            "extra": "mean: 445.7220944220206 nsec\nrounds: 93897"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_physities_power",
            "value": 69116.91739994769,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015850922224000533",
            "extra": "mean: 14.468237844194666 usec\nrounds: 22191"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_plain_python_chain",
            "value": 772107.9188665955,
            "unit": "iter/sec",
            "range": "stddev: 4.3317304673878536e-7",
            "extra": "mean: 1.2951557360892443 usec\nrounds: 126663"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_physities_chain",
            "value": 36013.5604994159,
            "unit": "iter/sec",
            "range": "stddev: 0.000002948551781381317",
            "extra": "mean: 27.767318369318662 usec\nrounds: 12118"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestCreationOverheadBenchmarks::test_plain_dataclass_creation",
            "value": 4731039.91578676,
            "unit": "iter/sec",
            "range": "stddev: 2.957864897299043e-8",
            "extra": "mean: 211.37001965744835 nsec\nrounds: 192716"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestCreationOverheadBenchmarks::test_physities_unit_creation",
            "value": 4986529.231977189,
            "unit": "iter/sec",
            "range": "stddev: 3.616405170507854e-8",
            "extra": "mean: 200.54028633526647 nsec\nrounds: 179824"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestCreationOverheadBenchmarks::test_plain_float_operation",
            "value": 11491063.303827696,
            "unit": "iter/sec",
            "range": "stddev: 9.122174020975722e-9",
            "extra": "mean: 87.02414855438124 nsec\nrounds: 115527"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestCreationOverheadBenchmarks::test_physities_unit_operation",
            "value": 524585.1315856572,
            "unit": "iter/sec",
            "range": "stddev: 4.817087910569636e-7",
            "extra": "mean: 1.906268286669338 usec\nrounds: 80496"
          }
        ]
      }
    ]
  }
}