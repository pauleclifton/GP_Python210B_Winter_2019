""" Tests for circle_class.py """

import pytest
from circle_class import *
import math


def test_basic_circle():
    """ Test if a circle can be instantiated and basic parameters are set properly """
    c1 = Circle(10)
    assert c1.radius == 10
    assert c1.diameter == 20


def test_set_radius():
    """ Tests setting the radius """
    c1 = Circle(10)
    c1.radius = 20

    assert c1.radius == 20


def test_set_diameter():
    """
    Tests setting the diameter and checks to ensure radius is calculated
    accurately.
    """
    c1 = Circle(10)

    c1.diameter = 100
    assert c1.radius == 50
    assert c1.diameter == 100


def test_area():
    """ Tests the circle area function """
    c1 = Circle(10)

    asserted_area = math.pi * (10 ** 2)
    assert c1.area == asserted_area


def test_construct_from_diameter():
    """ Tests instantiating a Circle from its diameter """
    c1 = Circle.from_diameter(50)

    assert c1.radius == 25
    assert c1.diameter == 50


def test_str_and_repr():
    """ Testing Circle's dunder str and repr methods """
    c1 = Circle(10)

    assert c1.__str__() == 'A circle with a radius of 10'
    assert c1.__repr__() == 'Circle(10)'


def test_add_multiply():
    """ Testing variations of Circle addition and multiplication """
    c1 = Circle(10)
    c2 = Circle(20)

    assert c1 + c2 == 30
    assert c1 + 10 == 20
    assert 10 + c1 == 20
    assert c1 * c2 == 200
    assert c1 * 10 == 100
    assert 10 * c1 == 100


def test_comparison():
    """ Tests Circle's comparison operators """
    c1 = Circle(10)
    c2 = Circle(20)

    assert c1 < c2
    assert not (c1 > c2)
    assert c1 < 30
    assert c1 == 10
    assert c1 > 5
    assert c1 <= c2
    assert c1 <= 15
    assert c1 >= 3


def test_comparison_complex():
    """ Tests Circle comparison in a more complex way """
    c1 = Circle(10)

    assert c1 * 3 == 3 * c1


def test_sphere():
    """ Tests instantiating a sphere and checks its properties for accuracy """
    s1 = Sphere(10)

    assert s1.radius == 10
    assert s1.volume == 4188.79
    assert s1.area == 1256.64


def test_sphere_from_diameter():
    """ Tests creating a sphere from its diameter. """
    s1 = Sphere.from_diameter(30)
    assert s1.radius == 15
    assert s1.diameter == 30
