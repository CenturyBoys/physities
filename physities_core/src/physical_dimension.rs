use pyo3::prelude::*;
use pyo3::types::PyTuple;
use std::collections::hash_map::DefaultHasher;
use std::hash::{Hash, Hasher};

// Dimension indices (same as physical_scale.rs)
pub const DIM_LENGTH: usize = 0;
pub const DIM_MASS: usize = 1;
pub const DIM_TEMPERATURE: usize = 2;
pub const DIM_TIME: usize = 3;
pub const DIM_AMOUNT: usize = 4;
pub const DIM_ELECTRIC_CURRENT: usize = 5;
pub const DIM_LUMINOUS_INTENSITY: usize = 6;

/// Symbols for dimension display
const SYMBOLS: [&str; 7] = ["L", "m", "T", "t", "N", "I", "Iᵥ"];

/// Superscript characters for power display
const SUPERSCRIPTS: [char; 10] = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹'];

/// Physical dimension representation using 7 SI base dimensions.
///
/// A PhysicalDimension stores exponents for each of the 7 SI base dimensions:
/// LENGTH, MASS, TEMPERATURE, TIME, AMOUNT, ELECTRIC_CURRENT, and LUMINOUS_INTENSITY.
///
/// This is a frozen (immutable) class that supports arithmetic operations
/// for combining dimensions algebraically.
#[pyclass(frozen, skip_from_py_object)]
#[derive(Clone, Debug)]
pub struct PhysicalDimension {
    data: [f64; 7],
}

impl Default for PhysicalDimension {
    fn default() -> Self {
        Self::new_dimensionless()
    }
}

impl PhysicalDimension {
    /// Create from raw array (internal use)
    pub fn from_array(data: [f64; 7]) -> Self {
        Self { data }
    }

    /// Get the internal data array
    pub fn as_array(&self) -> &[f64; 7] {
        &self.data
    }
}

#[pymethods]
impl PhysicalDimension {
    /// Create a new PhysicalDimension from a 7-element tuple of exponents.
    #[new]
    pub fn new(dimensions_tuple: &Bound<'_, PyTuple>) -> PyResult<Self> {
        if dimensions_tuple.len() != 7 {
            return Err(pyo3::exceptions::PyValueError::new_err(
                "dimensions_tuple must have exactly 7 elements",
            ));
        }

        let mut data = [0.0; 7];
        for i in 0..7 {
            data[i] = dimensions_tuple.get_item(i)?.extract::<f64>()?;
        }

        Ok(Self { data })
    }

    // ==================== Static Factory Methods ====================

    /// Create a dimensionless dimension (all exponents are zero).
    #[staticmethod]
    pub fn new_dimensionless() -> Self {
        Self { data: [0.0; 7] }
    }

    /// Create a new dimension from a tuple of exponents.
    #[staticmethod]
    pub fn new_instance(dimensions_tuple: &Bound<'_, PyTuple>) -> PyResult<Self> {
        Self::new(dimensions_tuple)
    }

    /// Create a length dimension with the given power.
    #[staticmethod]
    #[pyo3(signature = (power=None))]
    pub fn new_length(power: Option<f64>) -> Self {
        let mut data = [0.0; 7];
        data[DIM_LENGTH] = power.unwrap_or(1.0);
        Self { data }
    }

    /// Create a mass dimension with the given power.
    #[staticmethod]
    #[pyo3(signature = (power=None))]
    pub fn new_mass(power: Option<f64>) -> Self {
        let mut data = [0.0; 7];
        data[DIM_MASS] = power.unwrap_or(1.0);
        Self { data }
    }

    /// Create a temperature dimension with the given power.
    #[staticmethod]
    #[pyo3(signature = (power=None))]
    pub fn new_temperature(power: Option<f64>) -> Self {
        let mut data = [0.0; 7];
        data[DIM_TEMPERATURE] = power.unwrap_or(1.0);
        Self { data }
    }

    /// Create a time dimension with the given power.
    #[staticmethod]
    #[pyo3(signature = (power=None))]
    pub fn new_time(power: Option<f64>) -> Self {
        let mut data = [0.0; 7];
        data[DIM_TIME] = power.unwrap_or(1.0);
        Self { data }
    }

