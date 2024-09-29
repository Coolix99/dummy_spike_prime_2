# math.py

import math

e = math.e
pi = math.pi

def acos(x):
    """
    Returns the inverse cosine of x.

    Args:
        x (float): A number in the range [-1, 1].

    Returns:
        float: The inverse cosine of x, in radians.
    """
    return math.acos(x)

def acosh(x):
    """
    Returns the inverse hyperbolic cosine of x.

    Args:
        x (float): A number greater than or equal to 1.

    Returns:
        float: The inverse hyperbolic cosine of x.
    """
    return math.acosh(x)

def asin(x):
    """
    Returns the inverse sine of x.

    Args:
        x (float): A number in the range [-1, 1].

    Returns:
        float: The inverse sine of x, in radians.
    """
    return math.asin(x)

def asinh(x):
    """
    Returns the inverse hyperbolic sine of x.

    Args:
        x (float): Any real number.

    Returns:
        float: The inverse hyperbolic sine of x.
    """
    return math.asinh(x)

def atan(x):
    """
    Returns the inverse tangent of x.

    Args:
        x (float): Any real number.

    Returns:
        float: The inverse tangent of x, in radians.
    """
    return math.atan(x)

def atan2(y, x):
    """
    Returns the principal value of the inverse tangent of y/x.

    Args:
        y (float): The y-coordinate.
        x (float): The x-coordinate.

    Returns:
        float: The angle between the positive x-axis and the point (x, y), in radians.
    """
    return math.atan2(y, x)

# Continue implementing other functions similarly...
