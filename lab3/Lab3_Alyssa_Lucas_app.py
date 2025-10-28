# Date: Oct 27, 2025
# Name: "Shape Area Calculator - Lab3"
# Programmer: Alyssa and Lucas
# Description: Application to calculate areas of Circle, Trapezium, Ellipse, and Rhombus
#              with comprehensive input validation and user-friendly interface

# imports 
from math import pi


#----------------------------
# Shape 1: CIRCLE

def calculate_circle_area(radius):
    """Calculate the area of a circle given its radius."""
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return pi * radius ** 2

# ---------------------------


#----------------------------
# Shape 2: Trapezium

def calculate_trapezium_area(base, top, height):
    """Calculate the area of a trapezium given its parallel sides and height."""
    if not all(isinstance(x, (int, float)) for x in [base, top, height]):
        raise TypeError("All dimensions must be numbers")
    if any(x < 0 for x in [base, top, height]):
        raise ValueError("All dimensions must be non-negative")
    return 0.5 * (base + top) * height

# ---------------------------


#----------------------------
# Shape 3: Ellipse

def calculate_ellipse_area(major_axis, minor_axis):
    """Calculate the area of an ellipse given its major and minor axes."""
    if not all(isinstance(x, (int, float)) for x in [major_axis, minor_axis]):
        raise TypeError("All dimensions must be numbers")
    if any(x < 0 for x in [major_axis, minor_axis]):
        raise ValueError("All dimensions must be non-negative")
    return pi * major_axis * minor_axis

# ---------------------------


#----------------------------
# Shape 4: Rhombus

def calculate_rhombus_area(diagonal1, diagonal2):
    """Calculate the area of a rhombus given its diagonals."""
    if not all(isinstance(x, (int, float)) for x in [diagonal1, diagonal2]):
        raise TypeError("All diagonals must be numbers")
    if any(x < 0 for x in [diagonal1, diagonal2]):
        raise ValueError("All diagonals must be non-negative")
    return 0.5 * diagonal1 * diagonal2

#----------------------------

