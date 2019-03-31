'''
Tests for Circle program
You'll note that this is chock full of pylint disables.  This is because I use
Atom's pylinter plugin, and while it's fantastic at helping me with problems
while I'm going, unit testing is going to have linting problems, so I disable
them as they come up, that way I know when I'm doing something bad.
'''
from math import pi
import pytest
from circle import Circle, Sphere


def test_empty_circle():
    '''
    Test 1:  No values insertered.
    '''
    #pylint: disable=E1120
    with pytest.raises(TypeError):
        Circle()


def test_new_circle():
    '''
    Test 2:  Testing a value for the circle.
    '''
    Circle(1)


def test_radius():
    '''
    Test 3:  Testing inserting a radius.
    '''
    #pylint: disable=C0103
    c = Circle(2)

    assert c.radius == 2


def test_diameter():
    '''
    Test 4:  Testing diameter calculation.
    '''
    #pylint: disable=C0103
    c = Circle(3)

    assert c.diameter == 6


def test_set_diameter():
    '''
    Test 5: Testing manually setting a diameter.
    '''
    #pylint: disable=C0103
    c = Circle(4)
    c.diameter = 5

    assert c.diameter == 5
    assert c.radius == 2.5


def test_area():
    '''
    Test 6:  Testing area calculation.
    '''
    #pylint: disable=C0103
    c = Circle(6)

    assert c.area == pi * 36


def test_set_area():
    '''
    Test 7:  Testing AttributeError
    '''
    #pylint: disable=C0103
    c = Circle(7)

    with pytest.raises(AttributeError):
        c.area = 10


def test_from_diameter():
    '''
    Test 8:  Testing calculating circle from diameter insertion
    '''
    #pylint: disable=C0103
    c = Circle.from_diameter(8)

    assert c.diameter == 8
    assert c.radius == 4


def test_string():
    '''
    Test 9:  String insertion and formatted print
    '''
    #pylint: disable=C0103
    c = Circle(9)
    assert str(c) == "Circle with radius: 9"

def test_string_representation():
    '''
    Test 10:  Testing string representation, turns out it's a lot like string
    '''
    #pylint: disable=C0103
    c = Circle(12)
    assert repr(c) == "Circle(12)"

def test_add_circles():
    '''
    Test 11:  Testing adding circles
    '''
    #pylint: disable=C0103
    c1 = Circle(6)
    c2 = Circle(4)

    assert c1 + c2 == 10

def test_multiply_circles():
    '''
    Test 12:  Testing multiplication
    '''
    #pylint: disable=C0103
    c1 = Circle(4)
    c2 = Circle(2)

    assert c1 * c2 == 8

def test_rmul_circles():
    '''
    Test 13: Testing the rmul function
    '''
    #pylint: disable=C0103
    c1 = Circle(2)

    assert 4 * c1 == 8

def test_greater_than():
    '''
    Test 14: Testing greater than
    '''
    #pylint: disable=C0103
    c1 = Circle(5)
    c2 = Circle(2)

    assert (c1 > c2) is False


def test_less_than():
    '''
    Test 15:  Less than
    '''
    #pylint: disable=C0103
    c1 = Circle(2)
    c2 = Circle(5)

    assert (c1 < c2) is True


def test_equal_to():
    '''
    Test 16:  Testing equal to function
    '''
    #pylint: disable=C0103
    c1 = Circle(3)
    c2 = Circle(3)

    assert (c1 == c2) is True


def test_sort():
    '''
    Test 17:  Testing the sorting function
    '''
    #pylint: disable=C0103
    circles = [Circle(4), Circle(1), Circle(3), Circle(2), Circle(5)]
    circles.sort()

    assert circles == [Circle(1), Circle(2), Circle(3), Circle(4), Circle(5)]


def test_reflected_numerics():
    '''
    Test 18: Testing relected numerics
    '''
    #pylint: disable=C0103
    c1 = Circle(3)

    assert c1 * 3 == 3 * c1


def test_dividing_reflected_numerics():
    '''
    Test 19: Testing dividing relected numerics
    '''
    #pylint: disable=C0103
    c1 = Circle(3)

    assert c1 / 3 == 3 / c1


def test_augmented_assignments():
    '''
    Test 20:  Let's test augmented assignment I guess
    '''
    #pylint: disable=C0103
    c1 = Circle(3)
    c2 = Circle(3)

    c1 += c2
    assert c1 == 6

    c1 *= 2
    assert c1 == 12

'''
Spheres!
'''

def test_new_sphere():
    '''
    Test 21:  Here goes this test
    '''
    Sphere(4)

def test_empty_sphere():
    '''
    Test 22:  No values insertered.
    '''
    #pylint: disable=E1120
    with pytest.raises(TypeError):
        Sphere()


def test_str_sphere():
    '''
    Test 23:  Testing string insertion.
    '''
    #pylint: disable=E1120, C0103
    s = Sphere(13)
    assert str(s) == "Sphere with radius: 13"


def test_repr_sphere():
    '''
    Test 24:  Testing repr fuctionality.
    '''
    #pylint: disable=E1120, C0103
    s = Sphere(12)
    assert repr(s) == "Sphere(12)"


def test_sphere_volume():
    '''
    Test 24:  Testing sphere volume fuctionality.
    '''
    #pylint: disable=E1120, C0103
    s = Sphere(4)
    assert s.volume == 4 / 3 * pi * 4 ** 3


def test_sphere_area():
    '''
    Test 24:  Testing sphere area fuctionality.
    '''
    #pylint: disable=E1120, C0103
    s = Sphere(6)
    assert s.area == 4 * pi * 6 ** 2


def test_sphere_set_diameter():
    '''
    Test 24:  Testing set diameter fuctionality.
    '''
    #pylint: disable=E1120, C0103
    s = Sphere.from_diameter(8)

    assert s.area == 4 * pi * 4 ** 2
    assert s.volume == 4 / 3 * pi * 4 ** 3
