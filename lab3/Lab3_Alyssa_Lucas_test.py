"""
Date: Oct 28, 2025
Name: "test_Lab3_Alyssa_Lucas.py"
Programmer: Alyssa and Lucas
Description: 
Comprehensive unit tests for Shape Area Calculator (Lab3).
Uses unittest framework with menu-driven test suite selection (case-insensitive).
Tests: valid, zero, float, negative, invalid type, large values for ALL shapes.
Runs ONLY tests for selected shape. All cases HARDcoded for automation.
"""

import unittest
from math import pi
from Lab3_Alyssa_Lucas_app import (
    calculate_circle_area,
    calculate_trapezium_area,
    calculate_ellipse_area,
    calculate_rhombus_area
)

# Circle tests
class TestCircle(unittest.TestCase):
    """Unit tests for calculate_circle_area."""

    def test_valid_positive(self):
        result = calculate_circle_area(5)
        expected = pi * 25
        self.assertAlmostEqual(result, expected, places=12)

    def test_zero_radius(self):
        result = calculate_circle_area(0)
        self.assertEqual(result, 0.0)

    def test_float_radius(self):
        result = calculate_circle_area(3.14)
        expected = pi * (3.14 ** 2)
        self.assertAlmostEqual(result, expected, places=12)

    def test_negative_radius(self):
        self.assertRaises(ValueError, calculate_circle_area, -1)

    def test_invalid_type(self):
        self.assertRaises(TypeError, calculate_circle_area, "invalid")

    def test_large_radius(self):
        r = 10000.0
        result = calculate_circle_area(r)
        expected = pi * (r ** 2)
        self.assertAlmostEqual(result, expected, places=12)

# Trapezium tests
class TestTrapezium(unittest.TestCase):
    """Unit tests for calculate_trapezium_area."""

    def test_valid_trapezium(self):
        result = calculate_trapezium_area(10, 20, 5)
        self.assertEqual(result, 75.0)

    def test_zero_height(self):
        result = calculate_trapezium_area(10, 20, 0)
        self.assertEqual(result, 0.0)

    def test_float_dimensions(self):
        result = calculate_trapezium_area(10.5, 20.3, 5.1)
        self.assertAlmostEqual(result, 0.5 * (10.5 + 20.3) * 5.1, places=12)

    def test_negative_base(self):
        self.assertRaises(ValueError, calculate_trapezium_area, -10, 20, 5)

    def test_negative_top(self):
        self.assertRaises(ValueError, calculate_trapezium_area, 10, -20, 5)

    def test_negative_height(self):
        self.assertRaises(ValueError, calculate_trapezium_area, 10, 20, -5)

    def test_invalid_type_base(self):
        self.assertRaises(TypeError, calculate_trapezium_area, "10", 20, 5)

    def test_large_values(self):
        result = calculate_trapezium_area(10000, 20000, 5000)
        self.assertEqual(result, 75000000.0)

# Ellipse tests
class TestEllipse(unittest.TestCase):
    """Unit tests for calculate_ellipse_area."""

    def test_valid_ellipse(self):
        result = calculate_ellipse_area(10, 5)
        expected = pi * 10 * 5
        self.assertAlmostEqual(result, expected, places=12)

    def test_zero_minor(self):
        result = calculate_ellipse_area(10, 0)
        self.assertEqual(result, 0.0)

    def test_float_axes(self):
        result = calculate_ellipse_area(9.2, 4.7)
        expected = pi * 9.2 * 4.7
        self.assertAlmostEqual(result, expected, places=12)

    def test_negative_major(self):
        self.assertRaises(ValueError, calculate_ellipse_area, -10, 5)

    def test_negative_minor(self):
        self.assertRaises(ValueError, calculate_ellipse_area, 10, -5)

    def test_invalid_type(self):
        self.assertRaises(TypeError, calculate_ellipse_area, 10, "5")

    def test_large_axes(self):
        a, b = 10000.0, 5000.0
        result = calculate_ellipse_area(a, b)
        expected = pi * a * b
        self.assertAlmostEqual(result, expected, places=12)

# Rhombus tests
class TestRhombus(unittest.TestCase):
    """Unit tests for calculate_rhombus_area."""

    def test_valid_rhombus(self):
        result = calculate_rhombus_area(10, 20)
        self.assertEqual(result, 100.0)

    def test_zero_diagonal1(self):
        result = calculate_rhombus_area(0, 20)
        self.assertEqual(result, 0.0)

    def test_float_diagonals(self):
        result = calculate_rhombus_area(10.5, 20.3)
        self.assertAlmostEqual(result, 0.5 * 10.5 * 20.3, places=12)

    def test_negative_diagonal1(self):
        self.assertRaises(ValueError, calculate_rhombus_area, -10, 20)

    def test_negative_diagonal2(self):
        self.assertRaises(ValueError, calculate_rhombus_area, 10, -20)

    def test_invalid_type(self):
        self.assertRaises(TypeError, calculate_rhombus_area, 10, "20")

    def test_large_diagonals(self):
        d1, d2 = 10000, 20000
        result = calculate_rhombus_area(d1, d2)
        self.assertEqual(result, 100000000.0)

# Run test depending on shape selected
def run_tests(shape):
    """Load and run test suite for selected shape."""
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner(verbosity=2)

    if shape == 'c':
        suite = loader.loadTestsFromTestCase(TestCircle)
        print("\n Running Circle Tests...")
    elif shape == 't':
        suite = loader.loadTestsFromTestCase(TestTrapezium)
        print("\n Running Trapezium Tests...")
    elif shape == 'e':
        suite = loader.loadTestsFromTestCase(TestEllipse)
        print("\n Running Ellipse Tests...")
    elif shape == 'r':
        suite = loader.loadTestsFromTestCase(TestRhombus)
        print("\n Running Rhombus Tests...")
    else:
        return

    result = runner.run(suite)
    print(f"✅ Tests passed: {result.testsRun - len(result.failures) - len(result.errors)} / {result.testsRun}")

# Menu shape selection
def main():
    print("Area of a Shape Tester ")
    choice = ""

    while choice != "q":
        print("\n📋 Select shape to test:")
        #prompt user for menu
        print("- 'c' for testing area of circle")
        print("- 't' for testing area of trapezium")
        print("- 'e' for testing area of ellipse")
        print("- 'r' for testing area of rhombus")
        print("- 'a' for testing all shapes")
        print("- 'q' to quit")
        choice = input("Enter choice: ").lower().strip()
    

        # If c test circle functions
        if choice == "c":
            run_tests('c')
        # If t test trapezium functions
        elif choice == "t":
            run_tests('t')
        # If e test ellipse functions
        elif choice == "e":
            run_tests('e')
        # If r test rhombus functions
        elif choice == "r":
            run_tests('r')
        # If a test all functions
        elif choice == "a":
            for shape in ['c', 't', 'e', 'r']:
                run_tests(shape)
        # If q exit program
        elif choice == 'q':
            print("Exiting Shape Tester...")
        # Restart loop
        else:
            print("Invalid choice. Please enter a valid letter.")

# Start the program

if __name__ == "__main__":
    main()