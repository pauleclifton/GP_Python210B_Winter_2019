#!/usr/bin/env python3

class SparseArray(object):
    working_dict = dict()

    def __init__(self, sequence=None):
        if sequence is None:
            self.sequence = []
        self.sequence = sequence
        self.display_list = [i for i in self.sequence if i > 0]
        self.create_working_dict = {key: value for key, value in enumerate(self.sequence) if value > 0}

    # @classmethod
    def create_working_dict(cls):
        working_dict = {key: value for key, value in enumerate(self.sequence) if value > 0}
        return working_dict

    def __len__(self):
        return len(self.sequence)

    def append(self, val):
        if val == 0:
            return self.sequence
        self.sequence.append(val)
        # self.create_working_dict()
        self.working_dict = {key: value for key, value in enumerate(self.sequence) if value > 0}

    def __getslice__(self, start, end):
        return self.sequence[start:end]

    def __delitem__(self, key):
        if key in self.working_dict:
            del (self.working_dict[key])
        self.sequence.pop(key)

    def __getitem__(self, item):
        return self.sequence[item]

    def __setitem__(self, key, value):
        self.working_dict[key] = value

    def __contains__(self, item):
        if self.sequence:
            return True

    def __repr__(self):
        return f'{self.sequence} has a length of {len(self.sequence)}'
