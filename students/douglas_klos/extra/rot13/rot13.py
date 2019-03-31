#!/usr/bin/env python3

""" Function to convert rot13 'encrypt' """

# Douglas Klos
# March 6th, 2019
# Python 210, Extra
# rot13.py

# a - z == 97 - 122
# A - Z == 65 - 90
# We'll ignore other characters such as punctuation


def rot13(value):
    """ Function to perform rot13 on input """

    output = ''
    for letter in value:
        if ord(letter) >= 97 and ord(letter) <= 122:
            output += chr(ord(letter) - 13) if ord(letter) >= 110 else chr(ord(letter) + 13)
        elif ord(letter) >= 65 and ord(letter) <= 90:
            output += chr(ord(letter) - 13) if ord(letter) >= 78 else chr(ord(letter) + 13)
        else:
            output += letter
    print(output)
    return output
