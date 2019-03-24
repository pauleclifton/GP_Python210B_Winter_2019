
import pytest
from sparse_array import SparseArray


my_array = [1, 2, 0, 0, 0, 0, 3, 0, 0, 4]

def test_sparsearray_len():
    """ Tests that length is returned properly """
    sa = SparseArray(my_array)
    print(sa)
    assert len(sa) == len(my_array)



def test_sparsearray_str():
    """ Tests that __str__is correctly implemented """
    sa = SparseArray(my_array)
    result = str(sa) 
    assert result == "Sparse Array({0: 1, 1: 2, 6: 3, 9: 4})"



def test_sparsearray_del():
    """ Tests that you can delete an element from the sparse array """
    sa = SparseArray(my_array)
    del sa[4]
    print(sa)

    assert sa[4] == 0
    assert len(sa) == 8


def test_sparsearray_append():
    """ Tests that you can append to the sparse array """
    sa = SparseArray(my_array)
    sa.append(4)
    assert len(sa) == 11



def test_sparsearray_set():
    """test that value set properly"""
    sa = SparseArray(my_array)
    sa[5]= 12
    sa[3] = 0 #the zero won't store
    assert sa[5] == 12 
