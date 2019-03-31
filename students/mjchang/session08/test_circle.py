"""
test code for circle.py
"""
from circle import *
import pytest
import math

#### Step 1 ####

def test_radius():
    c = Circle(4)
    assert c.radius == 4

#### Step 2 ####

def test_diameter():
    c = Circle(4)
    assert c.diameter == 8

#### Step 3 ####

def test_set_diameter():
    c = Circle(4)
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1

#### Step 4 ####

def test_area():
    c = Circle(2)
    assert round(c.area, 6) == 12.566371

    with pytest.raises(AttributeError):
        c.area = 12.56637


#### Step 5 ####
def test_alt_construct():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4


#### Step 6 ####
def test_print():
    c = Circle(4)
    d = eval(repr(c))
    assert d == c
    assert c.__str__() == "Circle with radius: 4"
    assert c. __repr__() == "Circle(4)"


#### Step 7 ####
def test_add():
    c1 = Circle(2)
    c2 = Circle(4)
    assert c1 + c2 == Circle(6)

def test_multiply():
    c1 = Circle(2)
    c2 = Circle(4)
    assert c2 * 3 == Circle(12)



#### Step 8 ####
def test_compare_circles():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(4)
    assert (c1 > c2) == False
    assert (c1 < c2) == True
    assert (c1 == c2) == False
    assert (c2 == c3) == True


    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0),
               Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]

    circles.sort()

    assert circles == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4),
                       Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]

#### Step 9 ####
def test_sphere():
    s = Sphere(4)
    assert s.__str__() == "Sphere with radius: 4"
    assert s.__repr__() == "Sphere(4)"
    assert s.volume == 4/3 * math.pi * 4**3
    assert s.area == 4 * math.pi * 4**2

