#!/usr/bin/env python3
#pylint: disable=C0103
""" Pytest file for sparsearray.py """

# Douglas Klos
# March 5th, 2019
# Python 210, Session 8
# test_sparsearray.py


import pytest
from sparsearray import SparseArray

LIST1 = [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
LIST2 = [2, 0, 0]


def test_sparsearray_init():
    """ Tests that a sparsearray can be initialized """
    sa = SparseArray(LIST1)
    print(sa.array)
    assert sa.array[0] == sa.array[4] == sa.array[5] == sa.array[10] == sa.array[14] == 1


def test_sparsearray_len():
    """ Tests that length is returned properly """
    sa = SparseArray(LIST1)
    print(sa)
    assert len(sa) == len(LIST1)


def test_sparsearray_set_get_value():
    """ Tests that you can get and set values to the sparse array """
    sa = SparseArray(LIST1)
    sa[1] = 2
    sa[2] = 0

    with pytest.raises(IndexError):
        print(sa[20])
    with pytest.raises(IndexError):
        sa[20] = 10

    sa[0] = 0
    assert sa[0] == 0

    assert sa[1] == 2
    assert sa[2] == 0


def test_sparsearray_str():
    """ Tests that str(SparseArray) is correctly implemented """
    sa = SparseArray(LIST1)

    assert str(sa) == str(LIST1)


def test_sparsearray_repr():
    """ Tests that repr(SparseArray) is correctly implemented """
    sa = SparseArray(LIST1)

    print(repr(LIST1))
    assert repr(sa) == repr(LIST1)


def test_sparsearray_append():
    """ Tests that you can append to the sparse array """
    sa = SparseArray(LIST1)
    sa.append(LIST2)

    assert str(sa) == str(LIST1 + LIST2)
    assert len(sa) == 21


def test_sparsearray_del():
    """ Tests that you can delete an element from the sparse array """
    sa = SparseArray(LIST1)
    del sa[4]
    print(sa)

    assert sa[4] == 0
    assert len(sa) == 18


def test_sparsearray_slice():
    """ Tests that you can get slices from the sparse array """
    sa = SparseArray(LIST1)
    sa.append(LIST2)
    list3 = LIST1 + LIST2

    assert sa[0:4] == list3[0:4]
    assert sa[5:10] == list3[5:10]
    assert sa[10:21] == list3[10:21]
    assert sa[-1::2] == list3[-1::2]
