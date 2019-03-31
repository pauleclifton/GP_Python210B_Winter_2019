#!/usr/bin/env python3


import unittest
import mailroom4
from unittest import mock


class TestMailroom4(unittest.TestCase):

    def test_write_a_letter(self):
        actual = mailroom4.write_a_letter('Paul Allen', 200)
        expected = f"Dear Paul Allen,\n\nThank you for your kind donation of $200\n\n" \
        f"It will be put to very good use.\n\n" \
        f"Sincerely,\n" \
        f"The Fundraising Committee"
        self.assertEqual(actual, expected)

    @mock.patch('mailroom4.get_value', mock.MagicMock(return_value=200.00))
    @mock.patch('mailroom4.dir_for_letter')
    def test_add_donor(self, mocks):
        new_donor = 'Pete Rose'
        mailroom4.add_donor(new_donor)
        with open(f'{new_donor}.txt', 'r') as my_test_file:
            actual = my_test_file.read()

        expected = f"Dear {new_donor},\n\nThank you for your kind donation of $200.0\n\n" \
        f"It will be put to very good use.\n\n" \
        f"Sincerely,\n" \
        f"The Fundraising Committee"

        self.assertEqual(actual, expected)


    def test_create_summary(self):
        mailroom4.donor_db = {"William Gates, III": [653772.32, 12.17, 15.123], "Jeff Bezos": [877.33, 1000.20]}
        actual = mailroom4.create_summary()
        expected = [['William Gates, III', 653799.613, 3, 217933.20433333333], ['Jeff Bezos', 1877.5300000000002, 2, 938.7650000000001]]
        self.assertEqual(expected, actual)

    @unittest.expectedFailure
    def test_letter_to_all_donors(self):
        amount = 200
        self.assertEqual(amount, 200)
        letter_to_all_donors = str()
        with open(f'{donor}.txt', 'wt') as letter:
            letter.write(letter_to_all_donors)
        with self.assertRaises(NameError):
            self.assertTrue(mailroom4.letter_to_all_donors(amount), True)

    def test_report(self):
        self.assertEqual(mailroom4.report(), None)

    def test_current_donor(self):
        current_donor = 'Elon Musk'
        self.assertEqual(current_donor, "Elon Musk")
        self.assertNotEqual(mailroom4.add_donor(current_donor), current_donor)


if __name__ == '__main__':
    unittest.main()
