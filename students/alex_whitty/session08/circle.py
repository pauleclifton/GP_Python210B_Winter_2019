#!/usr/bin/env python3

import math

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2


    @property
    def area(self):
        return math.pi * self.radius**2

    @classmethod
    def from_diameter(cls, diameter):
        """ Initializes class from diameter instead of radius """
        return cls(diameter / 2)


    def __str__(self):
        return "Circle with radius: " + str(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __add__(self, other):
        return "Circle({})".format(self.radius + other.radius)

    def __mul__(self, other):
        return "Circle({})".format(self.radius * other)

    __rmul__ = __mul__

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius


class Sphere(Circle):
    """ Sphere class, inherits from Circle """

    @property
    def area(self):
        """ Returns the area of the sphere """
        return 4 * math.pi * self.radius ** 2

    @property
    def volume(self):
        """ Returns the Volume of the sphere """
        return (4/3) * math.pi * self.radius ** 3

    def __str__(self):
        return "Sphere with a radius of: " + str(self.radius)

    def __repr__(self):
        return "Sphere({})".format(self.radius)
