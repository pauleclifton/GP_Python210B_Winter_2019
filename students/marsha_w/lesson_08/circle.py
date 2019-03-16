'''
Title: Circle exercise
Dev: Marsha Wheeler
Date: 3/10/2019
'''


import math


class Circle(object):

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2

    @property
    def area(self):
        area = (self.diameter / 2)**2 * math.pi
        return area

    @classmethod
    def from_diameter(cls, diameter):
        cls.diameter = diameter
        cls.radius = diameter / 2.0
        return cls

    def __add__(self, other):
        sumC = self.radius + other.radius
        return sumC

    def __mul__(self, val):
        mulC = self.radius * val
        return mulC

    def __rmul__(self, other):
        mulC = self.radius * other
        return mulC

    def __lt__(self, other):
        return self.radius < other.radius

    def __repr__(self):
        return 'Circle({})'.format(self.radius)

    def __str__(self):
        return 'A circle with radius a of {} and diameter of {}'.format(self.radius, self.diameter)


