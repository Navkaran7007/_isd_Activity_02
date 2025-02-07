"""This module defines the Triangle class."""

__author__ = "Navkaran Singh SIdhu"
__version__ = "1.0.0"

from shape.shape import Shape

class Triangle(Shape):
    """
    
    """
    def __init__(self, side_1 : int,
                       side_2 : int,
                       side_3 : int):
        """
        Initializes the class attributes with argument values.
        Args: 
            side_1 (int): Length of first side of triangle.
            side_2 (int): Length of second side of triangle.
            side_3 (int): Length of third side of triangle.

        Raises:
            ValueError: 
        
        """
        super().__init__(color)
        if isinstance(side_1, int):
            self.side_1 = side_1
        else:
            raise ValueError("Side 1 must be numeric.")
        
        if isinstance(side_2, int):
            self.side_2 = side_2
        else:
            raise ValueError("Side 2 must be numeric.")
        
        if isinstance(side_1, int):
            self.side_2 = side_2
        else:
            raise ValueError("Side 3 must be numeric.")
        
        