"""This module defines the Shape class."""

__author__ = "Navkaran Singh Singh"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class Shape(ABC):
    """
    class Shape: Maintains shape data.

    """    
    def __init__(self, color: str):
        """
        Initializes the class attributes with argument values.
        Args: 
           Color: Represents the color of the shape.

        Raises:
            ValueError: When color is blank.

        """
        if len(color.strip()) == 0:
            raise ValueError("Color cannot be blank.")
        else:
            self._color = color

        
    def __str__(self):
        return f"The shape color is {self._color}."

    @abstractmethod
    def calculate_area(self) -> float:
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        pass