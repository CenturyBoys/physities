"""Custom exceptions for the physities library.

This module defines a hierarchy of exceptions for handling errors related to
physical quantities, dimensions, units, and conversions.
"""


class PhysitiesError(Exception):
    """Base exception for all physities errors.

    All custom exceptions in the physities library inherit from this class,
    allowing users to catch all physities-related errors with a single except clause.
    """

    pass


class DimensionMismatchError(PhysitiesError):
    """Raised when an operation is attempted on quantities with incompatible dimensions.

    This error occurs when trying to add, subtract, or convert between units
    that have different physical dimensions.

    Examples:
        - Adding meters to seconds
        - Converting velocity to mass
        - Comparing length with time
    """

    def __init__(self, dim1, dim2, operation: str = "operation"):
        self.dim1 = dim1
        self.dim2 = dim2
        self.operation = operation
        message = f"Cannot perform {operation}: dimensions do not match ({dim1} vs {dim2})"
        super().__init__(message)


class InvalidConversionError(PhysitiesError):
    """Raised when a unit conversion cannot be performed.

    This error occurs when attempting to convert a quantity to an incompatible
    unit type or when the conversion target is invalid.

    Examples:
        - Converting to a non-unit type
        - Converting between incompatible unit systems
    """

    def __init__(self, source_type, target_type, reason: str = None):
        self.source_type = source_type
        self.target_type = target_type
        self.reason = reason
        if reason:
            message = f"Cannot convert {source_type} to {target_type}: {reason}"
        else:
            message = f"Cannot convert {source_type} to {target_type}"
        super().__init__(message)


class InvalidOperationError(PhysitiesError):
    """Raised when an invalid mathematical operation is attempted.

    This error occurs when an operation is not supported for the given operand types.

    Examples:
        - Multiplying a unit by a non-numeric type
        - Dividing by an incompatible type
        - Adding a Unit class (not instance) to another
    """

    def __init__(self, operation: str, operand_type, allowed_types: tuple = None):
        self.operation = operation
        self.operand_type = operand_type
        self.allowed_types = allowed_types
        if allowed_types:
            allowed_str = ", ".join(t.__name__ for t in allowed_types)
            message = f"Cannot perform {operation} with {operand_type}: allowed types are {allowed_str}"
        else:
            message = f"Cannot perform {operation} with {operand_type}"
        super().__init__(message)


class InvalidPowerError(PhysitiesError):
    """Raised when an invalid power/exponentiation operation is attempted.

    This error occurs when:
    - Raising a quantity to a non-numeric power
    - Attempting fractional powers that would result in invalid dimensions

    Examples:
        - Meter ** "two"
        - Taking the square root of a dimension with odd exponents (in some contexts)
    """

    def __init__(self, base_type, power, reason: str = None):
        self.base_type = base_type
        self.power = power
        self.reason = reason
        if reason:
            message = f"Cannot raise {base_type} to power {power}: {reason}"
        else:
            message = f"Cannot raise {base_type} to power {power}: exponent must be int or float"
        super().__init__(message)


class InvalidScaleError(PhysitiesError):
    """Raised when a Scale is constructed with invalid parameters.

    This error occurs when:
    - Conversion factors contain invalid values (zero, negative, or NaN)
    - Dimension tuple has wrong length
    - Rescale value is invalid
    """

    def __init__(self, parameter: str, value, reason: str = None):
        self.parameter = parameter
        self.value = value
        self.reason = reason
        if reason:
            message = f"Invalid Scale parameter '{parameter}' = {value}: {reason}"
        else:
            message = f"Invalid Scale parameter '{parameter}' = {value}"
        super().__init__(message)


class InvalidDimensionError(PhysitiesError):
    """Raised when a Dimension is constructed with invalid parameters.

    This error occurs when:
    - Dimension tuple has wrong length
    - Dimension values are not numeric
    """

    def __init__(self, message: str):
        super().__init__(message)
