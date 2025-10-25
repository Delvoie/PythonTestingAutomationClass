# Date: Oct 20, 2025
# Name: "App for unit testing Lab3"
# Programmer: Alyssa and Lucas
# Description: 

# imports 
from math import pi

def circle_area(r):
    return pi* (r**2)

radius = [2,0,-3, 2 + 5, True, "radius" ]
message = f"Area of a circle with r= {radius} is {circle_area}"

# Start a program 
def main_function():
    for r in radius:
        A = circle_area(r)
        print(message.format(radius=r, area=A))

# Start the program
if __name__ == "__main__":
    main_function()
