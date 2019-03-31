#!/usr/bin/env python3
#pylint: disable=C0113

""" Pytest file for circle.py """

# Douglas Klos
# March 4th, 2019
# Python 210, Session 8
# test_circle.py


import math
import pytest
from circle import Circle, Sphere


def test_set_radius_init():
    """ Tests that you can set the radius of a circle during init """
    circle1 = Circle()
    circle2 = Circle(5)

    assert circle1.radius == 0
    assert circle1.diameter == 0
    assert circle2.radius == 5
    assert circle2.diameter == 10


def test_set_diameter():
    """ Tests that you can set the diameter of circle and that radius updates """
    circle1 = Circle()
    circle1.diameter = 10

    assert circle1.radius == 5
    assert circle1.diameter == 10


def test_area():
    """ Tests that the area of a circle is computed properly """
    circle1 = Circle(10)

    assert circle1.radius == 10
    assert circle1.diameter == 20
    assert circle1.area == 2 * math.pi * circle1.radius ** 2


def test_set_area():
    """ Tests that setting the area fails and returns an AttributeError """
    circle1 = Circle(10)

    with pytest.raises(AttributeError):
        circle1.area = 100


def test_from_diameter():
    """ Tests that a circle can be created from a diameter """
    circle1 = Circle.from_diameter(10)

    assert circle1.radius == 5
    assert circle1.diameter == 10
    assert circle1.area == 2 * math.pi * circle1.radius ** 2


def test_str():
    """ Tests that __str__ is working """
    circle1 = Circle(10)

    assert str(circle1) == 'Circle with radius: 10'


def test_repr():
    """ Tests that __repr__ is working """
    circle1 = Circle(10)

    assert repr(circle1) == 'Circle(10)'


def test_addition():
    """ Tests that __add___ is working """
    circle1 = Circle(10)
    circle2 = Circle(20)
    circle3 = circle1 + circle2

    assert circle3.radius == 30
    assert circle1 + 5 == Circle(15)


def test_radd():
    """ Tests that reflected addition works """
    circle1 = Circle(2)
    circle2 = Circle(4)

    assert circle1 + 2 == 2 + circle1
    assert 2 + circle1 == circle2
    assert 5 + circle1 == Circle(7)


def test_iadd():
    """ Tests that += works """
    circle1 = Circle(2)
    circle2 = Circle(4)
    circle1 += circle2
    circle2 += 2

    assert circle1 == Circle(6)
    assert circle2 == Circle(6)


def test_subtraction():
    """ Tests that __sub___ is working """
    circle1 = Circle(10)
    circle2 = Circle(6)
    circle3 = circle1 - circle2

    assert circle3.radius == 4
    assert circle1 - 5 == Circle(5)
    assert circle2 - 2 == Circle(4)


def test_rsub():
    """ Tests that reflected subtractions works """
    circle1 = Circle(10)
    circle2 = Circle(6)

    assert 10 - circle1 == circle1 - 10
    assert 10 - circle2 == Circle(4)
    assert 10.0 - circle2 == Circle(4)


def test_isub():
    """ Tests that -= works """
    circle1 = Circle(2)
    circle2 = Circle(4)
    circle2 -= circle1
    circle1 -= 1

    assert circle1 == Circle(1)
    assert circle2 == Circle(2)


def test_multiplication():
    """ Tests that __mul__ is working """
    circle1 = Circle(2)
    circle2 = Circle(4)
    circle3 = circle1 * circle2

    assert circle3.radius == 8
    assert circle1 * 2 == Circle(4)
    assert circle2 * 2 == Circle(8)


def test_rmul():
    """ Tests that reflected multiplication works """
    circle1 = Circle(2)
    circle2 = Circle(4)

    assert 2 * circle1 == circle1 * 2
    assert 2 * circle1 == Circle(4)
    assert 2 * circle2 == Circle(8)


def test_imul():
    """ Tests that *= works """
    circle1 = Circle(2)
    circle2 = Circle(4)
    circle2 *= circle1
    circle1 *= 5

    assert circle1 == Circle(10)
    assert circle2 == Circle(8)


def test_truediv():
    """ Tests that division works """
    circle1 = Circle(10)
    circle2 = Circle(5)
    circle3 = circle1 / circle2
    circle4 = circle2 / circle1
    circle5 = circle1 / 5
    circle6 = circle2 / 10

    assert circle1 / circle2 == Circle(2)
    assert circle2 / circle1 == Circle(.5)
    assert circle3.radius == 2
    assert circle4.radius == .5
    assert circle5.radius == 2
    assert circle6.radius == .5


def test_rtruediv():
    """ Tests that reflected division works """
    circle1 = Circle(10)
    circle2 = Circle(5)
    circle3 = 5 / circle1
    circle4 = 10 / circle2

    assert 2 / circle1 == Circle(0.2)
    assert circle3 == Circle(.5)
    assert circle3.radius == 0.5
    assert circle4 == Circle(2)
    assert circle4.radius == 2


def test_itruediv():
    """ Tests that /= works """
    circle1 = Circle(2)
    circle2 = Circle(4)
    circle2 /= circle1
    circle1 /= 10

    assert circle1 == Circle(.2)
    assert circle2 == Circle(2)


