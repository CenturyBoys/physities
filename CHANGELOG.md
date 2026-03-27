# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0] - 2025-03-27

### Added
- **UnitArray** for batch operations on arrays of values
  - NumPy-backed vectorized operations (~100x faster than loops)
  - Supports arithmetic, reductions (sum, mean, std, min, max)
  - Batch unit conversions
- **Database serialization** for Unit values
  - `to_tuple()` / `from_tuple()` for compact storage (si_value, dimension_int64)
  - `to_dict()` / `from_dict()` for full round-trip serialization
- Custom exception hierarchy for better error handling
  - `PhysitiesError` base exception
  - `DimensionMismatchError` for incompatible dimensions
  - `InvalidConversionError` for invalid unit conversions
  - `InvalidOperationError` for invalid arithmetic operations
  - `InvalidPowerError` for invalid power operations
- Comprehensive test suite
  - Integration tests for Python/Rust interoperability
  - Property-based tests using Hypothesis
  - Edge case tests for boundary conditions
- Benchmark suite with pytest-benchmark
  - Performance tracking over time
  - Comparison vs plain Python and NumPy
  - Interactive benchmark page at `/dev/bench/`
- CI/CD improvements
  - Codecov integration for coverage tracking
  - Benchmark CI with GitHub Pages deployment
  - Sphinx documentation
- Comprehensive docstrings for all public APIs

### Changed
- Improved error messages with more context
- Updated pyproject.toml with full metadata and classifiers

## [0.1.3] - 2025-01-15

### Added
- Rust core with PyO3 for high-performance operations
- `PhysicalScale` struct with ndarray-based linear algebra
- NumPy interoperability for the Rust backend
- JSON and int64 serialization for scales

### Changed
- Improved performance for scale operations

## [0.1.2] - 2024-12-01

### Added
- CI/CD pipeline with GitHub Actions
- Ruff linting integration
- Architecture documentation

### Changed
- Improved code organization

## [0.1.1] - 2024-11-15

### Added
- Kobject integration for attribute validation
- Additional unit types (area, volume, etc.)

### Fixed
- Minor bug fixes in unit conversion

## [0.1.0] - 2024-10-01

### Added
- Initial release
- Core `Dimension`, `Scale`, and `Unit` classes
- SI base units and common derived units
- Operator overloading for unit composition
- Unit conversion with dimensional analysis
- Basic arithmetic operations on physical quantities

[Unreleased]: https://github.com/CenturyBoys/physities/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/CenturyBoys/physities/compare/v0.1.3...v0.2.0
[0.1.3]: https://github.com/CenturyBoys/physities/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/CenturyBoys/physities/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/CenturyBoys/physities/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/CenturyBoys/physities/releases/tag/v0.1.0
