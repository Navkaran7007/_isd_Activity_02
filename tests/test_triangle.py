"""This module defines the TestTriangle class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_triangle.py
"""

__author__ = "Navkaran Singh Sidhu"
__version__ = "1.0.0"

import unittest
from shape.triangle import Triangle

class TestTraingle(unittest.TestCase):
    def setUp(self):
        self.traingle = Triangle("Green", 9, 10, 11)
    def test_init_valid_arguments_attributes_set(self):
        
        triangle = Triangle("Green", 9, 10, 11)
               
        self.assertEqual("Green", triangle._color)
        self.assertEqual(9, triangle._Triangle__side_1)
        self.assertEqual(10, triangle._Triangle__side_2)
        self.assertEqual(11, triangle._Triangle__side_3)

    def test_init_blank_color_raises_value_error(self):
        with self.assertRaises(ValueError):
            Triangle(" ", 9, 10, 11)

    def test_init_side_1_not_integer_raises_value_error(self):
        with self.assertRaises(ValueError):
            Triangle("Green", "Nine", 10, 11)

    def test_init_side_2_not_integer_raises_value_error(self):
        with self.assertRaises(ValueError):
            Triangle("Green", 9, "Ten", 11)

    def test_init_side_3_not_integer_raises_value_error(self):
        with self.assertRaises(ValueError):
            Triangle("Green", 9, 10, "Eleven")

    def test_str_valid_traingle_class_returns_formatted_string(self):
        expected = (f"The shape color is Green."
                   f"\nThis triangle has three sides with" 
                   f" lengths of 9, 10 and 11 centimeters.")
        
        self.assertEqual(expected, str(self.traingle))

    def test_calculate_area_returns_correct_value(self):
        self.triangle = Triangle("Green", 9, 10, 11)
        expected = 42.43

        self.assertAlmostEqual(expected, round(self.triangle.calculate_area(), 2))

    def test_calculate_perimeter_returns_correct_value(self):
        self.triangle = Triangle("Green", 9, 10, 11)
        expected = 30

        self.assertEqual(expected, round(self.triangle.calculate_perimeter(), 2))
        
    def test_init_triangle_Inequality_theorem_raises_value_error(self):
        with self.assertRaises(ValueError):
            Triangle("Green", 9, 1, 11)
