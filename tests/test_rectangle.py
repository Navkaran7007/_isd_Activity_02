"""This module defines the TestRectangle class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_rectangle.py
"""

__author__ = "Navkaran Singh Sidhu"
__version__ = "1.0.0"

import unittest
from shape.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle("Green", 9, 10)

    def test_init_valid_argument_attributes_set(self):
        rectangle = Rectangle("Green", 9, 10)
               
        self.assertEqual("Green", rectangle._color)
        self.assertEqual(9, rectangle._Rectangle__length)
        self.assertEqual(10, rectangle._Rectangle__width)

    def test_init_blank_color_raises_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(" ", 9, 10)

    def test_init_non_integer_lenght_raises_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle("Green", "Nine", 10)
    
    def test_init_non_integer_width_raises_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle("Green", 9, "Ten")

    def test_str_valid_rectangle_class_returns_formatted_string(self):
        expected = (f"The shape color is Green."
                   + f"\nThis rectangle has four sides "
                   + f"with the lengths of 9, 10, 9 and 10 centimeters.")
        
        self.assertEqual(expected, str(self.rectangle))

    def test_calculate_area_returns_calculated_value(self):
        self.rectangle = Rectangle("Green", 9, 10)
        expected = 90

        self.assertEqual(expected, round(self.rectangle.calculate_area(), 2))

    def test_calculate_perimeter_returns_calculated_value(self):
        self.rectangle = Rectangle("Green", 9, 10)
        expected = 38

        self.assertEqual(expected, self.rectangle.calculate_perimeter())

