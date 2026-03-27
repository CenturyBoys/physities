use ndarray::Array1;
use numpy::{IntoPyArray, PyArray1, PyReadonlyArray1};
use pyo3::prelude::*;
use pyo3::types::{PyDict, PyTuple};
use serde_json;

use crate::physical_dimension::PhysicalDimension;

// Dimension indices
pub const DIM_LENGTH: usize = 0;
pub const DIM_MASS: usize = 1;
pub const DIM_TEMPERATURE: usize = 2;
pub const DIM_TIME: usize = 3;
pub const DIM_AMOUNT: usize = 4;
pub const DIM_ELECTRIC_CURRENT: usize = 5;
pub const DIM_LUMINOUS_INTENSITY: usize = 6;

// Conversion factor offset (indices 7-13)
pub const CONV_OFFSET: usize = 7;

// Rescale value index
pub const RESCALE_INDEX: usize = 14;

/// Unified data structure for physical scales.
///
/// Layout of the 15-element array:
/// - [0..7]  = dimension exponents (L, M, T, t, N, I, Iv)
/// - [7..14] = conversion factors per dimension
/// - [14]    = rescale_value
#[pyclass(skip_from_py_object)]
#[derive(Clone, Debug)]
pub struct PhysicalScale {
    pub data: Array1<f64>,
}

impl Default for PhysicalScale {
    fn default() -> Self {
        Self::new_default()
    }
}

impl PhysicalScale {
    /// Internal constructor with no arguments
    pub fn new_default() -> Self {
        let mut data = Array1::zeros(15);
        for i in CONV_OFFSET..=RESCALE_INDEX {
            data[i] = 1.0;
        }
        Self { data }
    }

    /// Fit scale and dimension - if only one dimension, fold rescale into conversion
    fn fit_scale_and_dimension(
        scale: &PhysicalScale,
        current_rescale: f64,
        factor: f64,
    ) -> (f64, [f64; 7]) {
        let dims = scale.get_dimensions_internal();
        let mut convs = [0.0; 7];
        for i in 0..7 {
            convs[i] = scale.data[CONV_OFFSET + i];
        }

        if dims.len() == 1 {
            // Single dimension: fold factor into conversion
            let idx = dims[0];
            convs[idx] *= current_rescale * factor;
            (1.0, convs)
        } else {
            // Multiple or no dimensions: keep in rescale
            (current_rescale * factor, convs)
        }
    }

    /// Internal helper to get dimensions
    fn get_dimensions_internal(&self) -> Vec<usize> {
        (0..7).filter(|&i| self.data[i] != 0.0).collect()
    }
}

#[pymethods]
impl PhysicalScale {
    /// Create a new PhysicalScale with optional parameters.
    /// Dimension exponents default to 0, conversions default to 1.0, rescale defaults to 1.0.
    #[new]
    #[pyo3(signature = (dimensions=None, conversions=None, rescale_value=None))]
    pub fn new(
        dimensions: Option<PyReadonlyArray1<f64>>,
        conversions: Option<PyReadonlyArray1<f64>>,
        rescale_value: Option<f64>,
    ) -> Self {
        let mut data = Array1::zeros(15);

        // Set dimension exponents (default 0.0)
        if let Some(dims) = dimensions {
            let dims_slice = dims.as_slice().unwrap();
            for (i, &val) in dims_slice.iter().enumerate().take(7) {
                data[i] = val;
            }
        }

        // Set conversion factors (default 1.0)
        for i in CONV_OFFSET..RESCALE_INDEX {
            data[i] = 1.0;
        }
        if let Some(convs) = conversions {
            let convs_slice = convs.as_slice().unwrap();
            for (i, &val) in convs_slice.iter().enumerate().take(7) {
                data[CONV_OFFSET + i] = val;
            }
        }

        // Set rescale value (default 1.0)
        data[RESCALE_INDEX] = rescale_value.unwrap_or(1.0);

        Self { data }
    }

