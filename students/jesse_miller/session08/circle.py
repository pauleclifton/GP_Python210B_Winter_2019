#!/usr/bin/env python3
'''
Class based circle calculation exercise
'''

from math import pi
'''
Imported the math module for calculation
'''

class Circle():
    '''
    Defining the circle class
    '''
    def __init__(self, radius):

        self.radius = radius

    @property
    def diameter(self):
        '''
        Defining diameter, I think I'm doing this right.
        '''
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        '''
        This seems like the right time to use a setter
        '''
        self.radius = value / 2

    @property
    def area(self):
        '''
        Defining area, I'm a tad more confident in this one
        '''
        return pi * self.radius**2

    @classmethod
    def from_diameter(cls, value):
        '''
        Attempting to do step five from the assignment, create a circle from
        entering the diameter, not the radius.
        '''
        return cls(value/2)


    def __str__(self):
        return f'{self.__class__.__name__} with radius: {self.radius}'


    def __repr__(self):
        return f'{self.__class__.__name__}({self.radius})'


    def __add__(self, other):
        return self.radius + other.radius


    def __rmul__(self, value):
        return self.radius * value


    def __mul__(self, value):
        try:
            return self.radius * value
        except TypeError:
            #pylint: disable=E0602
            '''
            I have no idea why this works, but is getting a linter error over
            unassigned variables.
            '''
            rmul(self, value)


    def __rtruediv__(self, value):
        return self.radius / value


    def __truediv__(self, value):
        try:
            return self.radius / value
        except TypeError:
            #pylint: disable=E0602
            '''
            I have no idea why this works, but is getting a linter error over
            unassigned variables.
            '''
            rdiv(self, value)


    def __lt__(self, other):
        if self.radius < other.radius:
            return True
        return False


    def __gt__(self, other):
        if self.radius < other.radius:
            return True
        return False


    def __eq__(self, other):
        if self.radius == other.radius:
            return True
        return False


    def sort_var(self):
        '''
        This one wants a doc string for sorting, so this method sorts
        '''
        return self.radius


    @staticmethod
    def __sort__(circle_list):
        return circle_list.sort(key=Circle.sort_var)


'''
-------------------------------------------------------------------------------
'''

class Sphere(Circle):
    '''
    Here goes spheres, we'll see how that works
    '''
    @property
    def area(self):
        '''
        Calculating the area of the sphere
        '''
        try:
            return 4 * pi * self.radius ** 2
        except NotImplementedError:
            print("This is not implemented")


    @property
    def volume(self):
        '''
        Determining the volume of said sphere, geometry isn't my strong suit
        so I'm basically assuming that the math is right here.
        '''
        return 4 / 3 * pi * self.radius ** 3
