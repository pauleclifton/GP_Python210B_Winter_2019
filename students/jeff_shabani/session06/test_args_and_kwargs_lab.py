#!/usr/bin/env python3
import unittest

from students.jeff_shabani.session06.args_and_kwargs_lab import colors


class MyTests(unittest.TestCase):

    def test_args(self):
        test_vals = ('red', 'blue', 'yellow', 'chartreuse')
        expected = (test_vals[0], test_vals[1], test_vals[2], test_vals[3])
        actual = colors(*test_vals)
        self.assertEqual(expected, actual)

    def test_kwargs(self):
        test_vals = {'link_color': 'red', 'back_color': 'blue'}
        expected = ('white', 'blue', 'red', 'blue')
        actual = colors(**test_vals)
        self.assertEqual(expected, actual)

    def test_args_and_kwargs(self):
        kwargs = {'link_color': 'red', 'back_color': 'blue'}
        pos_args = 'purple'
        expected = ('purple', 'blue', 'red', 'blue')
        actual = colors(pos_args, **kwargs)
        self.assertEqual(expected, actual)

    def test_tuples_and_dicts(self):
        regular = ('red', 'blue')
        links = {'link_color': 'chartreuse'}
        expected = ('red', 'blue', 'chartreuse', 'blue')
        actual = colors(*regular, **links)
        self.assertEqual(expected, actual)

    def test_tuples_and_dicts_two(self):
        regular = ('red')
        links = {'back_color': 'Weiß', 'link_color': 'purple-ish'}
        expected = ('red', 'Weiß', 'purple-ish', 'blue')
        actual = colors(regular, **links)
        self.assertEqual(expected, actual)

    @unittest.expectedFailure
    def test_kwargs_and_args_error(self):
        """
        Checks for type error. Args declared as mapping (kwarg). Kwags delcared as arg
        """
        regular = {'back_color': 'Weiß', 'link_color': 'purple-ish'}
        links = ('red')
        expected = 'TypeError: colors() argument after ** must be a mapping, not str'
        actual = colors(regular, **links)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
