#!/usr/bin/env python3
""" Test assertions for args_kwargs_lab using unittest """

# Douglas Klos
# February 19th, 2019
# Python 210, Session 6
# test_args_kwargs_lab.py

import unittest
from args_kwargs_lab import colors1, colors2


class ArgsKwargsTest(unittest.TestCase):
    """ Class to test args_kwargs_lab """

    color_tuple = ('light blue', 'grey')
    color_dict = {'link_color': 'blue', 'visited_color': 'black'}

    def test_colors1(self):
        """ Test assertions for colors1 function """

        assert(colors1()
               == ('white', 'white', 'white', 'white'))
        assert(colors1('red', 'blue', 'yellow', 'chartreuse')
               == ('red', 'blue', 'yellow', 'chartreuse'))
        assert(colors1(link_color='red', back_color='blue')
               == ('white', 'blue', 'red', 'white'))
        assert(colors1('purple', link_color='red', back_color='blue')
               == ('purple', 'blue', 'red', 'white'))
        assert(colors1(*self.color_tuple)
               == ('light blue', 'grey', 'white', 'white'))
        assert(colors1(*self.color_tuple, **self.color_dict)
               == ('light blue', 'grey', 'blue', 'black'))

    def test_colors2(self):
        """ Test assertions for colors2 function """

        assert(colors2() == ((), {}))
        assert(colors2(*self.color_tuple, **self.color_dict)
               == (self.color_tuple, self.color_dict))
        assert(colors2('red', *self.color_tuple, **self.color_dict)
               == (('red', 'light blue', 'grey'),
                   {'link_color': 'blue', 'visited_color': 'black'}))
        assert(colors2('red', *self.color_tuple, 'blue', **self.color_dict)
               == (('red', 'light blue', 'grey', 'blue'),
                   {'link_color': 'blue', 'visited_color': 'black'}))
