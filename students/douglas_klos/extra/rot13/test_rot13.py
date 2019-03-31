#!/usr/bin/env python3

""" Test cases for rot13.py """

# Douglas Klos
# March 6th, 2019
# Python 210, Extra
# test_rot13.py

import rot13


def test_rot13():
    """ Basic test cases for rot13 """
    assert rot13.rot13('abcdefghijklm') == 'nopqrstuvwxyz'
    assert rot13.rot13('nopqrstuvwxyz') == 'abcdefghijklm'
    assert rot13.rot13('abcdefghijklm'.upper()) == 'nopqrstuvwxyz'.upper()
    assert rot13.rot13('nopqrstuvwxyz'.upper()) == 'abcdefghijklm'.upper()

    assert rot13.rot13(rot13.rot13('This is a test')) == 'This is a test'
