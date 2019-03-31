#!/usr/bin/env python3

""" SparseArray Class """

# Douglas Klos
# March 5th, 2019
# Python 210, Session 8
# sparsearray.py


class SparseArray():
    """ SparseArray class """

    def __init__(self, values):
        self.array = {}
        self.length = len(values)

        for key, value in enumerate(values):
            if value:
                self.array[key] = value

    def full_array(self):
        """ Returns the sparse array including 0's """
        return_array = []
        sorted_values = {key: value for key, value in sorted(self.array.items())}
        for counter in range(self.length):
            try:
                return_array.append(sorted_values[counter])
            except KeyError:
                return_array.append(0)
        return return_array

    def __str__(self):
        return str(self.full_array())

    def __repr__(self):
        return str(self.full_array())

    def __len__(self):
        return self.length

    def __getitem__(self, key):
        if isinstance(key, slice):
            return self.full_array()[key.start:key.stop:key.step]
        if key > self.length:
            raise IndexError
        try:
            return self.array[key]
        except KeyError:
            return 0

    def __setitem__(self, key, value):
        if key > self.length:
            raise IndexError
        if value:
            self.array[key] = value
        elif key in self.array:
            del self.array[key]

    def __delitem__(self, key):
        del self.array[key]

    def append(self, values):
        """ Appends new values to the end of the sparse array """
        for key, value in enumerate(values):
            if value:
                self.array[key + self.length] = value
        self.length += len(values)
