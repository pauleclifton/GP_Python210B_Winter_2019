#!/usr/bin/env python3
import unittest
from pathlib import Path


from students.jeff_shabani.session06 import mailroom_4

ANSWER = 'New_Donor'
AMOUNT = 4512


def get_value(text, check_type):
    """
    Refactored function from mailroom_4 to mock
    user input testing
    """
    try:
        value = check_type(text)
        return value
    except ValueError:
        return 'Please enter a valid value'


def get_input(text):
    return input(text)


def amount_type():
    answer = get_input('Please enter an amount')
    if isinstance(answer, int):
        return 'Good'
    if not isinstance(answer, int):
        return "Wrong type."


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

    def test_get_value_pass(self):
        """
        test that get_value function returns input value
        if input value is the correct type
        :return: int
        """
        self.assertEqual(get_value(45, int), 45)

    @unittest.expectedFailure
    def test_get_value_fail(self):
        """
        test that get_value function returns a message to
        user if input value is incorrect type
        :return:
        """
        self.assertEqual(get_value('amoimt', int), 54)


if __name__ == '__main__':
    unittest.main()
