# Date: Oct 29, 2025
# Name: "test_Minimum.py - ICE3 Test"
# Programmer: Lucas
# Description: Unit test to find the minimum value in a list of integers

import sys
import os
# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from app.minumum import find_minimum  # Fixed: minumum -> minimum

class Test_Minimum(unittest.TestCase):  # Fixed: Test_Minumum -> Test_Minimum
    
    def test_case_1(self):
        self.assertEqual(find_minimum([180, 200, 90, 91]), 90, "Should be 90")

    def test_case_2(self):
        # Fixed: Removed incorrect assertEqual with len()
        # Use assertRaises to verify ValueError is raised for empty list
        self.assertRaises(ValueError, find_minimum, [])


if __name__ == '__main__':
    unittest.main()