def test_floordiv():
    """ Tests that classical floor division works """
    circle1 = Circle(10)
    circle2 = Circle(5)
    circle3 = circle1 // circle2
    circle4 = circle2 // circle1
    circle5 = circle1 // 5
    circle6 = circle2 // 10

    assert circle3 == Circle(2)
    assert circle4 == Circle(0)
    assert circle3.radius == 2
    assert circle4.radius == 0
    assert circle5.radius == 2
    assert circle6.radius == 0


def test_rfloordiv():
    """ Tests that reflected classical floor division works """
    circle1 = Circle(10)
    circle2 = Circle(5)
    circle3 = 5 // circle1
    circle4 = 10 // circle2

    assert 2 // circle1 == Circle(0)
    assert circle3.radius == 0
    assert circle3 == Circle(0)
    assert circle4.radius == 2
    assert circle4 == Circle(2)


def test_ifloordiv():
    """ Tests that //= works """
    circle1 = Circle(2)
    circle2 = Circle(4)
    circle2 //= circle1
    circle1 //= 10

    assert circle1 == Circle(0)
    assert circle2 == Circle(2)


def test_comparisons1():
    """ Tests comparison operations when circle1 is less than circle 2 """
    circle1 = Circle(2)
    circle2 = Circle(4)

    assert not circle1 > circle2
    assert not circle1 >= circle2
    assert circle1 < circle2
    assert circle1 <= circle2
    assert not circle1 == circle2
    assert circle1 != circle2


def test_comparisons2():
    """ Tests comparison operations when circle1 is greater than circle 2 """
    circle1 = Circle(4)
    circle2 = Circle(2)

    assert circle1 > circle2
    assert circle1 >= circle2
    assert not circle1 < circle2
    assert not circle1 <= circle2
    assert not circle1 == circle2
    assert circle1 != circle2


def test_comparisons3():
    """ Tests comparison operations when circle1 is equal to circle 2 """
    circle1 = Circle(2)
    circle2 = Circle(2)

    assert not circle1 > circle2
    assert circle1 >= circle2
    assert not circle1 < circle2
    assert circle1 <= circle2
    assert circle1 == circle2
    assert not circle1 != circle2


def test_sort():
    """ Tests that .sort() functions properly """
    circle1 = Circle(10)
    circle2 = Circle(5)
    circle3 = Circle(2)
    circle_list = [circle1, circle2, circle3]
    circle_list.sort()

    assert circle_list == [circle3, circle2, circle1]


def test_deleter():
    """ Tests that the deleter works for radius """
    circle1 = Circle(10)
    del circle1.radius

    with pytest.raises(AttributeError):
        print(circle1.radius)


def test_sphere_init():
    """ Tests that a Sphere object can be created """
    sphere1 = Sphere()
    sphere2 = Sphere(10)

    assert sphere1.radius == 0
    assert sphere1.diameter == 0
    assert sphere2.radius == 10
    assert sphere2.diameter == 20


def test_sphere_area():
    """ Tests that the area of the sphere is calculated correctly """
    sphere1 = Sphere(10)

    assert sphere1.area == 4 * math.pi * 10 ** 2


def test_sphere_volume():
    """ Tests that the volume of the sphere is calculated correctly """
    sphere1 = Sphere(10)

    assert sphere1.volume == (4/3) * math.pi * 10 ** 3


def test_sphere_str():
    """ Tests that __str__ is working """
    sphere1 = Sphere(10)

    print(str(sphere1))
    assert str(sphere1) == 'Sphere with radius: 10'


def test_sphere_repr():
    """ Tests that __repr__ is working """
    sphere1 = Sphere(10)

    print(repr(sphere1))
    assert repr(sphere1) == 'Sphere(10)'


def test_sphere_from_diameter():
    """ Tests you can create a sphere from diameter """
    sphere1 = Sphere.from_diameter(10)

    assert sphere1.radius == 5


def test_sphere_math():
    """ Tests that operators work on spheres """
    sphere1 = Sphere(10)
    sphere2 = Sphere(20)

    assert sphere1 + sphere2 == Sphere(30)
    assert sphere2 - sphere1 == Sphere(10)
    assert sphere1 * sphere2 == Sphere(200)
    assert sphere1 / sphere2 == Sphere(0.5)
    assert sphere1 // sphere2 == Sphere(0)

    assert 10 + sphere1 == Sphere(20)
    assert 20 - sphere1 == Sphere(10)
    assert 10 * sphere2 == Sphere(200)
    assert 10 / sphere2 == Sphere(.5)
    assert 10 // sphere2 == Sphere(0)


def test_sphere_comparisons():
    """ Tests that comparisons work on spheres """
    sphere1 = Sphere(10)
    sphere2 = Sphere(20)
    sphere3 = Sphere(20)

    assert sphere1 < sphere2
    assert sphere1 <= sphere2
    assert sphere2 > sphere1
    assert sphere2 >= sphere1
    assert sphere2 == sphere3
    assert sphere1 != sphere2
