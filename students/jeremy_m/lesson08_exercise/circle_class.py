import math


class Circle():
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return 'A circle with a radius of {}'.format(self.radius)

    def __repr__(self):
        return 'Circle({})'.format(self.radius)


    # Binary operators defined here
    def __add__(self, other):
        try:
            return self.radius + other.radius
        except AttributeError:
            return self.radius + other

    def __radd__(self, other):
        return self.radius + other

    def __mul__(self, other):
        try:
            return self.radius * other.radius
        except AttributeError:
            return self.radius * other

    def __rmul__(self, other):
        return self.radius * other
    # Binary operators end

    # Comparison operators defined here
    def __lt__(self, other):
        try:
            return self.radius < other.radius
        except AttributeError:
            return self.radius < other

    def __le__(self, other):
        try:
            return self.radius <= other.radius
        except AttributeError:
            return self.radius <= other

    def __eq__(self, other):
        try:
            return self.radius == other.radius
        except AttributeError:
            return self.radius == other

    def __ge__(self, other):
        try:
            return self.radius >= other.radius
        except AttributeError:
            return self.radius >= other

    def __gt__(self, other):
        try:
            return self.radius > other.radius
        except AttributeError:
            return self.radius > other
    # Comparison operators end

    @property
    def diameter(self):
        """ Calculates the diameter based on given radius """
        return self.radius * 2

    @diameter.setter
    def diameter(self, new_value):
        """ Sets the diameter based on the radius """
        self.radius = new_value // 2

    @property
    def area(self):
        """ Calculates the area of the circle """
        return math.pi * (self.radius ** 2)

    @classmethod
    def from_diameter(cls, diameter):
        """ Instantiates an instance of a circle from its diameter """
        return cls(diameter // 2)



class Sphere(Circle):
    def __str__(self):
        return 'A sphere with a radius of {}'.format(self.radius)

    def __repr__(self):
        return 'Sphere({})'.format(self.radius)

    @property
    def volume(self):
        """ Calculates the volume of the sphere """
        return round((4 / 3) * math.pi * (self.radius ** 3), 2)

    @property
    def area(self):
        """ Calculates the surface area of the sphere """
        return round(4 * math.pi * (self.radius ** 2), 2)