#!/usr/bin/env python3

import math

"""
Framework for a circular object.
Validation prevents user from entering a 
negative radius value.
"""


class Circle(object):
    instances = []

    def __init__(self, radius):
        if radius < 0:
            raise ValueError('It is not possible for a radius to be less than zero.')
        else:
            self.radius = radius
        self._radius = radius
        Circle.instances.append(self)

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    # make area non-settable
    @property
    def area(self):
        return math.pi * pow(self.radius, 2)

    # method to create a circle with the diameter
    @classmethod
    def from_diameter(cls, value):
        radius = value / 2
        return cls(radius)

    # simple add method
    def __add__(self, other):
        new_radius = self.radius + other.radius
        return new_radius

    # augmented assignment add method
    def __iadd__(self, other):
        new_radius =  self.radius + other.radius
        return new_radius

    # augmented assigment exponential method
    def __ipow__(self, other):
        new_radius = self.radius ** other
        return new_radius

    # multiplication method
    def __mul__(self, other):
        new_radius = self.radius * other
        return new_radius

    # allow for reversal of arguments
    __rmul__ = __mul__

    # less than comparison
    def __lt__(self, other):
        return self.radius < other.radius

    # greater than comparison
    def __gt__(self, other):
        return self.radius > other.radius

    # equality method
    def __eq__(self, other):
        return self.radius == other.radius

    # non-equality method
    def __ne__(self, other):
        return self.radius != other.radius

    def __repr__(self):
        return f'Circle with radius of {self.radius}'

    def __str__(self):
        return f'Circle with radius of {self.radius}'


class Sphere(Circle):
    """
    Sublclass of Circle
    """

    # override Circle volume method
    def volume(self):
        return (4 / 3) * math.pi * (self.radius ** 3)

    # override Circle area method
    def area(self):
        return 4 * math.pi * (self.radius ** 2)

    def __repr__(self):
        return f'Sphere with radius of {self.radius} volume of ' \
            f'{self.volume()} & surface area of {self.area()}'

    def __str__(self):
        return f'Sphere with radius of {self.radius} volume of ' \
            f'{self.volume()} & surface area of {self.area()}'

c1 = Circle(4)
c2 = Circle(2)
c3 = Circle(c1 + c2)
print(c3)



