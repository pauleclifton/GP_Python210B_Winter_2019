'''
##########################
#Python 210
#Session 08 - Circle Exercise
#Elaine Xu
#Mar 5, 2019
###########################
'''
from circle_exercise_ex import *
import pytest
#############################
#Step 1
#############################
def test_radius():
    c = Circle(4)
    assert c.radius == 4

#############################
#Step 2
#############################
def test_diameter():
    c = Circle(4)
    assert c.diameter == 8

#############################
#Step 3
#############################
def test_diameter2():
    c = Circle(4)
    c.diameter = 2
    assert c.diameter == 2
    assert c.radius == 1

#############################
#Step 4
#############################
def test_area():
    c = Circle(2)
    assert round(c.area, 6) == 12.566371

    with pytest.raises(AttributeError):
        c.area = 12

#############################
#Step 5
#############################
def test_alt_method():
    c = Circle.from_diameter(8)
    assert c.diameter == 8
    assert c.radius == 4

#############################
#Step 6
#############################
def test_print():
    c = Circle(4)
    assert c.__str__() == "Circle with radius: 4"
    assert c.__repr__() == "Circle(4)"

#############################
#Step 7
#############################
def test_numeric_protocol():
    c1 = Circle(2)
    c2 = Circle(4)
    assert c1 + c2 == 6
    assert c2 * 3 == 12
    assert 3 * c2 == 12

#############################
#Step 8
#############################
def test_compare():
    c1 = Circle(2)
    c2 = Circle(4)
    c3 = Circle(4)
    assert (c1 > c2) == False
    assert (c1 < c2) == True
    assert (c1 == c2) == False
    assert (c2 == c3) == True

    #test sorting
    circles = [Circle(6), Circle(7), Circle(8), Circle(4), Circle(0),
               Circle(2), Circle(3), Circle(5), Circle(9), Circle(1)]
    circles.sort()
    assert circles == [Circle(0), Circle(1), Circle(2), Circle(3), Circle(4),
                        Circle(5), Circle(6), Circle(7), Circle(8), Circle(9)]

    #test augmented assignment
    assert c1 * 3 == 3 * c1
    c1 += c2
    assert c1 == 6
    c2 *= 2
    assert c2 == 8

#############################
#Step 9
#############################
def test_sphere():
    s = Sphere(4)
    assert s.__str__() == "Sphere with radius: 4"
    assert s.__repr__() == "Sphere(4)"
    assert round(s.volume, 6) == 268.082573

    with pytest.raises(NotImplementedError):
        s.area()

    #test shpere with alternate constructor
    s2 = Sphere.from_diameter(8)
    assert s2.diameter == 8
    assert s2.radius == 4