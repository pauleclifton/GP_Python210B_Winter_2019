#!/usr/bin/env python3

from circle import *

# This file was briefly used for testing.
# It's not part of the assignment requirements and can be safely ignored.

def main():
    c1 = Circle(5)
    c2 = Circle(10)
    c3 = c1 * c2

    print("---------------str--------------------")

    print(c1)
    print(c2)

    print(str(c1))
    print(str(c2))

    print("---------------repr-------------------")

    print(repr(c1))
    print(repr(c2))

    print("---------------sort-------------------")

    c_list = [c2, c3, c1]
    circle_list = [Circle(5), Circle(10), Circle(2)]

    print(c_list)
    c_list.sort()
    print(c_list)

    print(circle_list)
    circle_list.sort()
    print(circle_list)

    print("---------------add--------------------")

    print(3 + c1)
    print(c1 + 3)
    print(c1 + c2)

    print("---------------sub--------------------")

    print(c1 - 2)
    print(10 - c1)
    print(c2 - c1)

    print("---------------mul--------------------")

    print(5 * c1)
    print(c1 * c2)
    print(c1 * 5.0)
    print(10.2 * c1)

    



if __name__ == '__main__':
    main()
    