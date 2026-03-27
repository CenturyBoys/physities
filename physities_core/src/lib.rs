use pyo3::prelude::*;

mod physical_dimension;
mod physical_scale;

pub use physical_dimension::PhysicalDimension;
pub use physical_scale::PhysicalScale;

/// Physities core module implemented in Rust.
///
/// This module provides high-performance implementations of physical scale
/// and dimension operations using ndarray for linear algebra.
#[pymodule]
fn _physities_core(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<PhysicalDimension>()?;
    m.add_class::<PhysicalScale>()?;

    // Add version info
    m.add("__version__", "0.2.0")?;

    Ok(())
}
