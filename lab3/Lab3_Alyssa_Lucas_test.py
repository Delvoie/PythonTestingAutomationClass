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
    expected = pi * 2 ** 2
    if abs(result - expected) < 1e-6:
        print("Test passed: Circle area with radius 2")
    else:
        print(f"Test failed: Expected {expected:.4f}, got {result}")

    # Test invalid input
    try:
        result = calculate_circle_area("test")
        print("Test failed: Should have raised TypeError")
    except TypeError as e:
        if str(e) == "Radius must be a number":
            print("Test passed: Invalid input handling")
        else:
            print(f"Test failed: Wrong error message: {e}")

    # Test negative radius
    try:
        result = calculate_circle_area(-1)
        print("Test failed: Should have raised ValueError")
    except ValueError as e:
        if str(e) == "Radius must be non-negative":
            print("Test passed: Negative radius handling")
        else:
            print(f"Test failed: Wrong error message: {e}")

    # Test large radius
    result = calculate_circle_area(10**6)
    expected = pi * (10**6) ** 2
    if abs(result - expected) < 1e-4:
        print("Test passed: Circle area with large radius")
    else:
        print(f"Test failed: Expected {expected}, got {result}")


if __name__ == "__main__":
    main()