    /// Create an amount of substance dimension with the given power.
    #[staticmethod]
    #[pyo3(signature = (power=None))]
    pub fn new_amount(power: Option<f64>) -> Self {
        let mut data = [0.0; 7];
        data[DIM_AMOUNT] = power.unwrap_or(1.0);
        Self { data }
    }

    /// Create an electric current dimension with the given power.
    #[staticmethod]
    #[pyo3(signature = (power=None))]
    pub fn new_electric_current(power: Option<f64>) -> Self {
        let mut data = [0.0; 7];
        data[DIM_ELECTRIC_CURRENT] = power.unwrap_or(1.0);
        Self { data }
    }

    /// Create a luminous intensity dimension with the given power.
    #[staticmethod]
    #[pyo3(signature = (power=None))]
    pub fn new_luminous_intensity(power: Option<f64>) -> Self {
        let mut data = [0.0; 7];
        data[DIM_LUMINOUS_INTENSITY] = power.unwrap_or(1.0);
        Self { data }
    }

    // ==================== Property Accessors ====================

    /// The length dimension exponent (L).
    #[getter]
    pub fn length(&self) -> f64 {
        self.data[DIM_LENGTH]
    }

    /// The mass dimension exponent (M).
    #[getter]
    pub fn mass(&self) -> f64 {
        self.data[DIM_MASS]
    }

    /// The temperature dimension exponent (Θ).
    #[getter]
    pub fn temperature(&self) -> f64 {
        self.data[DIM_TEMPERATURE]
    }

    /// The time dimension exponent (T).
    #[getter]
    pub fn time(&self) -> f64 {
        self.data[DIM_TIME]
    }

    /// The amount of substance dimension exponent (N).
    #[getter]
    pub fn amount(&self) -> f64 {
        self.data[DIM_AMOUNT]
    }

    /// The electric current dimension exponent (I).
    #[getter]
    pub fn electric_current(&self) -> f64 {
        self.data[DIM_ELECTRIC_CURRENT]
    }

    /// The luminous intensity dimension exponent (J).
    #[getter]
    pub fn luminous_intensity(&self) -> f64 {
        self.data[DIM_LUMINOUS_INTENSITY]
    }

