# Date: Oct 20, 2025
# Name: "App for claculating area of shapes Lab3"
# Programmer: Alyssa and Lucas
# Description: 

# imports 
from Lab3_Alyssa_Lucas_app import calculate_circle_area
from math import pi

def main():
    test_circle()


def test_circle():
    # Test valid radius
    result = calculate_circle_area(2)
    expected = round(pi * 2 ** 2, 2)
    if result - expected:
        print("Test passed: Circle area with radius 2")
    else:
        print(f"Test failed: Expected {expected:.4f}, got {result}")

    # Test invalid input
    result = calculate_circle_area("ada")
    if result == "Radius must be a number":
        print("Test passed: Invalid input handling")
    else:
        print(f"Test failed: Expected error message, got {result}")

    # Test negative radius
    result = calculate_circle_area(-1)
    if result == "Radius must be non-negative":
        print("Test passed: Negative radius handling")
    else:
        print(f"Test failed: Expected error message, got {result}")


if __name__ == "__main__":
    main()