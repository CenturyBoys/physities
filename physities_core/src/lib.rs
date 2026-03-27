use pyo3::prelude::*;

mod physical_scale;

pub use physical_scale::PhysicalScale;

/// Physities core module implemented in Rust.
///
/// This module provides high-performance implementations of physical scale
/// operations using ndarray for linear algebra.
#[pymodule]
fn _physities_core(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<PhysicalScale>()?;

    // Add version info
    m.add("__version__", "0.1.3")?;

    Ok(())
}
