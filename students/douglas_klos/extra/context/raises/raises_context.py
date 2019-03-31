#!/usr/bin/env python3

# Douglas Klos
# March 7th, 2019
# Python 210, Extra
# raises_context.py

""" A simple class based context manager for exception handling """

# This seems entirely too simple... Yet it seems to work...
# Am I missing something?


class Raises():
    """ A simple class based context manager for exception handling """
    def __init__(self, value):
        self.value = value

    def __enter__(self):
        pass

    def __exit__(self, exception_type, exeception_value, traceback):
        if exception_type == self.value:
            return True
        return False
