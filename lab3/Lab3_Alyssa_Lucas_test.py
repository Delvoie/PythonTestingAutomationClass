"""
Date: Oct 28, 2025
Name: "test_Lab3_Alyssa_Lucas.py"
Programmer: Alyssa and Lucas
Description: 
unit tests for Shape Area Calculator (Lab3).
Uses unittest framework with menu-driven test suite selection (case-insensitive).
Tests: valid, zero, float, negative, invalid type, large values for ALL shapes.
Runs ONLY tests for selected shape with setUp/tearDown fixtures.
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

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.valid_radius = 5
        self.zero_radius = 0
        self.float_radius = 3.14
        self.negative_radius = -1
        self.invalid_type = "invalid"
        self.large_radius = 10000.0
        print(f"\n--- Setting up Circle test ---")

    def tearDown(self):
        """Clean up after each test method."""
        print(f"--- Circle test completed ---")

    def test_valid_positive(self):
        """Test circle area with valid positive radius."""
        result = calculate_circle_area(self.valid_radius)
        expected = pi * self.valid_radius ** 2
        self.assertAlmostEqual(result, expected, places=12)

    def test_zero_radius(self):
        """Test circle area with zero radius."""
        result = calculate_circle_area(self.zero_radius)
        self.assertEqual(result, 0.0)

    def test_float_radius(self):
        """Test circle area with float radius."""
        result = calculate_circle_area(self.float_radius)
        expected = pi * (self.float_radius ** 2)
        self.assertAlmostEqual(result, expected, places=12)

    def test_negative_radius(self):
        """Test circle area with negative radius raises ValueError."""
        self.assertRaises(ValueError, calculate_circle_area, self.negative_radius)

    def test_invalid_type(self):
        """Test circle area with invalid type raises TypeError."""
        self.assertRaises(TypeError, calculate_circle_area, self.invalid_type)

    def test_large_radius(self):
        """Test circle area with large radius."""
        result = calculate_circle_area(self.large_radius)
        expected = pi * (self.large_radius ** 2)
        self.assertAlmostEqual(result, expected, places=12)


# Trapezium tests
class TestTrapezium(unittest.TestCase):
    """Unit tests for calculate_trapezium_area."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.valid_base = 10
        self.valid_top = 20
        self.valid_height = 5
        self.zero_height = 0
        self.float_base = 10.5
        self.float_top = 20.3
        self.float_height = 5.1
        self.negative_base = -10
        self.negative_top = -20
        self.negative_height = -5
        self.invalid_type = "10"
        self.large_base = 10000
        self.large_top = 20000
        self.large_height = 5000
        print(f"\n--- Setting up Trapezium test ---")

    def tearDown(self):
        """Clean up after each test method."""
        print(f"--- Trapezium test completed ---")

    def test_valid_trapezium(self):
        """Test trapezium area with valid dimensions."""
        result = calculate_trapezium_area(self.valid_base, self.valid_top, self.valid_height)
        self.assertEqual(result, 75.0)

    def test_zero_height(self):
        """Test trapezium area with zero height."""
        result = calculate_trapezium_area(self.valid_base, self.valid_top, self.zero_height)
        self.assertEqual(result, 0.0)

    def test_float_dimensions(self):
        """Test trapezium area with float dimensions."""
        result = calculate_trapezium_area(self.float_base, self.float_top, self.float_height)
        self.assertAlmostEqual(result, 0.5 * (self.float_base + self.float_top) * self.float_height, places=12)

    def test_negative_base(self):
        """Test trapezium area with negative base raises ValueError."""
        self.assertRaises(ValueError, calculate_trapezium_area, self.negative_base, self.valid_top, self.valid_height)

    def test_negative_top(self):
        """Test trapezium area with negative top raises ValueError."""
        self.assertRaises(ValueError, calculate_trapezium_area, self.valid_base, self.negative_top, self.valid_height)

    def test_negative_height(self):
        """Test trapezium area with negative height raises ValueError."""
        self.assertRaises(ValueError, calculate_trapezium_area, self.valid_base, self.valid_top, self.negative_height)

    def test_invalid_type_base(self):
        """Test trapezium area with invalid type raises TypeError."""
        self.assertRaises(TypeError, calculate_trapezium_area, self.invalid_type, self.valid_top, self.valid_height)

    def test_large_values(self):
        """Test trapezium area with large values."""
        result = calculate_trapezium_area(self.large_base, self.large_top, self.large_height)
        self.assertEqual(result, 75000000.0)


