"""
Implement this class.
Recall that every square is a rectangle.
Therefore the Square class should inherit from the Rectangle class.
Do NOT implement the get_area() and get_perimeter() methods here.
Those methods should be inherited from the parent class.
"""
from rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, a):
        """
        Constructs a Square object

        :param a: float -> side length of square
        """
        self.check_if_args_not_below_zero(a)
        self.a = a

    def __str__(self):
        return "TODO"

    @classmethod
    def get_area_formula(cls):
        return "TODO"

    @classmethod
    def get_perimeter_formula(cls):
        return "TODO"
