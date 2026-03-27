window.BENCHMARK_DATA = {
  "lastUpdate": 1774571461688,
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
      }
    ]
  }
}