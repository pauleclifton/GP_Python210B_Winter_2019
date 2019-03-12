#!/usr/bin/env python3

# Jeff Shabani
# March 12th, 2019
# Python 210, Session 8
# donor_collection_tests.py

import unittest

from students.jeff_shabani.session09.donor_collection import *

ANSWER = 'New_Donor'
AMOUNT = 4512

# donors = {'William B': [120, 130, 50],
#           'Sammy Maudlin': [500, 125, 670, 1000],
#           'Bobby Bittman': [10],
#           'Skip Bittman': [75, 125, 19],
#           'Ashley Lashbrooke': [10000, 15000]}


class OOMailroonTests(unittest.TestCase):

    def test_view_donor_names(self):
        dc = DonorCollection()
        """
        test that function returns all donor names
        """
        self.assertEqual(dc.view_donor_names(),
                         print('\nWilliam B\nSammy Maudlin\nSkip Bittman\nAshley Lashbrooke'))
        del dc

    def test_new_donor_dictionary(self):
        dc = DonorCollection()
        """
        tests values of a single dictionary key of the new donor
        dictionary
        """
        self.maxDiff = None
        result = dc.create_new_donors_dict()
        self.assertEqual(result['Ashley Lashbrooke'], (25000, 2, 1.0))
