#!/usr/bin/env python3

import unittest

from mailroom_oo.cli_main import *



class OOMailroonTests(unittest.TestCase):
    pass

    def test_get_value(self):
        #requires tester input
        clm = CommandLineInterface()
        expected = 10
        self.assertEqual(clm.get_value('Enter 10', int), expected)
        del clm

    def test_set_letter_dir_path(self):
        #requires tester input
        clm = CommandLineInterface()
        expected = os.getcwd()
        self.assertEqual(clm.set_letter_directory_path_path(), expected)
        del clm

