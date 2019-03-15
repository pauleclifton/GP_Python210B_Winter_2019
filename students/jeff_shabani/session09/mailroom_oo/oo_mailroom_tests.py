#!/usr/bin/env python3

# Jeff Shabani
# March 2019
# Python 210, Session 9
# donor_models.py

import mock
import unittest

import students
from mailroom_oo import cli_main
from students.jeff_shabani.session09.mailroom_oo.cli_main import *

"""
Test for mailroom_oo. Note: these are not complete."""

ANSWER = 'New_Donor'
AMOUNT = 4512

donors_test = {'William B': [120, 130, 50],
               'Sammy Maudlin': [500, 125, 670, 1000],
               'Bobby Bittman': [10],
               'Skip Bittman': [75, 125, 19],
               'Ashley Lashbrooke': [10000, 15000]}


class OOMailroomTests(unittest.TestCase):

    def test_add_donor(self):
        d = DonorCollection(donors_test)
        d.add_donor(ANSWER, AMOUNT)
        self.assertIn(ANSWER, d.donors)
        self.assertIn(AMOUNT, d.donors[ANSWER])
        del d

    def test_write_a_letter(self):
        d = Donor(donors_test)
        """
        test that a single letter is written, saved as a text
        file and named correctly.
        """
        self.assertEqual(d.write_a_single_letter(ANSWER, AMOUNT), True)
        del d
        os.remove('New_Donor.txt')

    def test_view_donor_names(self):
        d = DonorCollection(donors_test)
        d.add_donor(ANSWER, AMOUNT)
        """
        test that function returns all donor names
        """
        self.assertEqual(d.view_donor_names(),
                         print('\nWilliam B\nSammy Maudlin\nSkip Bittman\nAshley Lashbrooke\nNew_Donor'))
        del d

    def test_view_donor_names2(self):
        d = DonorCollection(donors_test)
        d.add_donor(ANSWER, AMOUNT)
        dc = DonorCollection(donors_test)
        """
        test that function returns all donor names
        """
        self.assertEqual(dc.view_donor_names(),
                         print('\nWilliam B\nSammy Maudlin\nSkip Bittman\nAshley Lashbrooke\nNew_Donor'))
        del d

    @mock.patch('builtins.input', mock.Mock(return_value='54'))
    def test_get_value_2(self):
        self.assertEqual(CommandLineInterface.get_value(self, 'Enter a value:', int), 54)


    @mock.patch('students.jeff_shabani.session09.mailroom_oo.cli_main.input', mock.Mock(return_value='54'))
    def test_get_value_3(self):
        self.assertEqual(
            students.jeff_shabani.session09.mailroom_oo.cli_main.CommandLineInterface.get_value(self, 'Enter a value:',
                                                                                                int), 54)

    @mock.patch('builtins.input', mock.Mock(return_value='54'))
    @unittest.expectedFailure
    def test_get_wrong_input(self):
        self.assertEqual(CommandLineInterface.get_value(self, 'Enter a value:', str), 'Incorrect data type')

    # def test_set_letter_dir_path(self):
    #     # requires tester input
    #     clm = CommandLineInterface(donors_test)
    #     expected = os.getcwd()
    #     self.assertEqual(clm.set_letter_directory_path_path(), expected)
    #     del clm


if __name__ == '__main__':
    unittest.main()
