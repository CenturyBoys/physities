#!/usr/bin/env python3
"""CLI script for running physities benchmarks.

Usage:
    python benchmarks/run_benchmarks.py [options]

Examples:
    # Run all benchmarks
    python benchmarks/run_benchmarks.py

    # Run only conversion benchmarks
    python benchmarks/run_benchmarks.py --group conversions

    # Run with comparison to baseline
    python benchmarks/run_benchmarks.py --compare baseline.json

    # Save results for later comparison
    python benchmarks/run_benchmarks.py --save results.json
"""

import argparse
import subprocess
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="Run physities benchmarks",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--group",
        "-g",
        help="Run only benchmarks in this group (e.g., 'conversions', 'arithmetic')",
    )
    parser.add_argument(
        "--save",
        "-s",
        metavar="FILE",
        help="Save benchmark results to JSON file",
    )
    parser.add_argument(
        "--compare",
        "-c",
        metavar="FILE",
        help="Compare results against a baseline JSON file",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Show verbose output",
    )
    parser.add_argument(
        "--quick",
        "-q",
        action="store_true",
        help="Run quick benchmarks (fewer iterations)",
    )
    parser.add_argument(
        "--list",
        "-l",
        action="store_true",
        help="List available benchmark groups",
    )

    args = parser.parse_args()

    # Get the benchmarks directory
    benchmark_dir = Path(__file__).parent

    if args.list:
        print("Available benchmark groups:")
        print("  - conversions: Unit conversion benchmarks")
        print("  - unit-creation: Unit creation benchmarks")
        print("  - arithmetic: Arithmetic operation benchmarks")
        print("  - vs-plain-python: Comparison with plain Python")
        print("  - vs-numpy: Comparison with NumPy (if installed)")
        print("  - batch-operations: Batch operation benchmarks")
        return 0

    # Build pytest command
    cmd = [
        sys.executable,
        "-m",
        "pytest",
        str(benchmark_dir),
        "--benchmark-only",
    ]

    # Add options
    if args.verbose:
        cmd.append("-v")

    if args.group:
        cmd.extend(["--benchmark-group-by", "group"])
        cmd.extend(["-k", args.group])

    if args.quick:
        cmd.extend(["--benchmark-disable-gc", "--benchmark-warmup=off"])
        cmd.extend(["--benchmark-min-rounds=5"])
    else:
        cmd.extend(["--benchmark-min-rounds=10"])

    if args.save:
        cmd.extend(["--benchmark-json", args.save])

    if args.compare:
        cmd.extend(["--benchmark-compare", args.compare])

    # Add nice output formatting
    cmd.extend([
        "--benchmark-columns=min,max,mean,stddev,median,ops",
        "--benchmark-sort=mean",
    ])

    print(f"Running: {' '.join(cmd)}")
    print()

    try:
        result = subprocess.run(cmd, check=False)
        return result.returncode
    except KeyboardInterrupt:
        print("\nBenchmark interrupted.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
