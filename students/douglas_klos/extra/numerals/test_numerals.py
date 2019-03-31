#!/usr/bin/env python3
#pylint: disable=C0103,W0612

""" Test cases for numerals.py """

# Douglas Klos
# March 6th, 2019
# Python 210, Extra
# test_numerals.py


import pytest
from numerals import Numerals


def test_numerals_arabic_init():
    """ Tests that Numerals class can be initialized with arabic numbers """
    n0 = Numerals(4999)
    n1 = Numerals(1999)
    n2 = Numerals(1949)
    n3 = Numerals(444)
    n4 = Numerals(14)
    n5 = Numerals(79)
    n6 = Numerals(225)
    n7 = Numerals(845)
    n8 = Numerals(2022)

    with pytest.raises(ValueError):
        n9 = Numerals(5000)


def test_numerals_roman_init():
    """ Tests that Numerals class can be initialized with roman numerals """
    n0 = Numerals('MMMMCMXCIX')  # 4999
    n1 = Numerals('MCMXCIX')     # 1999
    n2 = Numerals('MCMXLIX')     # 1949
    n3 = Numerals('CDXLIV')      # 444
    n4 = Numerals('XIV')         # 14
    n5 = Numerals('LXXIX')       # 79
    n6 = Numerals('CCXXV')       # 225
    n7 = Numerals('DCCCXLV')     # 845
    n8 = Numerals('MMXXII')      # 2022

    with pytest.raises(ValueError):
        n9 = Numerals('MMMMM')

    assert n0.arabic == 4999
    assert n1.arabic == 1999
    assert n2.arabic == 1949
    assert n3.arabic == 444
    assert n4.arabic == 14
    assert n5.arabic == 79
    assert n6.arabic == 225
    assert n7.arabic == 845
    assert n8.arabic == 2022


def test_convert_to_roman():
    """ Tests that converting arabic to roman numerals functions correctly """
    n0 = Numerals(4999)
    n1 = Numerals(1999)
    n2 = Numerals(1949)
    n3 = Numerals(444)
    n4 = Numerals(14)
    n5 = Numerals(79)
    n6 = Numerals(225)
    n7 = Numerals(845)
    n8 = Numerals(2022)

    assert n0.roman == 'MMMMCMXCIX'
    assert n1.roman == 'MCMXCIX'
    assert n2.roman == 'MCMXLIX'
    assert n3.roman == 'CDXLIV'
    assert n4.roman == 'XIV'
    assert n5.roman == 'LXXIX'
    assert n6.roman == 'CCXXV'
    assert n7.roman == 'DCCCXLV'
    assert n8.roman == 'MMXXII'
