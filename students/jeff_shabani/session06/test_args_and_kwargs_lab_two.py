#!/usr/bin/env python3

import unittest

from students.jeff_shabani.session06.args_and_kwargs_lab import colors_two


class MyTests(unittest.TestCase):

    def test_args(self):
        test_vals = ('red', 'blue', 'yellow', 'chartreuse')
        expected = (test_vals[0], test_vals[1], test_vals[2], test_vals[3])
        actual = colors_two(*test_vals)
        self.assertEqual(expected, actual)

    def test_kwargs(self):
        test_vals = {'link_color': 'red', 'back_color': 'blue'}
        expected = {'link_color': 'red', 'back_color': 'blue'}
        actual = colors_two(**test_vals)
        self.assertEqual(expected, actual)

    def test_args_and_kwargs(self):
        kwargs = {'link_color': 'red', 'back_color': 'blue'}
        pos_args = 'purple'
        expected = (('purple',), {'link_color': 'red', 'back_color': 'blue'})
        actual = colors_two(pos_args, **kwargs)
        self.assertEqual(expected, actual)

    def test_tuples_and_dicts(self):
        regular = ('red', 'blue')
        links = {'link_color': 'chartreuse'}
        expected = (('red', 'blue'), {'link_color': 'chartreuse'})
        actual = colors_two(*regular, **links)
        self.assertEqual(expected, actual)

    def test_tuples_and_dicts_two(self):
        regular = 'red'
        links = {'back_color': 'Weiß', 'link_color': 'purple-ish'}
        expected = (('red',), {'back_color': 'Weiß', 'link_color': 'purple-ish'})
        actual = colors_two(regular, **links)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