    /// Get the dimensions tuple as a Python tuple.
    #[getter]
    pub fn dimensions_tuple<'py>(&self, py: Python<'py>) -> Bound<'py, PyTuple> {
        PyTuple::new(py, self.data).unwrap()
    }

    /// Get the exponent for a specific base dimension by index.
    pub fn get(&self, index: usize) -> f64 {
        if index < 7 {
            self.data[index]
        } else {
            0.0
        }
    }

    /// Get list of active dimensions (indices where exponent != 0).
    pub fn get_dimensions(&self) -> Vec<usize> {
        (0..7).filter(|&i| self.data[i] != 0.0).collect()
    }

    // ==================== Arithmetic Operations ====================

    /// Add two dimensions (combine dimension exponents).
    pub fn __add__(&self, other: &PhysicalDimension) -> PhysicalDimension {
        let mut data = [0.0; 7];
        for i in 0..7 {
            data[i] = self.data[i] + other.data[i];
        }
        PhysicalDimension { data }
    }

    /// Subtract two dimensions.
    pub fn __sub__(&self, other: &PhysicalDimension) -> PhysicalDimension {
        let mut data = [0.0; 7];
        for i in 0..7 {
            data[i] = self.data[i] - other.data[i];
        }
        PhysicalDimension { data }
    }

    /// Multiply dimension by a scalar (scale all exponents).
    pub fn __mul__(&self, scalar: f64) -> PhysicalDimension {
        let mut data = [0.0; 7];
        for i in 0..7 {
            data[i] = self.data[i] * scalar;
        }
        PhysicalDimension { data }
    }

    /// Right multiply (scalar * dimension).
    pub fn __rmul__(&self, scalar: f64) -> PhysicalDimension {
        self.__mul__(scalar)
    }

    /// Divide dimension by a scalar.
    pub fn __truediv__(&self, scalar: f64) -> PhysicalDimension {
        let mut data = [0.0; 7];
        for i in 0..7 {
            data[i] = self.data[i] / scalar;
        }
        PhysicalDimension { data }
    }

    /// Right divide (scalar / dimension) - element-wise scalar/exponent.
    /// Returns 0.0 for zero exponents to avoid division by zero.
    pub fn __rtruediv__(&self, scalar: f64) -> PhysicalDimension {
        let mut data = [0.0; 7];
        for i in 0..7 {
            data[i] = if self.data[i] != 0.0 {
                scalar / self.data[i]
            } else {
                0.0
            };
        }
        PhysicalDimension { data }
    }

    /// Negate all dimension exponents.
    pub fn __neg__(&self) -> PhysicalDimension {
        let mut data = [0.0; 7];
        for i in 0..7 {
            data[i] = -self.data[i];
        }
        PhysicalDimension { data }
    }

    // ==================== Comparison Operations ====================

    /// Check equality of dimensions.
    pub fn __eq__(&self, other: &PhysicalDimension) -> bool {
        self.data == other.data
    }

    /// Check inequality.
    pub fn __ne__(&self, other: &PhysicalDimension) -> bool {
        self.data != other.data
    }

    /// Hash the dimension (for use in sets/dicts).
    pub fn __hash__(&self) -> u64 {
        let mut hasher = DefaultHasher::new();
        for &val in &self.data {
            val.to_bits().hash(&mut hasher);
        }
        hasher.finish()
    }

    // ==================== String Representation ====================

    /// Generate a human-readable string representation of the dimension.
    pub fn show_dimension(&self) -> String {
        let mut numerator = String::new();
        let mut denominator = String::new();

        for (i, &power) in self.data.iter().enumerate() {
            if power == 0.0 {
                continue;
            }

            let (is_numerator, abs_power) = if power < 0.0 {
                (false, -power)
            } else {
                (true, power)
            };

            let power_str = format_power(abs_power);
            let symbol = SYMBOLS[i];

            if is_numerator {
                numerator.push_str(symbol);
                numerator.push_str(&power_str);
            } else {
                denominator.push_str(symbol);
                denominator.push_str(&power_str);
            }
        }

        if denominator.is_empty() {
            numerator
        } else if numerator.is_empty() {
            format!("1 / {}", denominator)
        } else {
            format!("{} / {}", numerator, denominator)
        }
    }

    pub fn __repr__(&self) -> String {
        format!("PhysicalDimension({:?})", self.data)
    }

    pub fn __str__(&self) -> String {
        self.show_dimension()
    }
}

/// Format a power value as superscript characters.
fn format_power(power: f64) -> String {
    let s = format!("{}", power);
    let mut result = String::new();

    for c in s.chars() {
        match c {
            '0'..='9' => {
                let digit = c.to_digit(10).unwrap() as usize;
                result.push(SUPERSCRIPTS[digit]);
            }
            '.' => result.push('ˑ'),
            '-' => result.push('⁻'),
            _ => result.push(c),
        }
    }

    result
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_new_dimensionless() {
        let dim = PhysicalDimension::new_dimensionless();
        assert_eq!(dim.data, [0.0; 7]);
    }

    #[test]
    fn test_new_length() {
        let dim = PhysicalDimension::new_length(Some(2.0));
        assert_eq!(dim.data[DIM_LENGTH], 2.0);
        assert_eq!(dim.data[DIM_MASS], 0.0);
    }

    #[test]
    fn test_add() {
        let dim1 = PhysicalDimension::new_length(Some(1.0));
        let dim2 = PhysicalDimension::new_time(Some(-1.0));
        let result = dim1.__add__(&dim2);
        assert_eq!(result.data[DIM_LENGTH], 1.0);
        assert_eq!(result.data[DIM_TIME], -1.0);
    }

    #[test]
    fn test_mul_scalar() {
        let dim = PhysicalDimension::new_length(Some(1.0));
        let result = dim.__mul__(2.0);
        assert_eq!(result.data[DIM_LENGTH], 2.0);
    }

    #[test]
    fn test_eq() {
        let dim1 = PhysicalDimension::new_length(Some(1.0));
        let dim2 = PhysicalDimension::new_length(Some(1.0));
        let dim3 = PhysicalDimension::new_mass(Some(1.0));
        assert!(dim1.__eq__(&dim2));
        assert!(!dim1.__eq__(&dim3));
    }
}