# Ellipse tests
class TestEllipse(unittest.TestCase):
    """Unit tests for calculate_ellipse_area."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.valid_major = 10
        self.valid_minor = 5
        self.zero_minor = 0
        self.float_major = 9.2
        self.float_minor = 4.7
        self.negative_major = -10
        self.negative_minor = -5
        self.invalid_type = "5"
        self.large_major = 10000.0
        self.large_minor = 5000.0
        print(f"\n--- Setting up Ellipse test ---")

    def tearDown(self):
        """Clean up after each test method."""
        print(f"--- Ellipse test completed ---")

    def test_valid_ellipse(self):
        """Test ellipse area with valid axes."""
        result = calculate_ellipse_area(self.valid_major, self.valid_minor)
        expected = pi * self.valid_major * self.valid_minor
        self.assertAlmostEqual(result, expected, places=12)

    def test_zero_minor(self):
        """Test ellipse area with zero minor axis."""
        result = calculate_ellipse_area(self.valid_major, self.zero_minor)
        self.assertEqual(result, 0.0)

    def test_float_axes(self):
        """Test ellipse area with float axes."""
        result = calculate_ellipse_area(self.float_major, self.float_minor)
        expected = pi * self.float_major * self.float_minor
        self.assertAlmostEqual(result, expected, places=12)

    def test_negative_major(self):
        """Test ellipse area with negative major axis raises ValueError."""
        self.assertRaises(ValueError, calculate_ellipse_area, self.negative_major, self.valid_minor)

    def test_negative_minor(self):
        """Test ellipse area with negative minor axis raises ValueError."""
        self.assertRaises(ValueError, calculate_ellipse_area, self.valid_major, self.negative_minor)

    def test_invalid_type(self):
        """Test ellipse area with invalid type raises TypeError."""
        self.assertRaises(TypeError, calculate_ellipse_area, self.valid_major, self.invalid_type)

    def test_large_axes(self):
        """Test ellipse area with large axes."""
        result = calculate_ellipse_area(self.large_major, self.large_minor)
        expected = pi * self.large_major * self.large_minor
        self.assertAlmostEqual(result, expected, places=12)


# Rhombus tests
class TestRhombus(unittest.TestCase):
    """Unit tests for calculate_rhombus_area."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.valid_diagonal1 = 10
        self.valid_diagonal2 = 20
        self.zero_diagonal = 0
        self.float_diagonal1 = 10.5
        self.float_diagonal2 = 20.3
        self.negative_diagonal1 = -10
        self.negative_diagonal2 = -20
        self.invalid_type = "20"
        self.large_diagonal1 = 10000
        self.large_diagonal2 = 20000
        print(f"\n--- Setting up Rhombus test ---")

    def tearDown(self):
        """Clean up after each test method."""
        print(f"--- Rhombus test completed ---")

    def test_valid_rhombus(self):
        """Test rhombus area with valid diagonals."""
        result = calculate_rhombus_area(self.valid_diagonal1, self.valid_diagonal2)
        self.assertEqual(result, 100.0)

    def test_zero_diagonal1(self):
        """Test rhombus area with zero diagonal."""
        result = calculate_rhombus_area(self.zero_diagonal, self.valid_diagonal2)
        self.assertEqual(result, 0.0)

    def test_float_diagonals(self):
        """Test rhombus area with float diagonals."""
        result = calculate_rhombus_area(self.float_diagonal1, self.float_diagonal2)
        self.assertAlmostEqual(result, 0.5 * self.float_diagonal1 * self.float_diagonal2, places=12)

    def test_negative_diagonal1(self):
        """Test rhombus area with negative diagonal1 raises ValueError."""
        self.assertRaises(ValueError, calculate_rhombus_area, self.negative_diagonal1, self.valid_diagonal2)

    def test_negative_diagonal2(self):
        """Test rhombus area with negative diagonal2 raises ValueError."""
        self.assertRaises(ValueError, calculate_rhombus_area, self.valid_diagonal1, self.negative_diagonal2)

    def test_invalid_type(self):
        """Test rhombus area with invalid type raises TypeError."""
        self.assertRaises(TypeError, calculate_rhombus_area, self.valid_diagonal1, self.invalid_type)

    def test_large_diagonals(self):
        """Test rhombus area with large diagonals."""
        result = calculate_rhombus_area(self.large_diagonal1, self.large_diagonal2)
        self.assertEqual(result, 100000000.0)


# Run test depending on shape selected
def run_tests(shape):
    """Load and run test suite for selected shape."""
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner(verbosity=2)

    if shape == 'c':
        suite = loader.loadTestsFromTestCase(TestCircle)
        print("\n ⬤ Running Circle Tests...")
    elif shape == 't':
        suite = loader.loadTestsFromTestCase(TestTrapezium)
        print("\n ⏢ Running Trapezium Tests...")
    elif shape == 'e':
        suite = loader.loadTestsFromTestCase(TestEllipse)
        print("\n 💫 Running Ellipse Tests...")
    elif shape == 'r':
        suite = loader.loadTestsFromTestCase(TestRhombus)
        print("\n 🕳️ Running Rhombus Tests...")
    else:
        return

    result = runner.run(suite)
    print(f"\nTests passed: {result.testsRun - len(result.failures) - len(result.errors)} / {result.testsRun}")


# Menu shape selection
def main():
    """Main function to run menu-driven test suite."""
    print("\n" + "="*60)
    print(" "*15 + "Area of a Shape Tester")
    print(" "*18 + "by Alyssa and Lucas")
    print("="*60)
    choice = ""

    while choice != "q":
        print("\n📋 Select shape to test:")
        # Prompt user for menu
        print("  [C] Circle")
        print("  [T] Trapezium")
        print("  [E] Ellipse")
        print("  [R] Rhombus")
        print("  [A] All Shapes")
        print("  [Q] Quit")
        print("-"*60)
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
            print("-"*60)
            for shape in ['c', 't', 'e', 'r']:
                run_tests(shape)
            print("-"*60)
        # If q exit program
        elif choice == 'q':
            print("-"*60)
            print(" "*18 + "Exiting Shape Tester...")
            print("-"*60)
        # Restart loop
        else:
            print("\nInvalid choice. Please enter a valid letter.")


# Start the program
if __name__ == "__main__":
    main()