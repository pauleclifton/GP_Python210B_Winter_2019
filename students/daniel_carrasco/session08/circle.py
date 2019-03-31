import math


class Circle(object):
    pi = math.pi

    def __init__(self, the_radius):
        self.radius = the_radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @property
    def area(self):
        return self.pi * (self.radius)**2

    @area.setter
    def area(self, diameter):
        if input:
            print('Attribute Error')  # How do I do this correctly

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    def __str__(self):
        return f'Circle with a radius of {self.radius}'

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.radius!r})')

    def __add__(self, c2):
        print(f'Summing {self} + {c2}')
        print(c2.radius)
        return Circle(self.radius + c2.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return Circle(self.radius * other)

    def __iadd__(self, other):
        return Circle(self.radius + other)

    def __imul__(self, other):
        return Circle(self.radius * other)

    def __lt__(self, other):
        if self.radius < other.radius:
            return True
        else:
            return False

    def __le__(self, other):
        if self.radius <= other.radius:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.radius != other.radius:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.radius > other.radius:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.radius >= other.radius:
            return True
        else:
            return False


class Sphere(Circle):

    def __str__(self):
        return f'Sphere with a radius of {self.radius}'

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.radius!r})')

    @property
    def volume(self):
        return 4 / 3 * self.pi * self.radius**3


