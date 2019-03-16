#!/usr/bin/env python3
import os
import unittest


from donor import *

ANSWER = 'New_Donor'
AMOUNT = 4512

class OOMailroonTests(unittest.TestCase):

    def test_add_donor(self):
        d = Donor()
        d.add_donor(ANSWER, AMOUNT)
        expected = {f'{ANSWER}':[4512]}
        self.assertDictEqual(expected, d.donors)
        del d

    def test_write_a_letter(self):
        d = Donor()
        """
        test that a single letter is written, saved as a text
        file and named correctly.
        """
        self.assertEqual(d.write_a_single_letter(ANSWER, AMOUNT), True)
        del d
        os.remove('New_Donor.txt')

    def test_view_donor_names(self):
        d = Donor()
        d.add_donor(ANSWER, AMOUNT)
        """
        test that function returns all donor names
        """
        self.assertEqual(d.view_donor_names(), print('New Donor'))
        del d


