"""This module defines the Triangle class."""

__author__ = "Navkaran Singh Sidhu"
__version__ = "1.0.0"

import math
from shape.shape import Shape

class Triangle(Shape):
    """
    A sub-class representing a triangle, inherited from Shape.

    """
    def __init__(self, color : str,
                       side_1 : int,
                       side_2 : int,
                       side_3 : int):
        """
        Initializes the class attributes with argument values.
        Args: 
            side_1 (int): Length of first side of triangle.
            side_2 (int): Length of second side of triangle.
            side_3 (int): Length of third side of triangle.

        Raises:
            ValueError: When side 1,side 2, side 3
                        is non-numeric.
                        and when the sides do not satisfy the 
                        Triangle Inequality Theorem.
        
        """
        super().__init__(color)

        if isinstance(side_1, int):
            self.__side_1 = side_1
        else:
            raise ValueError("Side 1 must be numeric.")
        
        if isinstance(side_2, int):
            self.__side_2 = side_2
        else:
            raise ValueError("Side 2 must be numeric.")
        
        if isinstance(side_3, int):
            self.__side_3 = side_3
        else:
            raise ValueError("Side 3 must be numeric.")

        if  not ((side_1 + side_2 > side_3) and \
                (side_1 + side_3 > side_2) and \
                (side_2 + side_3 > side_1)):
            raise ValueError("The sides do not satisfy the Triangle Inequality Theorem.")
        
    def __str__(self) ->str:
        """
        Returns a string representation of the class instance.

        Returns:
            str: The Triangle instance formatted as a string.
            
        """
        value = super().__str__()
        value += (f"\nThis triangle has three sides with lengths of {self.__side_1}, "
          + f"{self.__side_2} and {self.__side_3} centimeters.")
        return value
    
    def calculate_area(self):
        """
        Calculates the area of the triangle .

        Returns:
            float: The area of the triangle.
        """
        semi_perimeter = (self.__side_1 + self.__side_2 + self.__side_3) / 2
        area = math.sqrt(semi_perimeter * 
                     (semi_perimeter - self.__side_1) *
                     (semi_perimeter - self.__side_2) *
                     (semi_perimeter - self.__side_3))
        return area
    
    def calculate_perimeter(self):
        """
        Calculates the perimeter of the triangle .
        
        Returns:
            float: The perimeter of the triangle.
        """
        perimeter = self.__side_1 + self.__side_2 + self.__side_3
        return perimeter
        
       