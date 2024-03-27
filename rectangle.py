from shape import Shape

class Rectangle(Shape):

    def __init__(self, a, b):
        """
        Constructs a Rectangle object

        :param a: float -> a side length of square
        :param b: float -> b side length of square
        """
        self.check_if_args_not_below_zero(a, b)
        self.a = a
        self.b = b

    def get_area(self):
        """
        Calculates Rectangle area using formula (a * b)
        
        :return: float -> area of rectangle
        """
        return(self.a * self.b)

    def get_perimeter(self):
        """
        Calculates Rectangle perimeter using formula (2a + 2b)
        
        :return: float -> perimeter of rectangle
        """
        return (2*self.a + 2*self.b)

    def __str__(self):
        return f"Rectangle, a={self.a}, b={self.b}"

    @classmethod
    def get_area_formula(cls):
        """
        Returns area formula for Rectangle as a string.
        
        :return: string
        """
        return "a * b"

    @classmethod
    def get_perimeter_formula(cls):
        r"""
        Returns perimeter formula for Rectangle as a string.
        
        :return: string
        """
        return "2*a + 2*b"
