'''
##########################
#Python 210
#Session 08 - Circle Exercise
#Elaine Xu
#Mar 5, 2019
###########################
'''
import math
#############################
#Step 1 create class called circle
#############################
class Circle(object):
    def __init__(self, radius):
        self.radius = radius

#############################
#Step 2 add diameter property
#############################
    @property
    def diameter(self):
        print("in getter")
        return self.radius * 2

#############################
# Step 3 set up diameter property setter
#############################
    @diameter.setter
    def diameter(self, value):
        print("in setter", value)
        self.radius = value / 2

#############################
# Step 4 add an area property
#############################
    @property
    def area(self):
        return math.pi * self.radius**2

#############################
# Step 5 add an alternate constructor that create circle directly with the diameter
#############################
    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter/2
        return cls(radius)

#############################
# Step 6 add __str__ and __repr__ methods
#############################
    def __str__(self):
        return "Circle with radius: " + str(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)

#############################
# Step 7 add numerical protocol
#############################
    def __add__(self, other):
        return (self.radius + other.radius)

    def __mul__(self, val):
        try:
            return (self.radius * val)
        except TypeError:
            __rmul__(self, val)

    def __rmul__(self, val):
        return (self.radius * val)

#############################
# Step 8 add ability to compare two circles
#############################
    def __eq__(self, other):
        return (self.radius == other.radius)

    def __lt__(self, other):
        return (self.radius < other.radius)

    def __iadd__(self, other):
        return self.radius + other.radius

    def __imul__(self, val):
        return self.radius * val

#############################
# Step 9 sphere subclassing
#############################
class Sphere(Circle):
    def __str__(self):
        return "Sphere with radius: " + str(self.radius)

    def __repr__(self):
        return "Sphere({})".format(self.radius)

    @property
    def volume(self):
        return 4/3 * math.pi * self.radius**3

    @property
    def area(self):
        raise NotImplementedError


