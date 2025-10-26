# Date: Oct 20, 2025
# Name: "App for claculating area of shapes Lab3"
# Programmer: Alyssa and Lucas
# Description: 

# imports 
from math import pi

#----------------------------
# Shape 1: CIRCLE

radii = [2, 3, "ada", -1, 4.5, 2, 6, 24, 12, 52, 100]

def circle_area(r):
    if not isinstance(r, (int, float)) or r < 0:
        return("Radius must be a positive number")
    return pi * (r ** 2)
    
circle_area_message = "Area of circle with radius = {radius:.2f} is {area:.2f}"

for radius in radii:
    C_A = circle_area(radius)
    if isinstance(C_A, (int, float)):
        print(circle_area_message.format(radius=radius, area=C_A))
    else:
        print(f"Error for radius {radius}: {C_A}")
# ---------------------------


#----------------------------
# Shape 2: Trapezium

trapezium_sides = {
    "Trapezium_base" :   [2,3,-1, "a"],
    "Trapezium_roof" :   [2,3,12, "3"],
    "Trapezium_height" : [2,3,-6, "0"]
}

def trapezium_area(Trapezium_base, Trapezium_roof, Trapezium_height):
    if not isinstance(Trapezium_base, (int, float)) or Trapezium_base < 0:
        return("Base must be a positive number")
    if not isinstance(Trapezium_roof, (int, float)) or Trapezium_roof < 0:
        return("Roof must be a positive number")
    if not isinstance(Trapezium_height, (int, float)) or Trapezium_height < 0:
        return("Height must be a positive number")
    return ((Trapezium_roof + Trapezium_base) / 2) * Trapezium_height

trapezium_area_message = "Area of trapeziums with base = {Trapezium_base:.2f}, roof = {Trapezium_roof:.2f}, height = {Trapezium_height:.2f} is {area:.2f}"

for base, roof, height in zip(trapezium_sides["Trapezium_base"], trapezium_sides["Trapezium_roof"], trapezium_sides["Trapezium_height"]):
    T_A = trapezium_area(base, roof, height)
    if isinstance(T_A, (int, float)):
        print(trapezium_area_message.format(Trapezium_base=base, Trapezium_roof=roof, Trapezium_height=height, area=T_A))
    else:
        print(f"Error for trapezium with base {base}, roof {roof}, height {height}: {T_A}")
# ---------------------------



#----------------------------
# Shape 3: Ellipse

ellipse_dimensions = {
    "Ellipse_major_axis" : [4,5],
    "Ellipse_minor_axis" : [2,3]
}

def ellipse_area(Ellipse_major_axis, Ellipse_minor_axis):
    if not isinstance(Ellipse_major_axis, (int, float)) or Ellipse_major_axis < 0:
        return("Major axis must be a positive number")
    if not isinstance(Ellipse_minor_axis, (int, float)) or Ellipse_minor_axis < 0:
        return("Minor axis must be a positive number")
    return pi * Ellipse_major_axis * Ellipse_minor_axis

ellipse_area_message = "Area of ellipses with major axis = {Ellipse_major_axis:.2f}, minor axis = {Ellipse_minor_axis:.2f} is {area:.2f}"

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
        return("Diagonal 1 must be a positive number")
    if not isinstance(Rhombus_diagonal2, (int, float)) or Rhombus_diagonal2 < 0:
        return("Diagonal 2 must be a positive number")
    return (Rhombus_diagonal1 * Rhombus_diagonal2) / 2

rhombus_area_message = "Area of rhombus with diagonal1 = {Rhombus_diagonal1:.2f}, diagonal2 = {Rhombus_diagonal2:.2f} is {area:.2f}"

for diagonal1, diagonal2 in zip(rhombus_diagonals["Rhombus_diagonal1"], rhombus_diagonals["Rhombus_diagonal2"]):
    R_A = rhombus_area(diagonal1, diagonal2)
    print(rhombus_area_message.format(Rhombus_diagonal1=diagonal1, Rhombus_diagonal2=diagonal2, area=R_A))
#----------------------------