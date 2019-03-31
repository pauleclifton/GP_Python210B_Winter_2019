#!/usr/bin/env python3
#pylint: disable=E1101

""" Circle class """

# Douglas Klos
# March 4th, 2019
# Python 210, Session 8
# circle.py


import math


class Circle():
    """
    Circle class

    Properties:
    radius      The radius of the circle
    diameter    Returns the diameter calculated from radius
    area        Returns the area calculated from radius
    """

    def __init__(self, radius=0):
        self._radius = radius

    def __lt__(self, other):
        return self._radius < other.radius

    def __le__(self, other):
        return self._radius <= other.radius

    def __eq__(self, other):
        return self._radius == other.radius

    def __ge__(self, other):
        return self._radius >= other.radius

    def __gt__(self, other):
        return self._radius > other.radius

    def __ne__(self, other):
        return self._radius != other.radius

    def __str__(self):
        return f'Circle with radius: {self.radius}'

    def __repr__(self):
        return f'Circle({self.radius})'

    def __add__(self, other):
        if hasattr(other, '_radius'):
            return self.__class__(self._radius + other.radius)
        return self.__class__(self.radius + other)

    def __radd__(self, other):
        return self.__class__(other + self.radius)

    def __iadd__(self, other):
        if hasattr(other, '_radius'):
            return self.__class__(self._radius + other.radius)
        return self.__class__(self.radius + other)

    def __sub__(self, other):
        if hasattr(other, '_radius'):
            return self.__class__(self._radius - other.radius)
        return self.__class__(self.radius - other)

    def __rsub__(self, other):
        return self.__class__(other - self._radius)

    def __isub__(self, other):
        if hasattr(other, '_radius'):
            return self.__class__(self._radius - other.radius)
        return self.__class__(self.radius - other)

    def __mul__(self, other):
        if hasattr(other, '_radius'):
            return self.__class__(self._radius * other.radius)
        return self.__class__(self.radius * other)

    def __rmul__(self, other):
        return self.__class__(other * self._radius)

    def __imul__(self, other):
        if hasattr(other, '_radius'):
            return self.__class__(self._radius * other.radius)
        return self.__class__(self.radius * other)

    def __truediv__(self, other):
        if hasattr(other, '_radius'):
            return self.__class__(self._radius / other.radius)
        return self.__class__(self.radius / other)

    def __rtruediv__(self, other):
        return self.__class__(other / self._radius)

    def __itruediv__(self, other):
        if hasattr(other, '_radius'):
            return self.__class__(self._radius / other.radius)
        return self.__class__(self.radius / other)

    def __floordiv__(self, other):
        if hasattr(other, '_radius'):
            return self.__class__(self._radius // other.radius)
        return self.__class__(self.radius // other)

    def __rfloordiv__(self, other):
        return self.__class__(other // self._radius)

    def __ifloordiv__(self, other):
        if hasattr(other, '_radius'):
            return self.__class__(self._radius // other.radius)
        return self.__class__(self.radius // other)

    @property
    def radius(self):
        """ Sets or returns the radius """
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @radius.deleter
    def radius(self):
        del self._radius

    @property
    def diameter(self):
        """ Returns the diameter calculated from radius """
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        self._radius = .5 * value

    @property
    def area(self):
        """ Returns the area calculated from radius """
        return 2 * math.pi * self.radius ** 2

    @classmethod
    def from_diameter(cls, diameter):
        """ Initializes class from diameter instead of radius """
        self = cls()
        self.radius = diameter * .5
        return self


class Sphere(Circle):
    """ Sphere class, inherits from Circle """

    def __str__(self):
        return f'Sphere with radius: {self.radius}'

    def __repr__(self):
        return f'Sphere({self.radius})'

    @Circle.area.getter
    def area(self):
        """ Returns the area of the sphere """
        return 4 * math.pi * self.radius ** 2

    @property
    def volume(self):
        """ Returns the Volume of the sphere """
        return (4/3) * math.pi * self.radius ** 3
