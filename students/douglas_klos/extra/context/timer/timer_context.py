#!/usr/bin/env python3

# Douglas Klos
# March 7th, 2019
# Python 210, Extra
# timer_context.py

""" A simple class based context manager to calculate execution time """

import time


class Timer():
    """ A simple class based context manager to calculate execution time """
    def __init__(self, file_name, name=''):
        self.file_obj = file_name
        self.name = name
        self.start = time.time

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exeception_type, exeception_value, traceback):
        self.file_obj.write(f'{self.name} execution took {time.time() - self.start} seconds')
        return self.file_obj
