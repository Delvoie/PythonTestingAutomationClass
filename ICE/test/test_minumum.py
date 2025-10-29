# Date: Oct 29, 2025
# Name: "test_Minimum.py - ICE3 Test"
# Programmer: Lucas
# Description: Unit test to find the minimum value in a list of integers

import sys
import os
# Add the current directory to a Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from ..app.minumum import find_minimum

class TestMinimum(unittest.TestCase):
    #Test Case 1: A very short list (of inputs) with the size of 1, 2, or 3 elements.
    def test_case_1(self):
        self.assertEqual(find_minimum([180, 200, 90, 91]), 90, "Should be 90")

    #Test Case 2: An empty list i.e., of size 0.
    def test_case_2(self):
        self.assertRaises(ValueError, find_minimum, [])

    #Test Case 3: A list where the minimum element is the first or last element.
    def test_case_3(self):
        self.assertEqual(find_minimum([180, 200, 90, 90]), 90, "Should be 90")

    #Test Case 4: A list where the minimum element is negative.
    def test_case_4(self):
        self.assertEqual(find_minimum([-21, -10, 1]), -21, "Should be -21")


if __name__ == '__main__':
    unittest.main()