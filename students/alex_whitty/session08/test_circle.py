from math import pi
from circle import Circle, Sphere


def test_radius():
    c = Circle(2)
    assert c.radius == 2


def test_diameter():
    c = Circle(3)
    assert c.diameter == 6


def test_set_diameter():
    c = Circle(4)
    c.diameter = 5
    assert c.diameter == 5
    assert c.radius == 2.5


def test_area():
    c = Circle(6)
    assert c.area == pi * 36

def test_alt_construct():
    c1 = Circle.from_diameter(10)
    assert c1.diameter == 10


def test_from_diameter():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4


def test_string():
    c = Circle(9)
    assert str(c) == "Circle with radius: 9"

def test_string_repr():
    c = Circle(12)
    assert repr(c) == "Circle(12)"


def test_less():
    c1 = Circle(2)
    c2 = Circle(5)
    assert (c1 < c2) is True


def test_equal():
    c1 = Circle(3)
    c2 = Circle(3)
    assert (c1 == c2) is True


def test_sort():
    list_c = [Circle(i) for i in range(3, 0, -1)]
    assert str(sorted(list_c)) == "[Circle(1), Circle(2), Circle(3)]"


def test_sphere():
    Sphere(4)


def test_sphere_repr():
    s = Sphere(12)
    assert repr(s) == "Sphere(12)"


def test_sphere_volume():
    s = Sphere(4)
    assert s.volume == 4 / 3 * pi * 4 ** 3


def test_sphere_area():
    s = Sphere(6)
    assert s.area == 4 * pi * 6 ** 2


def test_sphere_diameter():
    s = Sphere.from_diameter(8)
    assert s.area == 4 * pi * 4 ** 2
    assert s.volume == 4 / 3 * pi * 4 ** 3