    /// Create from a tuple of (dimensions_tuple, from_base_scale_conversions, rescale_value)
    #[staticmethod]
    pub fn from_components(
        dimensions_tuple: &Bound<'_, PyTuple>,
        from_base_scale_conversions: &Bound<'_, PyTuple>,
        rescale_value: f64,
    ) -> PyResult<Self> {
        let mut data = Array1::zeros(15);

        // Extract dimensions
        for i in 0..7 {
            data[i] = dimensions_tuple.get_item(i)?.extract::<f64>()?;
        }

        // Extract conversions
        for i in 0..7 {
            data[CONV_OFFSET + i] = from_base_scale_conversions.get_item(i)?.extract::<f64>()?;
        }

        // Set rescale value
        data[RESCALE_INDEX] = rescale_value;

        Ok(Self { data })
    }

    /// Create a dimensionless scale with default conversions
    #[staticmethod]
    pub fn dimensionless() -> Self {
        Self::new_default()
    }

    /// Create from a PhysicalDimension, conversion factors, and rescale value.
    #[staticmethod]
    pub fn from_dimension(
        dimension: &PhysicalDimension,
        conversions: &Bound<'_, PyTuple>,
        rescale_value: f64,
    ) -> PyResult<Self> {
        let mut data = Array1::zeros(15);

        // Copy dimension exponents
        let dim_data = dimension.as_array();
        for i in 0..7 {
            data[i] = dim_data[i];
        }

        // Extract conversions
        for i in 0..7 {
            data[CONV_OFFSET + i] = conversions.get_item(i)?.extract::<f64>()?;
        }

        // Set rescale value
        data[RESCALE_INDEX] = rescale_value;

        Ok(Self { data })
    }

    // ==================== Dimension Accessors ====================

    #[getter]
    pub fn length(&self) -> f64 {
        self.data[DIM_LENGTH]
    }

    #[getter]
    pub fn mass(&self) -> f64 {
        self.data[DIM_MASS]
    }

    #[getter]
    pub fn temperature(&self) -> f64 {
        self.data[DIM_TEMPERATURE]
    }

    #[getter]
    pub fn time(&self) -> f64 {
        self.data[DIM_TIME]
    }

    #[getter]
    pub fn amount(&self) -> f64 {
        self.data[DIM_AMOUNT]
    }

    #[getter]
    pub fn electric_current(&self) -> f64 {
        self.data[DIM_ELECTRIC_CURRENT]
    }

    #[getter]
    pub fn luminous_intensity(&self) -> f64 {
        self.data[DIM_LUMINOUS_INTENSITY]
    }

    /// Get the dimension as a PhysicalDimension object.
    #[getter]
    pub fn dimension(&self) -> PhysicalDimension {
        let mut dim_data = [0.0; 7];
        for i in 0..7 {
            dim_data[i] = self.data[i];
        }
        PhysicalDimension::from_array(dim_data)
    }

    /// Get dimension exponent by index
    pub fn get_dimension_exponent(&self, index: usize) -> f64 {
        if index < 7 {
            self.data[index]
        } else {
            0.0
        }
    }

