#!/usr/bin/env python3
import mock
import unittest

from pathlib import Path
from students.jeff_shabani.session06 import mailroom_4

ANSWER = 'New_Donor'
AMOUNT = 4512


class mailroomTests(unittest.TestCase):

    def test_add_donor_to_donors(self):
        """
        tests that new donor is added to donors
        """
        self.assertEqual(mailroom_4.add_donor(ANSWER, AMOUNT), 6)

    def test_write_single_letter(self):
        """
        test that a single letter is written, saved as a text
        file and named correctly.
        """
        self.assertEqual(mailroom_4.write_a_single_letter(ANSWER, AMOUNT), True)

    def test_view_donor_names(self):
        """
        test that function returns all donor names
        """
        self.assertEqual(mailroom_4.view_donor_names(),
                         print('\nWilliam B\nSammy Maudlin\nSkip Bittman\nAshley Lashbrooke'))

    def test_letter_text(self):
        """
        tests that text in letter is correct
        """
        letter_text = str()
        with open(f'{Path.cwd()}/{ANSWER}.txt') as infile:
            for line in infile:
                letter_text += line
        self.assertEqual(mailroom_4.write_a_letter(ANSWER, AMOUNT), letter_text)

    def test_new_donor_dictionary(self):
        """
        tests values of a single dictionary key of the new donor
        dictionary
        """
        self.maxDiff = None
        result = mailroom_4.create_new_donors_dict()
        self.assertEqual(result['Ashley Lashbrooke'], (25000, 2, 1.0))

    @unittest.expectedFailure
    def test_membership_in_dictionary(self):
        """
        test for key not in new donor dictionary
        """

        self.assertIn('Bobby', mailroom_4.create_new_donors_dict())

    @mock.patch('mailroom_4.get_value', mock.Mock(return_value='54'))
    def test_correct_input(self):
        self.assertEqual(mailroom_4.get_value('Enter a value:', int), 'Invalid')


if __name__ == '__main__':
    unittest.main()
