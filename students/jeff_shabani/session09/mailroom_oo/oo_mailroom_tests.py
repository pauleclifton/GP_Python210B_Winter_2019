#!/usr/bin/env python3
import os
import unittest

from students.jeff_shabani.session09.mailroom_oo.donor_models import *

ANSWER = 'New_Donor'
AMOUNT = 4512

donors_test = {'William B': [120, 130, 50],
               'Sammy Maudlin': [500, 125, 670, 1000],
               'Bobby Bittman': [10],
               'Skip Bittman': [75, 125, 19],
               'Ashley Lashbrooke': [10000, 15000]}


class DonorModelTests(unittest.TestCase):

    def test_add_donor(self):
        d = Donor(donors_test)
        d.add_donor(ANSWER, AMOUNT)
        expected = {f'{ANSWER}': [4512]}
        self.assertIn(ANSWER, d.donors)
        self.assertIn(AMOUNT, d.donors.values())
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
        d = Donor(donors_test)
        d.add_donor(ANSWER, AMOUNT)
        """
        test that function returns all donor names
        """
        self.assertEqual(d.view_donor_names(),
                         print('\nWilliam B\nSammy Maudlin\nSkip Bittman\nAshley Lashbrooke\nNew_Donor'))
        del d

    def test_view_donor_names2(self):
        d = Donor(donors_test)
        d.add_donor(ANSWER, AMOUNT)
        dc = DonorCollection(donors_test)
        """
        test that function returns all donor names
        """
        self.assertEqual(dc.view_donor_names(),
                         print('\nWilliam B\nSammy Maudlin\nSkip Bittman\nAshley Lashbrooke\nNew_Donor'))
        del d


if __name__ == '__main__':
    unittest.main()