    /// Get the dimensions tuple as a Python tuple
    pub fn dimensions_tuple<'py>(&self, py: Python<'py>) -> Bound<'py, PyTuple> {
        let dims: Vec<f64> = (0..7).map(|i| self.data[i]).collect();
        PyTuple::new(py, dims).unwrap()
    }

    /// Get the from_base_scale_conversions tuple as a Python tuple
    pub fn from_base_scale_conversions<'py>(&self, py: Python<'py>) -> Bound<'py, PyTuple> {
        let convs: Vec<f64> = (0..7).map(|i| self.data[CONV_OFFSET + i]).collect();
        PyTuple::new(py, convs).unwrap()
    }

    /// Get the rescale value
    #[getter]
    pub fn rescale_value(&self) -> f64 {
        self.data[RESCALE_INDEX]
    }

    /// Set rescale value
    #[setter]
    pub fn set_rescale_value(&mut self, value: f64) {
        self.data[RESCALE_INDEX] = value;
    }

    /// Set a conversion factor
    pub fn set_conversion(&mut self, index: usize, value: f64) {
        if index < 7 {
            self.data[CONV_OFFSET + index] = value;
        }
    }

    /// Get a conversion factor
    pub fn get_conversion(&self, index: usize) -> f64 {
        if index < 7 {
            self.data[CONV_OFFSET + index]
        } else {
            1.0
        }
    }

    // ==================== Properties ====================

    /// Calculate the total conversion factor
    #[getter]
    pub fn conversion_factor(&self) -> f64 {
        let mut product = self.data[RESCALE_INDEX];
        for i in CONV_OFFSET..RESCALE_INDEX {
            product *= self.data[i];
        }
        product
    }

    /// Check if scale is dimensionless (all dimension exponents are 0)
    #[getter]
    pub fn is_dimensionless(&self) -> bool {
        for i in 0..7 {
            if self.data[i] != 0.0 {
                return false;
            }
        }
        true
    }

    /// Get list of active dimensions (indices where exponent != 0)
    pub fn get_dimensions(&self) -> Vec<usize> {
        self.get_dimensions_internal()
    }

    // ==================== Linear Algebra Operations ====================

    /// Multiply two scales (for unit multiplication)
    /// - Add dimension exponents (vector addition)
    /// - Multiply conversion factors
    /// - Handle dimension annulation (when exponents cancel to 0)
    pub fn multiply(&self, other: &PhysicalScale) -> PhysicalScale {
        let mut result = PhysicalScale::new_default();
        let mut rescale_factor = 1.0;

        // Process each dimension
        for i in 0..7 {
            // Add exponents
            let new_exp = self.data[i] + other.data[i];
            result.data[i] = new_exp;

            // Multiply conversion factors
            let conv_product = self.data[CONV_OFFSET + i] * other.data[CONV_OFFSET + i];

            // Check for dimension annulation
            if new_exp == 0.0 && (self.data[i] != 0.0 || other.data[i] != 0.0) {
                // Dimension cancelled out, move conversion to rescale
                rescale_factor *= conv_product;
                result.data[CONV_OFFSET + i] = 1.0;
            } else {
                result.data[CONV_OFFSET + i] = conv_product;
            }
        }

        // Handle rescale and fit to single dimension if applicable
        let (new_rescale, new_convs) = Self::fit_scale_and_dimension(
            &result,
            self.data[RESCALE_INDEX],
            rescale_factor,
        );

        result.data[RESCALE_INDEX] = new_rescale;
        for (i, conv) in new_convs.iter().enumerate() {
            result.data[CONV_OFFSET + i] = *conv;
        }

        result
    }

    /// Divide two scales (for unit division)
    /// - Subtract dimension exponents (vector subtraction)
    /// - Divide conversion factors
    pub fn divide(&self, other: &PhysicalScale) -> PhysicalScale {
        let mut result = PhysicalScale::new_default();
        let mut rescale_factor = 1.0;

        // Process each dimension
        for i in 0..7 {
            // Subtract exponents
            let new_exp = self.data[i] - other.data[i];
            result.data[i] = new_exp;

            // Divide conversion factors
            let conv_quotient = self.data[CONV_OFFSET + i] / other.data[CONV_OFFSET + i];

            // Check for dimension annulation
            if new_exp == 0.0 && (self.data[i] != 0.0 || other.data[i] != 0.0) {
                rescale_factor *= conv_quotient;
                result.data[CONV_OFFSET + i] = 1.0;
            } else {
                result.data[CONV_OFFSET + i] = conv_quotient;
            }
        }

        // Handle rescale
        let (new_rescale, new_convs) = Self::fit_scale_and_dimension(
            &result,
            self.data[RESCALE_INDEX],
            rescale_factor,
        );

        result.data[RESCALE_INDEX] = new_rescale;
        for (i, conv) in new_convs.iter().enumerate() {
            result.data[CONV_OFFSET + i] = *conv;
        }

        result
    }

    /// Multiply scale by a scalar value
    pub fn multiply_scalar(&self, scalar: f64) -> PhysicalScale {
        let mut result = self.clone();

        // Get active dimensions
        let dims = self.get_dimensions_internal();

        if dims.len() == 1 {
            // Single dimension: fold scalar into that dimension's conversion
            let idx = dims[0];
            result.data[CONV_OFFSET + idx] *= scalar;
        } else {
            // Multiple or no dimensions: multiply rescale
            result.data[RESCALE_INDEX] *= scalar;
        }

        result
    }

    /// Divide scale by a scalar value
    pub fn divide_scalar(&self, scalar: f64) -> PhysicalScale {
        self.multiply_scalar(1.0 / scalar)
    }

    /// Scalar divided by scale (1/scale * scalar)
    pub fn rdivide_scalar(&self, scalar: f64) -> PhysicalScale {
        let mut result = PhysicalScale::new_default();

        // Negate all dimension exponents
        for i in 0..7 {
            result.data[i] = -self.data[i];
        }

        // Invert all conversion factors
        for i in 0..7 {
            result.data[CONV_OFFSET + i] = 1.0 / self.data[CONV_OFFSET + i];
        }

        // Invert rescale value
        result.data[RESCALE_INDEX] = 1.0 / self.data[RESCALE_INDEX];

        // Handle single dimension case
        let (new_rescale, new_convs) = Self::fit_scale_and_dimension(
            &result,
            result.data[RESCALE_INDEX],
            scalar,
        );

        result.data[RESCALE_INDEX] = new_rescale;
        for (i, conv) in new_convs.iter().enumerate() {
            result.data[CONV_OFFSET + i] = *conv;
        }

        result
    }

    /// Raise scale to a power
    /// - Multiply dimension exponents by power (scalar multiply)
    /// - Raise conversion factors to power
    pub fn power(&self, exp: f64) -> PhysicalScale {
        let mut result = PhysicalScale::new_default();

        // Scale dimension exponents
        for i in 0..7 {
            result.data[i] = self.data[i] * exp;
        }

        // Raise conversion factors to power
        for i in 0..7 {
            result.data[CONV_OFFSET + i] = self.data[CONV_OFFSET + i].powf(exp);
        }

        // Raise rescale to power
        result.data[RESCALE_INDEX] = self.data[RESCALE_INDEX].powf(exp);

        result
    }

    /// Add dimension exponents (for Dimension + Dimension)
    pub fn add_dimensions(&self, other: &PhysicalScale) -> PhysicalScale {
        let mut result = self.clone();
        for i in 0..7 {
            result.data[i] += other.data[i];
        }
        result
    }

    /// Subtract dimension exponents (for Dimension - Dimension)
    pub fn subtract_dimensions(&self, other: &PhysicalScale) -> PhysicalScale {
        let mut result = self.clone();
        for i in 0..7 {
            result.data[i] -= other.data[i];
        }
        result
    }

    /// Multiply dimension exponents by scalar (for Dimension * scalar)
    pub fn multiply_dimensions(&self, scalar: f64) -> PhysicalScale {
        let mut result = self.clone();
        for i in 0..7 {
            result.data[i] *= scalar;
        }
        result
    }

    /// Divide dimension exponents by scalar (for Dimension / scalar)
    pub fn divide_dimensions(&self, scalar: f64) -> PhysicalScale {
        self.multiply_dimensions(1.0 / scalar)
    }

    // ==================== Equality ====================

    /// Check if two scales have the same dimension
    pub fn same_dimension(&self, other: &PhysicalScale) -> bool {
        for i in 0..7 {
            if self.data[i] != other.data[i] {
                return false;
            }
        }
        true
    }

    /// Check if two scales are equal (same dimension AND same conversion factor)
    pub fn equals(&self, other: &PhysicalScale) -> bool {
        self.same_dimension(other) && self.conversion_factor() == other.conversion_factor()
    }

    // ==================== NumPy Interop ====================

    /// Get the internal array as a NumPy array
    pub fn as_numpy<'py>(&self, py: Python<'py>) -> Bound<'py, PyArray1<f64>> {
        self.data.clone().into_pyarray(py)
    }

    /// Create from a NumPy array
    #[staticmethod]
    pub fn from_numpy(arr: PyReadonlyArray1<f64>) -> PyResult<Self> {
        let slice = arr.as_slice()?;
        if slice.len() != 15 {
            return Err(pyo3::exceptions::PyValueError::new_err(
                "Array must have exactly 15 elements",
            ));
        }
        let mut data = Array1::zeros(15);
        for (i, &val) in slice.iter().enumerate() {
            data[i] = val;
        }
        Ok(Self { data })
    }

    // ==================== Serialization ====================

    /// Encode dimension exponents into an i64.
    /// Each exponent uses 4 bits, supporting range -8 to +7.
    pub fn to_dimension_int64(&self) -> i64 {
        let mut result: i64 = 0;

        for i in 0..7 {
            let exp = self.data[i] as i8;
            // Clamp to 4-bit signed range (-8 to +7)
            let clamped = exp.clamp(-8, 7);
            let bits = (clamped & 0x0F) as i64;
            result |= bits << (i * 4);
        }

        result
    }

    /// Decode an i64 into dimension exponents.
    /// Creates a new PhysicalScale with the decoded dimensions and default conversions.
    #[staticmethod]
    pub fn from_dimension_int64(encoded: i64) -> Self {
        let mut scale = PhysicalScale::new_default();

        for i in 0..7 {
            let bits = ((encoded >> (i * 4)) & 0x0F) as i8;
            // Sign extend 4-bit to 8-bit
            let exp = if bits & 0x08 != 0 {
                bits | 0xF0u8 as i8
            } else {
                bits
            };
            scale.data[i] = exp as f64;
        }

        scale
    }

    /// Serialize the full scale to JSON.
    /// Includes all 15 values: 7 dimension exponents, 7 conversion factors, 1 rescale value.
    pub fn to_json(&self) -> String {
        let data_vec: Vec<f64> = self.data.to_vec();
        serde_json::to_string(&data_vec).unwrap_or_else(|_| "[]".to_string())
    }

    /// Deserialize from JSON.
    #[staticmethod]
    pub fn from_json(json_str: &str) -> PyResult<Self> {
        let data_vec: Vec<f64> = serde_json::from_str(json_str)
            .map_err(|e| pyo3::exceptions::PyValueError::new_err(e.to_string()))?;

        if data_vec.len() != 15 {
            return Err(pyo3::exceptions::PyValueError::new_err(
                "JSON array must have exactly 15 elements",
            ));
        }

        let mut scale = PhysicalScale::new_default();
        for (i, &val) in data_vec.iter().enumerate() {
            scale.data[i] = val;
        }

        Ok(scale)
    }

    /// Serialize to a compact dictionary format.
    pub fn to_dict<'py>(&self, py: Python<'py>) -> PyResult<Bound<'py, PyDict>> {
        let dict = PyDict::new(py);

        // Dimensions as list
        let dims: Vec<f64> = (0..7).map(|i| self.data[i]).collect();
        dict.set_item("dimensions", dims)?;

        // Conversions as list
        let convs: Vec<f64> = (0..7).map(|i| self.data[7 + i]).collect();
        dict.set_item("conversions", convs)?;

        // Rescale value
        dict.set_item("rescale", self.data[14])?;

        Ok(dict)
    }

    /// Create from a dictionary.
    #[staticmethod]
    pub fn from_dict(dict: &Bound<'_, PyDict>) -> PyResult<Self> {
        let mut scale = PhysicalScale::new_default();

        // Extract dimensions
        if let Some(dims) = dict.get_item("dimensions")? {
            let dims_list: Vec<f64> = dims.extract()?;
            for (i, &val) in dims_list.iter().enumerate().take(7) {
                scale.data[i] = val;
            }
        }

        // Extract conversions
        if let Some(convs) = dict.get_item("conversions")? {
            let convs_list: Vec<f64> = convs.extract()?;
            for (i, &val) in convs_list.iter().enumerate().take(7) {
                scale.data[7 + i] = val;
            }
        }

        // Extract rescale
        if let Some(rescale) = dict.get_item("rescale")? {
            scale.data[14] = rescale.extract()?;
        }

        Ok(scale)
    }

    // ==================== String Representation ====================

    pub fn __repr__(&self) -> String {
        format!(
            "PhysicalScale(dims={:?}, convs={:?}, rescale={})",
            &self.data.slice(ndarray::s![0..7]).to_vec(),
            &self.data.slice(ndarray::s![7..14]).to_vec(),
            self.data[RESCALE_INDEX]
        )
    }

    pub fn __hash__(&self) -> u64 {
        use std::collections::hash_map::DefaultHasher;
        use std::hash::{Hash, Hasher};

        let mut hasher = DefaultHasher::new();

        // Hash the dimensions
        for i in 0..7 {
            self.data[i].to_bits().hash(&mut hasher);
        }

        // Hash the conversion factor
        self.conversion_factor().to_bits().hash(&mut hasher);

        hasher.finish()
    }
}
