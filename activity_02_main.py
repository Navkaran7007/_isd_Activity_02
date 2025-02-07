""""A client program written to verify correctness of the activity 
classes.
"""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Navkaran Singh Sidhu"

from shape import *
def main():
    """Test the functionality of the methods encapsulated 
    in this project.
    """

    # In the statements coded below, ensure that any statement that 
    # could result in an exception is handled.  When exceptions are 
    # 'caught', display the exception message to the console.

    # *** PART 1 ***
    print("*************PART 1****************")

    # 1. Create an empty list of Shape objects.
    shape=[]

    # 2. Code a statement which creates an instance of the Triangle 
    # class.
    # Append the Triangle to the list of shapes.
    try:
        triangle_1=Triangle("Green", 9, 10, 11)
        shape.append(triangle_1)
    except Exception as e:
        print(f"\nUnexpected Error : {e}")

    # 3. Code a statement which creates an instance of the Rectangle 
    # class.
    # Append the Rectangle to the list of shapes.
    try:
        rectangle_1=Rectangle("Green", 9, 10)
        shape.append(rectangle_1)
    except Exception as e:
        print(f"\nUnexpected Error : {e}")


    # 4. Code 3 additional statements which creates an instance of 
    # Triangle or Rectangle classes (your choice).
    # Append these instances to the list of shapes.
    # invalid input values
    try:
        triangle_2=Triangle("Green", 9, 1, 11)
        shape.append(triangle_2)
    except Exception as e:
        print(f"\nUnexpected Error : {e}")

    # 5. Iterate through the list of shapes.  
    # On each iteration:
    # - print the shape
    # - print the area of the shape to 2 decimal places
    # - print the perimeter of the shape to 2 decimal places
    for shapes in shape:
        print(f"\nShape: {shapes}")
        print("Area:", round(shapes.calculate_area(), 2), "cm")
        print("Perimeter:", round(shapes.calculate_perimeter(), 2), "cm\n")

    # *** END PART 1 ***
    print("*************PART 2****************")

if __name__ == "__main__":
    main()