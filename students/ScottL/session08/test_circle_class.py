
import circle_class


def test_radius():
    cir1 = circle_class.Circle(5)
    cir2 = circle_class.Circle(3.5)
    assert isinstance(cir1.radius, int)
    assert isinstance(cir2.radius, float)


def test_diameter():
    cir1 = circle_class.Circle(5)
    cir1.diameter = 20
    assert cir1.radius == 20 / 2
    assert cir1.diameter == 20


def test_area():
    cir1 = circle_class.Circle(10)
    assert round(cir1.area, 1) == round(3.1415 * 10 ** 2, 1)


def test_alt_constructor():
    cir1 = circle_class.Circle.from_diameter(10)
    assert cir1.diameter == 10


def test_string():
    cir1 = circle_class.Circle(4)
    assert cir1.__str__() == "Circle with a radius of: 4"


def test_repr():
    cir1 = circle_class.Circle(5)
    assert cir1.__repr__() == "Circle(5)"


def test_add():
    cir1 = circle_class.Circle(3)
    cir2 = circle_class.Circle(4)
    assert cir1 + cir2 == circle_class.Circle(7)


def test_multiply():
    cir1 = circle_class.Circle(4)
    assert cir1 * 2 == circle_class.Circle(8)
    assert 2 * cir1 == circle_class.Circle(8)


def test_less():
    cir1 = circle_class.Circle(1)
    cir2 = circle_class.Circle(2)
    assert cir1 < cir2


def test_more():
    cir4 = circle_class.Circle(4)
    cir3 = circle_class.Circle(3)
    assert cir4 > cir3


def test_equal():
    cir1 = circle_class.Circle(1)
    cir2 = circle_class.Circle(1)
    assert cir1 == cir2


def test_sort():
    list_circ = [circle_class.Circle(i) for i in range(3, 0, -1)]
    assert str(sorted(list_circ)) == "[Circle(1), Circle(2), Circle(3)]"


def test_sphere():
    sph1 = circle_class.Sphere(3)
    sph2 = circle_class.Sphere(4)
    assert sph1.radius == 3
    assert round(sph1.volume, 1) == round(4 / 3 * 3.1415 * 3 ** 3, 1)
    assert round(sph1.area, 1) == round(4 * 3.1415 * 3 ** 2, 1)
    assert sph1.__str__() == "Sphere with a radius of: 3"
    assert sph1.__repr__() == "Sphere(3)"
    assert sph1 + sph2 == circle_class.Sphere(7)
    assert sph1 * 2 == circle_class.Sphere(6)
    assert 4 * sph1 == circle_class.Sphere(12)
    assert sph1 < sph2
    assert sph2 > sph1
