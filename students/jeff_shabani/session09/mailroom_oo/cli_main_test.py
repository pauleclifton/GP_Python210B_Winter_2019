#!/usr/bin/env python3
import os
import unittest

from students.jeff_shabani.session09.mailroom_oo.cli_main import *

donors_test = {'William B': [120, 130, 50],
          'Sammy Maudlin': [500, 125, 670, 1000],
          'Bobby Bittman': [10],
          'Skip Bittman': [75, 125, 19],
          'Ashley Lashbrooke': [10000, 15000]}

print(os.getcwd())



class OOMailroonTests(unittest.TestCase):
    pass

    def test_get_value(self):
        #requires tester input
        clm = CommandLineInterface(donors_test)
        expected = 10
        self.assertEqual(clm.get_value('Enter 10', int), expected)
        del clm

    def test_set_letter_dir_path(self):
        #requires tester input
        clm = CommandLineInterface(donors_test)
        expected = os.getcwd()
        self.assertEqual(clm.set_letter_directory_path_path(), expected)
        del clm

    def test_set_letter_dir_path_2(self):
        #requires tester input
        clm = CommandLineInterface(donors_test)
        expected = r'C:\JRS\Python\UW\Intro_Klass\students\jeff_shabani\session08'
        self.assertEqual(clm.set_letter_directory_path_path(), expected)
        del clm



if __name__ == '__main__':
    unittest.main()
