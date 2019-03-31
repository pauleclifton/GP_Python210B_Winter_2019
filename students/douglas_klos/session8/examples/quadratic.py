#!/usr/bin/env python3

"""
A quaratic function evaluator

used to demonstrate callable classes
"""

class Quadratic:
    """
    Class to evaluate quadratic equations

    Each instance wil have a certain set of coefficients
    """

    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def __call__(self, x):
        return self.A * x**2 + self.B * x + self.C



def main():
    q1 = Quadratic(3,4,5)
    print(q1(1))
    print(q1(5))





if __name__ == '__main__':
    main()
