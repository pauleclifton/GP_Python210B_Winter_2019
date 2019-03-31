import pytest
import math
from Circle import Circle, Sphere


def test_radius():
    """Test that the radius is the radius"""
    c = Circle(4)
    assert c.radius == 4

    
def test_diameter():
    """ test that diameter is calculated correctly"""
    c = Circle(4) 
    assert c.diameter == 8


def test_set_diameter():
    c = Circle(4)
    c.diameter = 10
    assert c.diameter == 10
    assert c.radius == 5

    
def test_area():
    """test that area gets calculated properly"""
    c = Circle(2) 
    assert c.area == math.pi * (2 ** 2)

    
def test_constructor():
    """Test that the alternate constructor of from_diameter() works"""   
    c = Circle.from_diameter(4)
    assert c.diameter == 4
    assert c.radius == 2

    
def test_str():
    """Test that a Circle class object prints the string"""
    c = Circle(4)
    result = str(c)
    assert result == "Circle with radius: 4.0000"

    
def test_repr():
    c = Circle(4)
    d = repr(c)
    assert d == 'Circle(4)'

    
def test_add():
    """
    Testing that adding two Circle classes together yields a
    Circle class with sums of their radius
    """
    c1 = Circle(2)
    c2 = Circle(4)
    print(c1 + c2)
    assert(c1+c2) == 6

    
def test_mul():
    c1 = Circle(4)
    assert (c1 * 3) == 12

    
def test_rmul():
    c1 = Circle(4)
    assert 3 * c1 == 12

    
def test_less():
    """ Test that the Circles can be compared with less than statement"""
    c1 = Circle(3)
    c2 = Circle(5)
    assert c1.radius < c2.radius

    
def test_greater():
    """ Test that the Circles can be compared with greater than statement"""
    c1 = Circle(5)
    c2 = Circle(3)
    assert c1.radius > c2.radius

    
def test_equal():
    """Test that the Circles  can be compared with equal statement"""
    c1 = Circle(6)
    c2 = Circle(6)
    assert c1.radius == c2.radius

    
def test_sort_val():
    """test list of circles is sorted"""
    circle1= 10 
    circle2 = 5 
    circle3 = 2
    circle4 = 7
    circles_list = [circle1, circle2, circle3, circle4]
    circles_list.sort()
    assert circles_list == [circle3, circle2, circle4, circle1]

    
# Test the Sphere class
def test_sphere_str(): 
    """ Tests that __str__ is working """
    s = Sphere(4)
    sphere1 = str(s)
    assert sphere1 == "Sphere with radius: 4.00"

    
def test_sphere_repr():
    """ Tests that __repr__ is working """
    s = Sphere(4)
    sphere1 = repr(s)
    assert sphere1 == 'Sphere(4)'

    
def test_sphere_area(): 
    """ Tests that the area of the sphere is calculated correctly """ 
    sphere1 = Sphere(10) 
    assert sphere1.area == 4 * math.pi * 10 ** 2

    
def test_sphere_volume(): 
    """ Tests that the volume of the sphere is calculated correctly """ 
    sphere1 = Sphere(10) 
    assert sphere1.volume == (4/3) * math.pi * 10 ** 3


