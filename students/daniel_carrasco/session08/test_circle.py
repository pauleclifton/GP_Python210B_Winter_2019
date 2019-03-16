import io
import pytest
import math

from circle import *


def test_init():
    """
    This only tests that it can be initialized with and without
    some content -- but it's a start
    """
    c = Circle(4)


def test_radius():
    "check to see if it outputs correct radius"
    c = Circle(5)
    # making sure radius outputs correctly.
    assert c.radius == 5


def test_diameter():
    "check to see if it outputs correct diameter"
    c = Circle(5)
    # making sure radius outputs correctly.
    assert c.diameter == 10
    assert c.diameter == c.radius * 2
    c.diameter = 6
    assert c.radius == 3
    assert c.diameter == 6


def test_from_diameter():
    "test to see if it still calculates using diameter"
    t = Circle.from_diameter(5)
    assert t.radius == 2.5
    assert t.diameter == 5


def test_str_repr():
    "test to see if __str__ and __repr__ methods work"
    a = str(Circle(4))
    b = repr(Circle(5))
    c = str(Sphere(3))
    d = repr(Sphere(2))
    assert a == 'Circle with a radius of 4'
    assert b == 'Circle(5)'
    assert c == 'Sphere with a radius of 3'
    assert d == 'Sphere(2)'


def test_lo():
    "test to see if logical operators work for class"
    a = Circle(1)
    b = Circle(2)
    c = Circle(1)
    assert b > a
    assert a < b
    assert a == c
    assert b >= a
    assert a <= b
    assert a != b


def test_rmul_mul():
    "test to see if you can multiply the class, and at any order"
    a = Circle(2)
    b = 3 * a
    c = a * 4
    assert b.radius == 6
    assert c.radius == 8


def test_mult_add():
    "test to see if you can multiply and add classes together"
    a = Circle(5)
    b = Circle(5)
    assert a.radius + b.radius == 10
    assert a.radius * b.radius == 25


def test_volume():
    "test to see if volume of sphere calculations work"
    a = Sphere(2)
    b = Sphere.from_diameter(2)
    assert a.volume == 4 / 3 * math.pi * 2**3
    assert b.volume == 4 / 3 * math.pi * 1**3


def test_area():
    'test to see if area method works'
    a = Circle(7)
    b = Circle.from_diameter(4)
    assert a.area == math.pi * 7**2
    assert b.area == math.pi * 2**2
