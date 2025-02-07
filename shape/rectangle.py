"""This module defines the Rectangle class."""

__author__ = "Navkaran Singh Sidhu"
__version__ = "1.0.0"

from shape.shape import Shape

class Rectangle(Shape):
    """
    A sub-class representing a rectangle, inherited from Shape

    """
    def __init__(self, color: str,
                  length: int, 
                  width: int):
        """
        Initializes the class attributes with argument values.
        Args: 
            Length (int): Length of triangle.
            Width (int): Width of triangle.

        Raises:
            ValueError: When length and width are non-numeric.        

        """
        super().__init__(color)
    
        if isinstance(length, int):
                self.__length = length
        else:
            raise ValueError("Lenght must be numeric.")
    
        if isinstance(width, int):
            self.__width = width
        else:
            raise ValueError("Widht must be numeric.")
        
    def __str__(self) ->str:
        value = super().__str__()
        value += (f"\nThis rectangle has four sides with the"
                  f" lengths of {self.__length}, {self.__width},"
                  f" {self.__length} and {self.__width} centimeters.")
        return value
        
    def calculate_area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle, 
            calculated as the product of its length and width.
            
        """
        area = self.__length * self.__width
        return area
    
    def calculate_perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle, 
            calculated as the product of its length and width.

        """
        perimeter = self.__length * 2 + self.__width * 2
        return perimeter
