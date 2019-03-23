#!/usr/bin/env python3
#pylint: disable=C0103,W0104,W0107

# Douglas Klos
# March 7th, 2019
# Python 210, Extra
# test_raises_context.py

""" Run file for context manager testing """

import raises_context as rc


def test1():
    """ Tests AssertionError """
    with rc.Raises(AssertionError):
        raise AssertionError


def test2():
    """ Tests ZeroDivisionError """
    with rc.Raises(ZeroDivisionError):
        1 / 0


def test3():
    """ Tests that Raises fails properly """
    # We expcet the next line to fail, and it does
    # with rc.Raises(AssertionError):
    #     raise ZeroDivisionError
    pass


def main():
    """ Main, calls different tests """
    test1()
    test2()
    test3()


if __name__ == '__main__':
    main()
