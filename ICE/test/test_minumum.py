# Date: Oct 29, 2025
# Name: "test_Minimum.py - ICE3 Test"
# Programmer: Lucas
# Description: Unit test to find the minimum value in a list of integers

import sys
import os
# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from app.minumum import find_minimum

class Test_Minumum (unittest.TestCase):
    
    def test_case_1(self):
        self.assertEqual(find_minimum(self), 90)
        find_minimum([180, 200, 90, 91])
        print("test_case_1 passed")

    def test_case_2(self):
        self.assertEqual(len(find_minimum([])), 0)
        find_minimum([])
        self.assertRaises(ValueError, find_minimum, [])
        


if __name__ == '__main__':
    unittest.main()