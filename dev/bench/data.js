window.BENCHMARK_DATA = {
  "lastUpdate": 1774576901385,
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
      },
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
          "id": "21f7243bcad72e1a3a72e6de0b7d16ef26034f50",
          "message": "fix: include benchmark data in docs deployment\n\nFetch benchmark charts from gh-pages branch and include them\nin the Sphinx docs build so they're accessible at /dev/bench/\n\nCo-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>",
          "timestamp": "2026-03-26T21:29:42-03:00",
          "tree_id": "d0779dc8e8de54030686c8116679ac96842bbc74",
          "url": "https://github.com/CenturyBoys/physities/commit/21f7243bcad72e1a3a72e6de0b7d16ef26034f50"
        },
        "date": 1774571461229,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/bench_conversions.py::TestConversionBenchmarks::test_simple_conversion",
            "value": 899148.2821928114,
            "unit": "iter/sec",
            "range": "stddev: 3.0290214806256286e-7",
            "extra": "mean: 1.1121636106129624 usec\nrounds: 55736"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestConversionBenchmarks::test_composite_conversion",
            "value": 851789.3367217788,
            "unit": "iter/sec",
            "range": "stddev: 4.531554419467555e-7",
            "extra": "mean: 1.1739992001409985 usec\nrounds: 156275"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestConversionBenchmarks::test_to_si_conversion",
            "value": 94625.62884046447,
            "unit": "iter/sec",
            "range": "stddev: 8.095882720194142e-7",
            "extra": "mean: 10.567961473587301 usec\nrounds: 30265"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestConversionBenchmarks::test_repeated_conversion",
            "value": 421166.27209903573,
            "unit": "iter/sec",
            "range": "stddev: 4.568326831275303e-7",
            "extra": "mean: 2.3743591693991433 usec\nrounds: 131857"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestUnitCreationBenchmarks::test_simple_unit_creation",
            "value": 4677743.034173653,
            "unit": "iter/sec",
            "range": "stddev: 2.0492295398977794e-8",
            "extra": "mean: 213.7783099016871 nsec\nrounds: 192013"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestUnitCreationBenchmarks::test_composite_unit_type_creation",
            "value": 39504.76484775629,
            "unit": "iter/sec",
            "range": "stddev: 0.000053603973687009575",
            "extra": "mean: 25.31340216436691 usec\nrounds: 12475"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestUnitCreationBenchmarks::test_composite_unit_instance_creation",
            "value": 4629603.779094707,
            "unit": "iter/sec",
            "range": "stddev: 2.1988437138282812e-8",
            "extra": "mean: 216.001206089291 nsec\nrounds: 196503"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestUnitCreationBenchmarks::test_complex_unit_type_creation",
            "value": 13878.760614127912,
            "unit": "iter/sec",
            "range": "stddev: 0.00003343841862224477",
            "extra": "mean: 72.05254329281016 usec\nrounds: 6687"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestArithmeticBenchmarks::test_unit_addition",
            "value": 546308.125664888,
            "unit": "iter/sec",
            "range": "stddev: 7.023450776272975e-7",
            "extra": "mean: 1.8304688380443608 usec\nrounds: 99384"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestArithmeticBenchmarks::test_unit_subtraction",
            "value": 528953.7872315574,
            "unit": "iter/sec",
            "range": "stddev: 3.673120758562454e-7",
            "extra": "mean: 1.890524322046748 usec\nrounds: 103692"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestArithmeticBenchmarks::test_unit_multiplication",
            "value": 46879.37011728721,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017115397270051083",
            "extra": "mean: 21.331344629804242 usec\nrounds: 11508"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestArithmeticBenchmarks::test_unit_division",
            "value": 43206.51382753464,
            "unit": "iter/sec",
            "range": "stddev: 0.0000019009102492935284",
            "extra": "mean: 23.144658326095268 usec\nrounds: 17265"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestArithmeticBenchmarks::test_scalar_multiplication",
            "value": 1499967.2603952915,
            "unit": "iter/sec",
            "range": "stddev: 1.9305053168725635e-7",
            "extra": "mean: 666.6812179196942 nsec\nrounds: 188254"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestArithmeticBenchmarks::test_unit_power",
            "value": 76380.4721339506,
            "unit": "iter/sec",
            "range": "stddev: 0.0000019945670967839785",
            "extra": "mean: 13.09235164514657 usec\nrounds: 24374"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestVsNumpyBenchmarks::test_numpy_scalar_add",
            "value": 9710558.392365977,
            "unit": "iter/sec",
            "range": "stddev: 2.1582884198821044e-8",
            "extra": "mean: 102.98068963638545 nsec\nrounds: 198926"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestVsNumpyBenchmarks::test_physities_scalar_add",
            "value": 545730.4846692289,
            "unit": "iter/sec",
            "range": "stddev: 4.830658735711616e-7",
            "extra": "mean: 1.8324063399282287 usec\nrounds: 89654"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestVsNumpyBenchmarks::test_numpy_scalar_mul",
            "value": 9624883.784454986,
            "unit": "iter/sec",
            "range": "stddev: 1.0483121984030151e-8",
            "extra": "mean: 103.8973583883784 nsec\nrounds: 199961"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestVsNumpyBenchmarks::test_physities_scalar_mul",
            "value": 1508690.908605323,
            "unit": "iter/sec",
            "range": "stddev: 1.9036375742934752e-7",
            "extra": "mean: 662.8262915194662 nsec\nrounds: 182150"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestVsNumpyBenchmarks::test_numpy_scalar_power",
            "value": 4397366.787574614,
            "unit": "iter/sec",
            "range": "stddev: 1.2924910633125916e-7",
            "extra": "mean: 227.40882175797623 nsec\nrounds: 199801"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestVsNumpyBenchmarks::test_physities_scalar_power",
            "value": 76607.58487109652,
            "unit": "iter/sec",
            "range": "stddev: 8.614638848782071e-7",
            "extra": "mean: 13.053537736278287 usec\nrounds: 23651"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestBatchOperationsBenchmarks::test_numpy_batch_add_100",
            "value": 1854597.6884715527,
            "unit": "iter/sec",
            "range": "stddev: 3.807629591349757e-8",
            "extra": "mean: 539.2004995024773 nsec\nrounds: 85485"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestBatchOperationsBenchmarks::test_physities_batch_add_100",
            "value": 6379.650900299849,
            "unit": "iter/sec",
            "range": "stddev: 0.000004168482936743626",
            "extra": "mean: 156.74838884256175 usec\nrounds: 6005"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestBatchOperationsBenchmarks::test_numpy_batch_mul_100",
            "value": 1079963.6483324177,
            "unit": "iter/sec",
            "range": "stddev: 1.0764201820459275e-7",
            "extra": "mean: 925.9570926707602 nsec\nrounds: 53802"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestBatchOperationsBenchmarks::test_physities_batch_mul_100",
            "value": 22048.80406431324,
            "unit": "iter/sec",
            "range": "stddev: 0.0000021796257347630384",
            "extra": "mean: 45.35393380444316 usec\nrounds: 16557"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestBatchOperationsBenchmarks::test_numpy_batch_conversion_100",
            "value": 1170469.3407748104,
            "unit": "iter/sec",
            "range": "stddev: 1.8508061290496514e-7",
            "extra": "mean: 854.3581323864788 nsec\nrounds: 132962"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestBatchOperationsBenchmarks::test_physities_batch_conversion_100",
            "value": 11006.720793785504,
            "unit": "iter/sec",
            "range": "stddev: 0.0000028245873069799844",
            "extra": "mean: 90.85358107426595 usec\nrounds: 7894"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_plain_python_addition",
            "value": 3291814.2610046,
            "unit": "iter/sec",
            "range": "stddev: 2.848916174817577e-8",
            "extra": "mean: 303.783847055459 nsec\nrounds: 102260"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_physities_addition",
            "value": 547792.954086783,
            "unit": "iter/sec",
            "range": "stddev: 5.79952126902966e-7",
            "extra": "mean: 1.825507233233922 usec\nrounds: 90761"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_plain_python_multiplication",
            "value": 2139582.367380457,
            "unit": "iter/sec",
            "range": "stddev: 3.4910708411773216e-8",
            "extra": "mean: 467.38093155268945 nsec\nrounds: 80822"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_physities_multiplication",
            "value": 47102.17839287501,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013776807692788568",
            "extra": "mean: 21.230440589373394 usec\nrounds: 14728"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_plain_python_conversion",
            "value": 9920305.278674603,
            "unit": "iter/sec",
            "range": "stddev: 5.866652705742888e-9",
            "extra": "mean: 100.80334948458433 nsec\nrounds: 52030"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_physities_conversion",
            "value": 897741.115856202,
            "unit": "iter/sec",
            "range": "stddev: 2.924396798176656e-7",
            "extra": "mean: 1.1139068739725382 usec\nrounds: 119247"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_plain_python_power",
            "value": 2327817.9770421283,
            "unit": "iter/sec",
            "range": "stddev: 3.543112552687926e-8",
            "extra": "mean: 429.5868533804636 nsec\nrounds: 96386"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_physities_power",
            "value": 77486.76101453223,
            "unit": "iter/sec",
            "range": "stddev: 8.978826060284649e-7",
            "extra": "mean: 12.905430384584733 usec\nrounds: 23716"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_plain_python_chain",
            "value": 820798.2271341081,
            "unit": "iter/sec",
            "range": "stddev: 3.058340015305503e-7",
            "extra": "mean: 1.2183262182370826 usec\nrounds: 130192"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_physities_chain",
            "value": 40590.59900940027,
            "unit": "iter/sec",
            "range": "stddev: 0.0000015808571067303641",
            "extra": "mean: 24.636246431554575 usec\nrounds: 14012"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestCreationOverheadBenchmarks::test_plain_dataclass_creation",
            "value": 4491732.710957137,
            "unit": "iter/sec",
            "range": "stddev: 2.045070699126195e-8",
            "extra": "mean: 222.63123483741313 nsec\nrounds: 196812"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestCreationOverheadBenchmarks::test_physities_unit_creation",
            "value": 4672609.895182653,
            "unit": "iter/sec",
            "range": "stddev: 2.3438862512465e-8",
            "extra": "mean: 214.0131580492114 nsec\nrounds: 186707"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestCreationOverheadBenchmarks::test_plain_float_operation",
            "value": 13098091.856327632,
            "unit": "iter/sec",
            "range": "stddev: 6.2356853092542975e-9",
            "extra": "mean: 76.34699855283421 nsec\nrounds: 130617"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestCreationOverheadBenchmarks::test_physities_unit_operation",
            "value": 547419.5312866856,
            "unit": "iter/sec",
            "range": "stddev: 3.291002355908712e-7",
            "extra": "mean: 1.8267525048833093 usec\nrounds: 37427"
          }
        ]
      },
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
          "id": "2b8acbf0dc0b43b4036b1dc7789f0c4cfa5b60ea",
          "message": "fix: update GitHub URLs from M4tus4l3m to CenturyBoys\n\nUpdate all repository references to point to the correct\nCenturyBoys/physities repository.\n\nCo-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>",
          "timestamp": "2026-03-26T21:32:09-03:00",
          "tree_id": "a865c34cb9b9f68bb609ab7cdc59ccea0cfc2051",
          "url": "https://github.com/CenturyBoys/physities/commit/2b8acbf0dc0b43b4036b1dc7789f0c4cfa5b60ea"
        },
        "date": 1774571608281,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/bench_conversions.py::TestConversionBenchmarks::test_simple_conversion",
            "value": 849427.9490628872,
            "unit": "iter/sec",
            "range": "stddev: 4.0771403135397385e-7",
            "extra": "mean: 1.177262887456468 usec\nrounds: 34646"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestConversionBenchmarks::test_composite_conversion",
            "value": 800258.1810543921,
            "unit": "iter/sec",
            "range": "stddev: 4.5499800677595704e-7",
            "extra": "mean: 1.2495967222508555 usec\nrounds: 187935"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestConversionBenchmarks::test_to_si_conversion",
            "value": 86051.51766186598,
            "unit": "iter/sec",
            "range": "stddev: 0.0000013628339777740795",
            "extra": "mean: 11.620945535550426 usec\nrounds: 32535"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestConversionBenchmarks::test_repeated_conversion",
            "value": 409478.837578326,
            "unit": "iter/sec",
            "range": "stddev: 6.297423308871804e-7",
            "extra": "mean: 2.4421286480005646 usec\nrounds: 135999"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestUnitCreationBenchmarks::test_simple_unit_creation",
            "value": 4983564.137931518,
            "unit": "iter/sec",
            "range": "stddev: 3.146614416314953e-8",
            "extra": "mean: 200.65960271056844 nsec\nrounds: 195695"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestUnitCreationBenchmarks::test_composite_unit_type_creation",
            "value": 34457.912848108106,
            "unit": "iter/sec",
            "range": "stddev: 0.000038488782697358004",
            "extra": "mean: 29.020910361229397 usec\nrounds: 14670"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestUnitCreationBenchmarks::test_composite_unit_instance_creation",
            "value": 4843417.9411577135,
            "unit": "iter/sec",
            "range": "stddev: 3.2816192449099095e-8",
            "extra": "mean: 206.46576697466278 nsec\nrounds: 199243"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestUnitCreationBenchmarks::test_complex_unit_type_creation",
            "value": 12162.222442860198,
            "unit": "iter/sec",
            "range": "stddev: 0.00003047307345073384",
            "extra": "mean: 82.22181469695512 usec\nrounds: 6913"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestArithmeticBenchmarks::test_unit_addition",
            "value": 521162.94541268406,
            "unit": "iter/sec",
            "range": "stddev: 5.379760852125573e-7",
            "extra": "mean: 1.9187856865152753 usec\nrounds: 103008"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestArithmeticBenchmarks::test_unit_subtraction",
            "value": 522530.0966779267,
            "unit": "iter/sec",
            "range": "stddev: 5.716015258504977e-7",
            "extra": "mean: 1.9137653627181836 usec\nrounds: 133798"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestArithmeticBenchmarks::test_unit_multiplication",
            "value": 39812.568917071374,
            "unit": "iter/sec",
            "range": "stddev: 0.0000024596153007126344",
            "extra": "mean: 25.117695923691237 usec\nrounds: 14891"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestArithmeticBenchmarks::test_unit_division",
            "value": 38184.93344072229,
            "unit": "iter/sec",
            "range": "stddev: 0.0000027198890123716954",
            "extra": "mean: 26.18833948086841 usec\nrounds: 20496"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestArithmeticBenchmarks::test_scalar_multiplication",
            "value": 1709422.322993397,
            "unit": "iter/sec",
            "range": "stddev: 6.127867417299298e-8",
            "extra": "mean: 584.9929455986355 nsec\nrounds: 77682"
          },
          {
            "name": "benchmarks/bench_conversions.py::TestArithmeticBenchmarks::test_unit_power",
            "value": 70509.1019567986,
            "unit": "iter/sec",
            "range": "stddev: 0.0000017310073333983393",
            "extra": "mean: 14.182566111999366 usec\nrounds: 28966"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestVsNumpyBenchmarks::test_numpy_scalar_add",
            "value": 7833520.069719553,
            "unit": "iter/sec",
            "range": "stddev: 1.829349028514628e-8",
            "extra": "mean: 127.65653130389057 nsec\nrounds: 197629"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestVsNumpyBenchmarks::test_physities_scalar_add",
            "value": 517043.5900736478,
            "unit": "iter/sec",
            "range": "stddev: 5.387034348242398e-7",
            "extra": "mean: 1.9340729083549024 usec\nrounds: 106531"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestVsNumpyBenchmarks::test_numpy_scalar_mul",
            "value": 8224913.425345542,
            "unit": "iter/sec",
            "range": "stddev: 1.4473537475120974e-8",
            "extra": "mean: 121.58182685771372 nsec\nrounds: 80685"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestVsNumpyBenchmarks::test_physities_scalar_mul",
            "value": 1738066.672951316,
            "unit": "iter/sec",
            "range": "stddev: 6.603583431925473e-8",
            "extra": "mean: 575.3519215130449 nsec\nrounds: 79911"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestVsNumpyBenchmarks::test_numpy_scalar_power",
            "value": 6713229.202537203,
            "unit": "iter/sec",
            "range": "stddev: 2.1696982479201783e-8",
            "extra": "mean: 148.95960942633266 nsec\nrounds: 196890"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestVsNumpyBenchmarks::test_physities_scalar_power",
            "value": 70757.26911172531,
            "unit": "iter/sec",
            "range": "stddev: 0.000001643475135808701",
            "extra": "mean: 14.132823560799187 usec\nrounds: 22461"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestBatchOperationsBenchmarks::test_numpy_batch_add_100",
            "value": 1443461.375678872,
            "unit": "iter/sec",
            "range": "stddev: 2.816418652452416e-7",
            "extra": "mean: 692.7791881716902 nsec\nrounds: 187970"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestBatchOperationsBenchmarks::test_physities_batch_add_100",
            "value": 6011.0672347381715,
            "unit": "iter/sec",
            "range": "stddev: 0.000007308573380346905",
            "extra": "mean: 166.3598094895636 usec\nrounds: 5543"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestBatchOperationsBenchmarks::test_numpy_batch_mul_100",
            "value": 966591.2465222961,
            "unit": "iter/sec",
            "range": "stddev: 1.7101914742755868e-7",
            "extra": "mean: 1.0345634761311069 usec\nrounds: 176679"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestBatchOperationsBenchmarks::test_physities_batch_mul_100",
            "value": 20381.561893573966,
            "unit": "iter/sec",
            "range": "stddev: 0.000003081447588332949",
            "extra": "mean: 49.06395325449943 usec\nrounds: 11830"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestBatchOperationsBenchmarks::test_numpy_batch_conversion_100",
            "value": 1028558.568734223,
            "unit": "iter/sec",
            "range": "stddev: 3.6292239197962273e-7",
            "extra": "mean: 972.2343776987167 nsec\nrounds: 121125"
          },
          {
            "name": "benchmarks/bench_vs_numpy.py::TestBatchOperationsBenchmarks::test_physities_batch_conversion_100",
            "value": 10268.136642976839,
            "unit": "iter/sec",
            "range": "stddev: 0.000004049413025697898",
            "extra": "mean: 97.388653342861 usec\nrounds: 8256"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_plain_python_addition",
            "value": 3262277.125941975,
            "unit": "iter/sec",
            "range": "stddev: 6.352375225537002e-8",
            "extra": "mean: 306.5343505148412 nsec\nrounds: 155232"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_physities_addition",
            "value": 521836.6818473829,
            "unit": "iter/sec",
            "range": "stddev: 5.831866320616779e-7",
            "extra": "mean: 1.916308367705859 usec\nrounds: 119818"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_plain_python_multiplication",
            "value": 2079486.1821657969,
            "unit": "iter/sec",
            "range": "stddev: 5.347682044095074e-8",
            "extra": "mean: 480.88802348206536 nsec\nrounds: 78107"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_physities_multiplication",
            "value": 40061.664734553015,
            "unit": "iter/sec",
            "range": "stddev: 0.0000026494481627279304",
            "extra": "mean: 24.96151886413008 usec\nrounds: 14472"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_plain_python_conversion",
            "value": 8867428.878842043,
            "unit": "iter/sec",
            "range": "stddev: 1.0981889852774707e-8",
            "extra": "mean: 112.77226055745604 nsec\nrounds: 89040"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_physities_conversion",
            "value": 828499.3067842128,
            "unit": "iter/sec",
            "range": "stddev: 6.348104297015466e-7",
            "extra": "mean: 1.207001613412883 usec\nrounds: 153093"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_plain_python_power",
            "value": 2295604.8679641243,
            "unit": "iter/sec",
            "range": "stddev: 5.5319414398562804e-8",
            "extra": "mean: 435.6150372197488 nsec\nrounds: 93897"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_physities_power",
            "value": 70742.18392244376,
            "unit": "iter/sec",
            "range": "stddev: 0.0000016096846812951946",
            "extra": "mean: 14.135837269263872 usec\nrounds: 24052"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_plain_python_chain",
            "value": 790525.4127669546,
            "unit": "iter/sec",
            "range": "stddev: 4.6879572256430453e-7",
            "extra": "mean: 1.264981471626388 usec\nrounds: 145075"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestVsPlainPythonBenchmarks::test_physities_chain",
            "value": 36429.7440576184,
            "unit": "iter/sec",
            "range": "stddev: 0.000002643308532383316",
            "extra": "mean: 27.450096778565594 usec\nrounds: 15241"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestCreationOverheadBenchmarks::test_plain_dataclass_creation",
            "value": 4819545.455452917,
            "unit": "iter/sec",
            "range": "stddev: 3.094348343082066e-8",
            "extra": "mean: 207.48844662699585 nsec\nrounds: 198060"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestCreationOverheadBenchmarks::test_physities_unit_creation",
            "value": 5014834.078269898,
            "unit": "iter/sec",
            "range": "stddev: 2.7377601293398767e-8",
            "extra": "mean: 199.4083920605282 nsec\nrounds: 194970"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestCreationOverheadBenchmarks::test_plain_float_operation",
            "value": 11489899.281883068,
            "unit": "iter/sec",
            "range": "stddev: 9.563210921415098e-9",
            "extra": "mean: 87.03296482126287 nsec\nrounds: 112398"
          },
          {
            "name": "benchmarks/bench_vs_plain_python.py::TestCreationOverheadBenchmarks::test_physities_unit_operation",
            "value": 517871.28659163666,
            "unit": "iter/sec",
            "range": "stddev: 5.209419346308247e-7",
            "extra": "mean: 1.9309817437098848 usec\nrounds: 87093"
          }
        ]
      },
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
          "id": "338e1285f5bc2ed8227fe5d6f6ab6e4627b0157c",
          "message": "refactor: simplify benchmark tracking to 8 core metrics\n\nReplace 40+ detailed benchmarks with 8 key operations:\n- create_unit, create_composite_type\n- add_units, multiply_units, divide_units\n- convert_simple, convert_composite\n- power\n\nThe detailed benchmarks remain for local testing.\n\nCo-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>",
          "timestamp": "2026-03-26T21:35:16-03:00",
          "tree_id": "2b811f6cb7e4568766c81074881ff66a850eb8d1",
          "url": "https://github.com/CenturyBoys/physities/commit/338e1285f5bc2ed8227fe5d6f6ab6e4627b0157c"
        },
        "date": 1774571769120,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/bench_core.py::TestCoreBenchmarks::test_create_unit",
            "value": 4971936.655376339,
            "unit": "iter/sec",
            "range": "stddev: 2.939282110664026e-8",
            "extra": "mean: 201.1288697571495 nsec\nrounds: 107216"
          },
          {
            "name": "benchmarks/bench_core.py::TestCoreBenchmarks::test_create_composite_type",
            "value": 33674.52780325465,
            "unit": "iter/sec",
            "range": "stddev: 0.00006471392901257904",
            "extra": "mean: 29.696036299085087 usec\nrounds: 10992"
          },
          {
            "name": "benchmarks/bench_core.py::TestCoreBenchmarks::test_add_units",
            "value": 502790.7152219277,
            "unit": "iter/sec",
            "range": "stddev: 5.303436863185236e-7",
            "extra": "mean: 1.9888990980245298 usec\nrounds: 103328"
          },
          {
            "name": "benchmarks/bench_core.py::TestCoreBenchmarks::test_multiply_units",
            "value": 41042.14029756191,
            "unit": "iter/sec",
            "range": "stddev: 0.000002333115185348276",
            "extra": "mean: 24.36520105310893 usec\nrounds: 11395"
          },
          {
            "name": "benchmarks/bench_core.py::TestCoreBenchmarks::test_divide_units",
            "value": 39694.11227463581,
            "unit": "iter/sec",
            "range": "stddev: 0.0000023120635271728203",
            "extra": "mean: 25.19265308369149 usec\nrounds: 15387"
          },
          {
            "name": "benchmarks/bench_core.py::TestCoreBenchmarks::test_convert_simple",
            "value": 813319.5636346707,
            "unit": "iter/sec",
            "range": "stddev: 5.957954054339557e-7",
            "extra": "mean: 1.2295290125950824 usec\nrounds: 161499"
          },
          {
            "name": "benchmarks/bench_core.py::TestCoreBenchmarks::test_convert_composite",
            "value": 782850.9327200936,
            "unit": "iter/sec",
            "range": "stddev: 5.428493869467383e-7",
            "extra": "mean: 1.2773823958098898 usec\nrounds: 196851"
          },
          {
            "name": "benchmarks/bench_core.py::TestCoreBenchmarks::test_power",
            "value": 70739.53132357642,
            "unit": "iter/sec",
            "range": "stddev: 0.0000014929749927491694",
            "extra": "mean: 14.136367336472796 usec\nrounds: 21498"
          }
        ]
      },
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
          "id": "ad5501323085d3f5033a1d8559e550052a2ffa81",
          "message": "docs: add benchmark explanation and baseline comparison\n\n- Compare physities vs plain Python floats\n- Explain what values mean (iter/sec, higher = faster)\n- Document expected overhead (~10-50x for safety)\n- Add benchmarks page to docs navigation\n\nCo-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>",
          "timestamp": "2026-03-26T21:36:58-03:00",
          "tree_id": "29563ba76c491c5927471d2700844a971ea3ce53",
          "url": "https://github.com/CenturyBoys/physities/commit/ad5501323085d3f5033a1d8559e550052a2ffa81"
        },
        "date": 1774571882013,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/bench_core.py::TestBaseline::test_python_float_add",
            "value": 11154719.286893234,
            "unit": "iter/sec",
            "range": "stddev: 8.485933443234501e-9",
            "extra": "mean: 89.6481546761108 nsec\nrounds: 76959"
          },
          {
            "name": "benchmarks/bench_core.py::TestBaseline::test_python_float_multiply",
            "value": 11133237.937145293,
            "unit": "iter/sec",
            "range": "stddev: 9.684231325283098e-9",
            "extra": "mean: 89.82112891560928 nsec\nrounds: 104844"
          },
          {
            "name": "benchmarks/bench_core.py::TestBaseline::test_python_float_divide",
            "value": 11216097.030738395,
            "unit": "iter/sec",
            "range": "stddev: 1.0039204171789027e-8",
            "extra": "mean: 89.15757391005964 nsec\nrounds: 105297"
          },
          {
            "name": "benchmarks/bench_core.py::TestBaseline::test_python_convert",
            "value": 10237890.071528578,
            "unit": "iter/sec",
            "range": "stddev: 1.0172847190121097e-8",
            "extra": "mean: 97.67637599283191 nsec\nrounds: 101236"
          },
          {
            "name": "benchmarks/bench_core.py::TestPhysities::test_unit_add",
            "value": 523611.3106087821,
            "unit": "iter/sec",
            "range": "stddev: 6.233444451888163e-7",
            "extra": "mean: 1.9098135959617444 usec\nrounds: 60165"
          },
          {
            "name": "benchmarks/bench_core.py::TestPhysities::test_unit_multiply",
            "value": 38758.51896126381,
            "unit": "iter/sec",
            "range": "stddev: 0.00001536327240733211",
            "extra": "mean: 25.80077946217253 usec\nrounds: 10225"
          },
          {
            "name": "benchmarks/bench_core.py::TestPhysities::test_unit_divide",
            "value": 38101.97365057427,
            "unit": "iter/sec",
            "range": "stddev: 0.0000025847327875935986",
            "extra": "mean: 26.245359601862205 usec\nrounds: 17080"
          },
          {
            "name": "benchmarks/bench_core.py::TestPhysities::test_unit_convert",
            "value": 833514.8374037208,
            "unit": "iter/sec",
            "range": "stddev: 5.416436549109194e-7",
            "extra": "mean: 1.199738691053007 usec\nrounds: 157928"
          },
          {
            "name": "benchmarks/bench_core.py::TestCreation::test_create_simple",
            "value": 4713047.634091467,
            "unit": "iter/sec",
            "range": "stddev: 3.079992057130605e-8",
            "extra": "mean: 212.17693467949522 nsec\nrounds: 193051"
          },
          {
            "name": "benchmarks/bench_core.py::TestCreation::test_create_composite_type",
            "value": 33098.9746631767,
            "unit": "iter/sec",
            "range": "stddev: 0.00011558808724322061",
            "extra": "mean: 30.212416250842992 usec\nrounds: 11827"
          }
        ]
      },
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
          "id": "c9c6c0b3a3feb09635641d0afb4deaeffaf8420f",
          "message": "fix: use human-readable benchmark names\n\nSet benchmark.name for each test to show clean labels like:\n- \"Python: a + b\"\n- \"Physities: m1 + m2\"\n- \"Create: Meter(100)\"\n\nInstead of long pytest paths.\n\nCo-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>",
          "timestamp": "2026-03-26T21:40:16-03:00",
          "tree_id": "0e396adff03ad48197abd6b999fcc64fcd120896",
          "url": "https://github.com/CenturyBoys/physities/commit/c9c6c0b3a3feb09635641d0afb4deaeffaf8420f"
        },
        "date": 1774572070402,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/bench_core.py::test_baseline_add",
            "value": 11534784.060829062,
            "unit": "iter/sec",
            "range": "stddev: 6.488063077109535e-9",
            "extra": "mean: 86.6942974160968 nsec\nrounds: 62384"
          },
          {
            "name": "benchmarks/bench_core.py::test_baseline_multiply",
            "value": 11131505.634254323,
            "unit": "iter/sec",
            "range": "stddev: 8.822315287149326e-9",
            "extra": "mean: 89.83510702479536 nsec\nrounds: 109087"
          },
          {
            "name": "benchmarks/bench_core.py::test_baseline_divide",
            "value": 11249844.22791963,
            "unit": "iter/sec",
            "range": "stddev: 8.857149448486304e-9",
            "extra": "mean: 88.89011969771103 nsec\nrounds: 110779"
          },
          {
            "name": "benchmarks/bench_core.py::test_baseline_convert",
            "value": 10436395.413236648,
            "unit": "iter/sec",
            "range": "stddev: 1.0291760145270387e-8",
            "extra": "mean: 95.81852358065541 nsec\nrounds: 105065"
          },
          {
            "name": "benchmarks/bench_core.py::test_physities_add",
            "value": 528438.6109585519,
            "unit": "iter/sec",
            "range": "stddev: 4.957578631163961e-7",
            "extra": "mean: 1.8923673994715633 usec\nrounds: 66410"
          },
          {
            "name": "benchmarks/bench_core.py::test_physities_multiply",
            "value": 38195.031720700994,
            "unit": "iter/sec",
            "range": "stddev: 0.0000025551750902500833",
            "extra": "mean: 26.181415617414416 usec\nrounds: 397"
          },
          {
            "name": "benchmarks/bench_core.py::test_physities_divide",
            "value": 38398.84875700201,
            "unit": "iter/sec",
            "range": "stddev: 0.0000032876168590387754",
            "extra": "mean: 26.042447426699233 usec\nrounds: 18070"
          },
          {
            "name": "benchmarks/bench_core.py::test_physities_convert",
            "value": 844700.9084654492,
            "unit": "iter/sec",
            "range": "stddev: 4.507241904572396e-7",
            "extra": "mean: 1.1838509820199903 usec\nrounds: 187266"
          },
          {
            "name": "benchmarks/bench_core.py::test_create_unit",
            "value": 4771662.567995325,
            "unit": "iter/sec",
            "range": "stddev: 2.9358575868672712e-8",
            "extra": "mean: 209.57056073235597 nsec\nrounds: 193051"
          },
          {
            "name": "benchmarks/bench_core.py::test_create_type",
            "value": 33125.937372516324,
            "unit": "iter/sec",
            "range": "stddev: 0.00010641642054214528",
            "extra": "mean: 30.187824989057436 usec\nrounds: 13662"
          }
        ]
      },
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
          "id": "abad862a2a37a2850effb4b36d072c06f89511ff",
          "message": "feat: add custom benchmark page with better UX\n\n- Clean test names (Python: a + b, Physities: m + s)\n- Comparison table showing overhead (e.g., \"15x slower\")\n- Color-coded legend (green=baseline, blue=physities)\n- Clear explanation of what values mean\n- Responsive charts with Chart.js\n\nCo-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>",
          "timestamp": "2026-03-26T21:43:23-03:00",
          "tree_id": "9f86dc52c37fe7f38b6e1489f659efabe9635476",
          "url": "https://github.com/CenturyBoys/physities/commit/abad862a2a37a2850effb4b36d072c06f89511ff"
        },
        "date": 1774572266876,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/bench_core.py::test_baseline_add",
            "value": 10876785.382294916,
            "unit": "iter/sec",
            "range": "stddev: 7.746117099792136e-9",
            "extra": "mean: 91.93892909092138 nsec\nrounds: 77743"
          },
          {
            "name": "benchmarks/bench_core.py::test_baseline_multiply",
            "value": 11236915.636801967,
            "unit": "iter/sec",
            "range": "stddev: 1.268462372466085e-8",
            "extra": "mean: 88.99239189133847 nsec\nrounds: 109566"
          },
          {
            "name": "benchmarks/bench_core.py::test_baseline_divide",
            "value": 11273687.938565433,
            "unit": "iter/sec",
            "range": "stddev: 8.598165799660522e-9",
            "extra": "mean: 88.7021181932454 nsec\nrounds: 108602"
          },
          {
            "name": "benchmarks/bench_core.py::test_baseline_convert",
            "value": 10355557.25387573,
            "unit": "iter/sec",
            "range": "stddev: 9.006742401326705e-9",
            "extra": "mean: 96.56650776814517 nsec\nrounds: 103756"
          },
          {
            "name": "benchmarks/bench_core.py::test_physities_add",
            "value": 532403.5340393274,
            "unit": "iter/sec",
            "range": "stddev: 5.217297723644926e-7",
            "extra": "mean: 1.8782745343800296 usec\nrounds: 58204"
          },
          {
            "name": "benchmarks/bench_core.py::test_physities_multiply",
            "value": 38353.89350562726,
            "unit": "iter/sec",
            "range": "stddev: 0.0000035633303687611505",
            "extra": "mean: 26.07297222257971 usec\nrounds: 468"
          },
          {
            "name": "benchmarks/bench_core.py::test_physities_divide",
            "value": 37990.15716600631,
            "unit": "iter/sec",
            "range": "stddev: 0.0000041169456758877084",
            "extra": "mean: 26.32260760676196 usec\nrounds: 18168"
          },
          {
            "name": "benchmarks/bench_core.py::test_physities_convert",
            "value": 820930.7013444635,
            "unit": "iter/sec",
            "range": "stddev: 4.570959392438799e-7",
            "extra": "mean: 1.2181296160105468 usec\nrounds: 152836"
          },
          {
            "name": "benchmarks/bench_core.py::test_create_unit",
            "value": 4940706.274403378,
            "unit": "iter/sec",
            "range": "stddev: 3.017216031543889e-8",
            "extra": "mean: 202.4002125321668 nsec\nrounds: 195734"
          },
          {
            "name": "benchmarks/bench_core.py::test_create_type",
            "value": 32988.898792162836,
            "unit": "iter/sec",
            "range": "stddev: 0.00011435230014619481",
            "extra": "mean: 30.313227680020944 usec\nrounds: 11828"
          }
        ]
      },
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
          "id": "ac81867b2fe29c00a31524ffec476b92b64a76ff",
          "message": "fix: handle both old and new benchmark name patterns\n\nUpdate JavaScript to recognize:\n- Old: TestBaseline::test_python_float_add\n- New: test_baseline_add\n\nUse helper functions to categorize benchmarks properly.\n\nCo-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>",
          "timestamp": "2026-03-26T21:47:14-03:00",
          "tree_id": "6d70bebd295970b5691ef7be03e545877eba1ac3",
          "url": "https://github.com/CenturyBoys/physities/commit/ac81867b2fe29c00a31524ffec476b92b64a76ff"
        },
        "date": 1774572495541,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/bench_core.py::test_baseline_add",
            "value": 11282334.711959362,
            "unit": "iter/sec",
            "range": "stddev: 6.8365731776393045e-9",
            "extra": "mean: 88.63413695216754 nsec\nrounds: 50644"
          },
          {
            "name": "benchmarks/bench_core.py::test_baseline_multiply",
            "value": 11349508.714034922,
            "unit": "iter/sec",
            "range": "stddev: 1.9086970686842074e-8",
            "extra": "mean: 88.1095407031697 nsec\nrounds: 112411"
          },
          {
            "name": "benchmarks/bench_core.py::test_baseline_divide",
            "value": 11187117.163314864,
            "unit": "iter/sec",
            "range": "stddev: 1.2029859550443183e-8",
            "extra": "mean: 89.38853373945769 nsec\nrounds: 110792"
          },
          {
            "name": "benchmarks/bench_core.py::test_baseline_convert",
            "value": 10313834.937595524,
            "unit": "iter/sec",
            "range": "stddev: 1.0346498113477401e-8",
            "extra": "mean: 96.95714601319955 nsec\nrounds: 101854"
          },
          {
            "name": "benchmarks/bench_core.py::test_physities_add",
            "value": 514171.6673547721,
            "unit": "iter/sec",
            "range": "stddev: 5.577745444455164e-7",
            "extra": "mean: 1.9448757360448108 usec\nrounds: 56042"
          },
          {
            "name": "benchmarks/bench_core.py::test_physities_multiply",
            "value": 37207.33454834147,
            "unit": "iter/sec",
            "range": "stddev: 0.0000035820620234165792",
            "extra": "mean: 26.87642133302385 usec\nrounds: 375"
          },
          {
            "name": "benchmarks/bench_core.py::test_physities_divide",
            "value": 36662.340998139276,
            "unit": "iter/sec",
            "range": "stddev: 0.00000426664832955237",
            "extra": "mean: 27.275945091742862 usec\nrounds: 17338"
          },
          {
            "name": "benchmarks/bench_core.py::test_physities_convert",
            "value": 819668.2343407014,
            "unit": "iter/sec",
            "range": "stddev: 7.957336104878587e-7",
            "extra": "mean: 1.2200058000348741 usec\nrounds: 172414"
          },
          {
            "name": "benchmarks/bench_core.py::test_create_unit",
            "value": 4645858.976867666,
            "unit": "iter/sec",
            "range": "stddev: 9.996935169189538e-8",
            "extra": "mean: 215.24544868436283 nsec\nrounds: 196890"
          },
          {
            "name": "benchmarks/bench_core.py::test_create_type",
            "value": 30078.56108225812,
            "unit": "iter/sec",
            "range": "stddev: 0.00014340186540089247",
            "extra": "mean: 33.246271231699694 usec\nrounds: 10880"
          }
        ]
      },
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
          "id": "7a69c9bc2c20c2845a29b5583772db318ad98538",
          "message": "fix: redesign benchmark page for clarity\n\n- Show TIME per operation (lower = faster) instead of ops/sec\n- Add \"✓ faster\" label under Python column\n- Color code: green (faster) vs red (slower)\n- Show average overhead summary at top\n- Use nanoseconds/microseconds for intuitive comparison\n\nCo-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>",
          "timestamp": "2026-03-26T21:54:32-03:00",
          "tree_id": "91b5887fd1d3cda426acc1c2461e89e98f236096",
          "url": "https://github.com/CenturyBoys/physities/commit/7a69c9bc2c20c2845a29b5583772db318ad98538"
        },
        "date": 1774572931860,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/bench_core.py::test_baseline_add",
            "value": 11203471.224930026,
            "unit": "iter/sec",
            "range": "stddev: 9.22980367601862e-9",
            "extra": "mean: 89.2580504669661 nsec\nrounds: 84653"
          },
          {
            "name": "benchmarks/bench_core.py::test_baseline_multiply",
            "value": 11314513.548191458,
            "unit": "iter/sec",
            "range": "stddev: 9.4445995236748e-9",
            "extra": "mean: 88.38205864895744 nsec\nrounds: 111272"
          },
          {
            "name": "benchmarks/bench_core.py::test_baseline_divide",
            "value": 10803053.027309453,
            "unit": "iter/sec",
            "range": "stddev: 9.991644565888491e-9",
            "extra": "mean: 92.56642520141875 nsec\nrounds: 106406"
          },
          {
            "name": "benchmarks/bench_core.py::test_baseline_convert",
            "value": 10262952.692625493,
            "unit": "iter/sec",
            "range": "stddev: 1.0231747703639298e-8",
            "extra": "mean: 97.43784561332222 nsec\nrounds: 102470"
          },
          {
            "name": "benchmarks/bench_core.py::test_physities_add",
            "value": 529486.0219423464,
            "unit": "iter/sec",
            "range": "stddev: 5.118769660061117e-7",
            "extra": "mean: 1.8886239835598269 usec\nrounds: 60383"
          },
          {
            "name": "benchmarks/bench_core.py::test_physities_multiply",
            "value": 37556.20063766439,
            "unit": "iter/sec",
            "range": "stddev: 0.0000036284619957093964",
            "extra": "mean: 26.626761573882934 usec\nrounds: 432"
          },
          {
            "name": "benchmarks/bench_core.py::test_physities_divide",
            "value": 38628.9706050511,
            "unit": "iter/sec",
            "range": "stddev: 0.0000025363494265476353",
            "extra": "mean: 25.887306452562846 usec\nrounds: 17745"
          },
          {
            "name": "benchmarks/bench_core.py::test_physities_convert",
            "value": 822019.8010451862,
            "unit": "iter/sec",
            "range": "stddev: 4.866628257267352e-7",
            "extra": "mean: 1.216515707685526 usec\nrounds: 140568"
          },
          {
            "name": "benchmarks/bench_core.py::test_create_unit",
            "value": 5015021.82547301,
            "unit": "iter/sec",
            "range": "stddev: 3.3606152061855916e-8",
            "extra": "mean: 199.40092681565255 nsec\nrounds: 198808"
          },
          {
            "name": "benchmarks/bench_core.py::test_create_type",
            "value": 32973.18189175701,
            "unit": "iter/sec",
            "range": "stddev: 0.00012817419614369113",
            "extra": "mean: 30.327676694434842 usec\nrounds: 11834"
          }
        ]
      },
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
          "id": "ccf690102d1b53b61aee801c5f466bd115c24275",
          "message": "fix: copy benchmarks to /tmp to use installed wheel\n\nPytest was importing from source directory instead of the installed\nwheel, causing Rust module to not be found. Copy benchmarks to /tmp\nto isolate from source.\n\nCo-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>",
          "timestamp": "2026-03-26T22:50:05-03:00",
          "tree_id": "fa2f4a6458f072353a9cf9c79c39efef48d75c72",
          "url": "https://github.com/CenturyBoys/physities/commit/ccf690102d1b53b61aee801c5f466bd115c24275"
        },
        "date": 1774576260483,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/bench_core.py::test_baseline_add",
            "value": 11559222.471035618,
            "unit": "iter/sec",
            "range": "stddev: 8.401399558912505e-9",
            "extra": "mean: 86.51100906706647 nsec\nrounds: 82761"
          },
          {
            "name": "benchmarks/bench_core.py::test_baseline_multiply",
            "value": 11500001.900187364,
            "unit": "iter/sec",
            "range": "stddev: 9.010405686213164e-9",
            "extra": "mean: 86.95650737099065 nsec\nrounds: 112537"
          },
          {
            "name": "benchmarks/bench_core.py::test_baseline_divide",
            "value": 10991612.067633962,
            "unit": "iter/sec",
            "range": "stddev: 1.0022841357739199e-8",
            "extra": "mean: 90.9784655650534 nsec\nrounds: 110412"
          },
          {
            "name": "benchmarks/bench_core.py::test_baseline_convert",
            "value": 9819015.205644714,
            "unit": "iter/sec",
            "range": "stddev: 1.3988641783716399e-8",
            "extra": "mean: 101.84320719091602 nsec\nrounds: 104406"
          },
          {
            "name": "benchmarks/bench_core.py::test_physities_add",
            "value": 319712.6470692095,
            "unit": "iter/sec",
            "range": "stddev: 7.532423977042093e-7",
            "extra": "mean: 3.127808703118103 usec\nrounds: 40790"
          },
          {
            "name": "benchmarks/bench_core.py::test_physities_multiply",
            "value": 318441.2882581725,
            "unit": "iter/sec",
            "range": "stddev: 7.853328208466961e-7",
            "extra": "mean: 3.140296302247282 usec\nrounds: 30533"
          },
          {
            "name": "benchmarks/bench_core.py::test_physities_divide",
            "value": 317235.44536178844,
            "unit": "iter/sec",
            "range": "stddev: 6.952078315876704e-7",
            "extra": "mean: 3.152232875048243 usec\nrounds: 47781"
          },
          {
            "name": "benchmarks/bench_core.py::test_physities_convert",
            "value": 584525.754056713,
            "unit": "iter/sec",
            "range": "stddev: 6.151532360766166e-7",
            "extra": "mean: 1.710788606079068 usec\nrounds: 110779"
          },
          {
            "name": "benchmarks/bench_core.py::test_create_unit",
            "value": 2987409.8292052303,
            "unit": "iter/sec",
            "range": "stddev: 2.3756896015185492e-7",
            "extra": "mean: 334.73813677115726 nsec\nrounds: 161760"
          },
          {
            "name": "benchmarks/bench_core.py::test_create_type",
            "value": 130639.94996546276,
            "unit": "iter/sec",
            "range": "stddev: 0.00007424663422527274",
            "extra": "mean: 7.6546263242168235 usec\nrounds: 29357"
          }
        ]
      },
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
          "id": "b3152651a5379aa5e8b5e9cf52f5b29167dd159c",
          "message": "feat: add NumPy batch operations via UnitArray\n\n- UnitArray class for vectorized operations on arrays of values\n- All values share same unit type for efficiency\n- Supports: add, sub, mul, div, pow, sum, mean, std, min, max\n- Batch convert() for converting all values at once\n- ~100x faster than loops for 1000+ elements\n\nAlso adds numpy as a dependency and batch benchmarks.\n\nNote: mypyc compilation would conflict with maturin build system.\nThe Rust backend already handles performance-critical code.\n\nCo-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>",
          "timestamp": "2026-03-26T23:00:43-03:00",
          "tree_id": "c98f2310c72e59449a4b6e2c79aad7ab235d6c4d",
          "url": "https://github.com/CenturyBoys/physities/commit/b3152651a5379aa5e8b5e9cf52f5b29167dd159c"
        },
        "date": 1774576901110,
        "tool": "pytest",
        "benches": [
          {
            "name": "benchmarks/bench_core.py::test_baseline_add",
            "value": 10847941.078958722,
            "unit": "iter/sec",
            "range": "stddev: 1.7375897574085292e-8",
            "extra": "mean: 92.1833915506516 nsec\nrounds: 79340"
          },
          {
            "name": "benchmarks/bench_core.py::test_baseline_multiply",
            "value": 10992433.667853765,
            "unit": "iter/sec",
            "range": "stddev: 9.966061546223853e-9",
            "extra": "mean: 90.97166562159765 nsec\nrounds: 108614"
          },
          {
            "name": "benchmarks/bench_core.py::test_baseline_divide",
            "value": 10446206.72330525,
            "unit": "iter/sec",
            "range": "stddev: 1.0061904321218857e-8",
            "extra": "mean: 95.72852868870775 nsec\nrounds: 110534"
          },
          {
            "name": "benchmarks/bench_core.py::test_baseline_convert",
            "value": 10321520.640412029,
            "unit": "iter/sec",
            "range": "stddev: 9.911781098194147e-9",
            "extra": "mean: 96.88494891780029 nsec\nrounds: 103853"
          },
          {
            "name": "benchmarks/bench_core.py::test_physities_add",
            "value": 318409.70106013684,
            "unit": "iter/sec",
            "range": "stddev: 6.841555883127812e-7",
            "extra": "mean: 3.140607829065904 usec\nrounds: 41589"
          },
          {
            "name": "benchmarks/bench_core.py::test_physities_multiply",
            "value": 322726.4315081284,
            "unit": "iter/sec",
            "range": "stddev: 6.129602118060761e-7",
            "extra": "mean: 3.0985996260886157 usec\nrounds: 29947"
          },
          {
            "name": "benchmarks/bench_core.py::test_physities_divide",
            "value": 326658.2417082383,
            "unit": "iter/sec",
            "range": "stddev: 7.582047666718828e-7",
            "extra": "mean: 3.0613034429211523 usec\nrounds: 66543"
          },
          {
            "name": "benchmarks/bench_core.py::test_physities_convert",
            "value": 569986.834117202,
            "unit": "iter/sec",
            "range": "stddev: 7.422133216384307e-7",
            "extra": "mean: 1.7544264887254881 usec\nrounds: 128123"
          },
          {
            "name": "benchmarks/bench_core.py::test_numpy_add_1000",
            "value": 926878.2562902432,
            "unit": "iter/sec",
            "range": "stddev: 3.446086825735468e-7",
            "extra": "mean: 1.0788903431637513 usec\nrounds: 61346"
          },
          {
            "name": "benchmarks/bench_core.py::test_numpy_multiply_1000",
            "value": 920883.9766663961,
            "unit": "iter/sec",
            "range": "stddev: 3.231483469958852e-7",
            "extra": "mean: 1.0859131284051702 usec\nrounds: 105731"
          },
          {
            "name": "benchmarks/bench_core.py::test_numpy_sum_1000",
            "value": 331403.63203872246,
            "unit": "iter/sec",
            "range": "stddev: 6.097291270325847e-7",
            "extra": "mean: 3.0174684382552464 usec\nrounds: 24238"
          },
          {
            "name": "benchmarks/bench_core.py::test_unitarray_add_1000",
            "value": 238307.08884132354,
            "unit": "iter/sec",
            "range": "stddev: 7.580615987746601e-7",
            "extra": "mean: 4.19626627500724 usec\nrounds: 27235"
          },
          {
            "name": "benchmarks/bench_core.py::test_unitarray_multiply_1000",
            "value": 508140.7310490102,
            "unit": "iter/sec",
            "range": "stddev: 4.668666274127735e-7",
            "extra": "mean: 1.9679587541340986 usec\nrounds: 133977"
          },
          {
            "name": "benchmarks/bench_core.py::test_unitarray_sum_1000",
            "value": 289427.08739212825,
            "unit": "iter/sec",
            "range": "stddev: 6.751231373864007e-7",
            "extra": "mean: 3.455101625112086 usec\nrounds: 35572"
          },
          {
            "name": "benchmarks/bench_core.py::test_unitarray_convert_1000",
            "value": 344585.76121638017,
            "unit": "iter/sec",
            "range": "stddev: 6.053629254142483e-7",
            "extra": "mean: 2.9020351754234475 usec\nrounds: 46424"
          },
          {
            "name": "benchmarks/bench_core.py::test_loop_add_100",
            "value": 3453.3550811632717,
            "unit": "iter/sec",
            "range": "stddev: 0.000007222364151377228",
            "extra": "mean: 289.5734659475409 usec\nrounds: 3245"
          },
          {
            "name": "benchmarks/bench_core.py::test_batch_add_100",
            "value": 257413.01308375987,
            "unit": "iter/sec",
            "range": "stddev: 6.878602681779269e-7",
            "extra": "mean: 3.8848074851391017 usec\nrounds: 25250"
          }
        ]
      }
    ]
  }
}