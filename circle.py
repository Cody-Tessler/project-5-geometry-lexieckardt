from shape import Shape
import math

class Circle(Shape):

    def __init__(self, r):
        """
        Constructs a Circle object

        :param r: float -> radius of circle
        """
        self.check_if_args_not_below_zero(r)
        self.r = r

    def get_area(self):
        """
        Calculates Circle area using formula (pi)(r ** 2)
        
        :return: float -> area of circle
        """
        return (math.pi * (self.r ** 2))

    def get_perimeter(self):
        """
        Calculates Circle perimeter using formula 2(pi)(r)
        
        :return: float -> perimeter of circle
        """
        return (2 * math.pi * self.r)

    def __str__(self):
        return f"Circle,  r={self.r} "

    @classmethod
    def get_area_formula(cls):
        """
        Returns area formula for Circle as a string.
        
        :return: string
        """
        return "pi(r**2)"

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns perimeter formula for Circle as a string.
        
        :return: string
        """
        return "2 * pi * r"
