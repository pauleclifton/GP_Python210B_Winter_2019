#!/usr/bin/env python3
#pylint: disable=R0912

""" Class to convert between Roman and Arabic numerals """

# Douglas Klos
# March 6th, 2019
# Python 210, Extra
# numerals.py


class Numerals():
    """
    Class to convert between Roman and Arabic numerals

    Subtractive roman numerals with a standard upper limit of 4999
    """

    ROMAN_NUMERAL_LIST = {'M': 1000,
                          'D': 500,
                          'C': 100,
                          'L': 50,
                          'X': 10,
                          'V': 5,
                          'I': 1}

    def __init__(self, value=0):
        if isinstance(value, int):
            if value > 4999:
                raise ValueError
            self._arabic = value

        if isinstance(value, str):
            self._arabic = self.convert_to_arabic(value)

    def __str__(self):
        return str(self.arabic)

    def convert_to_arabic(self, value):
        """ Given an input Roman Numeral, conert to arabic and set self._arabic """
        return_arabic = 0

        for i in range(len(value)-1):
            if self.ROMAN_NUMERAL_LIST[value[i]] < self.ROMAN_NUMERAL_LIST[value[i + 1]]:
                return_arabic -= self.ROMAN_NUMERAL_LIST[value[i]]
            else:
                return_arabic += self.ROMAN_NUMERAL_LIST[value[i]]
                
        self.arabic = return_arabic + self.ROMAN_NUMERAL_LIST[value[-1]]
        if self.arabic < 5000:
            return self.arabic
        raise ValueError

    @property
    def arabic(self):
        """ Returns the roman numerals """
        return self._arabic

    @arabic.setter
    def arabic(self, value):
        self._arabic = value

    @property
    def roman(self):
        """ Returns the roman numeral for self._arabic """
        number = self._arabic
        roman_numeral = ''

        roman_conversions = [
            ('M', 1000),
            ('CM', 900),
            ('D', 500),
            ('CD', 400),
            ('C', 100),
            ('XC', 90),
            ('L', 50),
            ('XL', 40),
            ('X', 10),
            ('IX', 9),
            ('V', 5),
            ('IV', 4),
            ('I', 1)
        ]

        for value in roman_conversions:
            while number >= value[1]:
                roman_numeral += value[0]
                number -= value[1]
