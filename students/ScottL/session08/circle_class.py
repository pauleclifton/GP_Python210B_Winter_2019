
"""
Homework 8 - Circle Class
Use objects and their associated methods for characterizing circles and spheres.
"""

import math


class Circle:
    """Define and quantify properties for circles with a given radius"""

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        """Return the diameter calculated from the radius property."""
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        """Return the area of a circle calculated from the radius property."""
        return math.pi * self.radius ** 2

    @classmethod
    def from_diameter(cls, diameter):
        """Define the object and its radius based an input for the diameter."""
        return cls(diameter / 2)

    def __str__(self):
        return f"Circle with a radius of: {self.radius}"

    def __repr__(self):
        return f"Circle({self.radius})"

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    __rmul__ = __mul__

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius


class Sphere(Circle):
    """Define and calculate member of the sphere class based on the circle class"""

    @property
    def volume(self):
        """Return the volume of a sphere calculated from the radius property."""
        return 4 / 3 * math.pi * self.radius ** 3

    @property
    def area(self):
        """Return the surface area of a sphere calculated from the radius property."""
        return 4 * math.pi * self.radius ** 2

    def __str__(self):
        return f"Sphere with a radius of: {self.radius}"

    def __repr__(self):
        return f"Sphere({self.radius})"

    def __add__(self, other):
        return Sphere(self.radius + other.radius)

    def __mul__(self, other):
        return Sphere(self.radius * other)

    __rmul__ = __mul__
