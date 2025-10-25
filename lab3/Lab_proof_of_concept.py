# Date: Oct 20, 2025
# Name: "App for claculating area of shapes Lab3"
# Programmer: Alyssa and Lucas
# Description: 

# imports 
from math import pi

#----------------------------
# Shape 1: CIRCLE

radii = [2, 3]

def circle_area(r):
    if not isinstance(r, (int, float)) or r < 0:
        raise ValueError("Radius must be a positive number")
    return pi * (r ** 2)

circle_area_message = "Area of circles with radius = {radius} is {area}"


for radius in radii:
    C_A = circle_area(radius)
    print(circle_area_message.format(radius=radius, area=C_A))
# ---------------------------


#----------------------------
# Shape 2: Trapezium

trapezium_sides = {
    "Trapezium_base" : [2,3],
    "Trapezium_roof" : [2,3],
    "Trapezium_height" : [2,3]
}

def trapezium_area(Trapezium_base, Trapezium_roof, Trapezium_height):
    if not isinstance(Trapezium_base, (int, float)) or Trapezium_base < 0:
        raise ValueError("Base must be a positive number")
    if not isinstance(Trapezium_roof, (int, float)) or Trapezium_roof < 0:
        raise ValueError("Roof must be a positive number")
    if not isinstance(Trapezium_height, (int, float)) or Trapezium_height < 0:
        raise ValueError("Height must be a positive number")
    return ((Trapezium_roof + Trapezium_base) / 2) * Trapezium_height

trapezium_area_message = "Area of trapeziums with base = {Trapezium_base}, roof = {Trapezium_roof}, height = {Trapezium_height} is {area}"

for base, roof, height in zip(trapezium_sides["Trapezium_base"], trapezium_sides["Trapezium_roof"], trapezium_sides["Trapezium_height"]):
    T_A = trapezium_area(base, roof, height)
    print(trapezium_area_message.format(Trapezium_base=base, Trapezium_roof=roof, Trapezium_height=height, area=T_A))
# ---------------------------



#----------------------------
# Shape 3: Ellipse

ellipse_dimensions = {
    "Ellipse_major_axis" : [4,5],
    "Ellipse_minor_axis" : [2,3]
}

def ellipse_area(Ellipse_major_axis, Ellipse_minor_axis):
    if not isinstance(Ellipse_major_axis, (int, float)) or Ellipse_major_axis < 0:
        raise ValueError("Major axis must be a positive number")
    if not isinstance(Ellipse_minor_axis, (int, float)) or Ellipse_minor_axis < 0:
        raise ValueError("Minor axis must be a positive number")
    return pi * Ellipse_major_axis * Ellipse_minor_axis

ellipse_area_message = "Area of ellipses with major axis = {Ellipse_major_axis}, minor axis = {Ellipse_minor_axis} is {area}"

for major_axis, minor_axis in zip(ellipse_dimensions["Ellipse_major_axis"], ellipse_dimensions["Ellipse_minor_axis"]):
    E_A = ellipse_area(major_axis, minor_axis)
    print(ellipse_area_message.format(Ellipse_major_axis=major_axis, Ellipse_minor_axis=minor_axis, area=E_A))
# ---------------------------


#----------------------------
# Shape 4: Rhombus

rhombus_diagonals = {
    "Rhombus_diagonal1" : [3,4],
    "Rhombus_diagonal2" : [2,5]
}
def rhombus_area(Rhombus_diagonal1, Rhombus_diagonal2):
    if not isinstance(Rhombus_diagonal1, (int, float)) or Rhombus_diagonal1 < 0:
        raise ValueError("Diagonal 1 must be a positive number")
    if not isinstance(Rhombus_diagonal2, (int, float)) or Rhombus_diagonal2 < 0:
        raise ValueError("Diagonal 2 must be a positive number")
    return (Rhombus_diagonal1 * Rhombus_diagonal2) / 2

rhombus_area_message = "Area of rhombus with diagonal1 = {Rhombus_diagonal1}, diagonal2 = {Rhombus_diagonal2} is {area}"

for diagonal1, diagonal2 in zip(rhombus_diagonals["Rhombus_diagonal1"], rhombus_diagonals["Rhombus_diagonal2"]):
    R_A = rhombus_area(diagonal1, diagonal2)
    print(rhombus_area_message.format(Rhombus_diagonal1=diagonal1, Rhombus_diagonal2=diagonal2, area=R_A))
#----------------------------