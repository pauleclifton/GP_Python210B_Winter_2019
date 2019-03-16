#!/usr/bin/env python3

import unittest

from donor_collection import *

ANSWER = 'New_Donor'
AMOUNT = 4512


class OOMailroonTests(unittest.TestCase):

    def test_view_donor_names(self):
        dc = DonorCollection()
        """
        test that function returns all donor names
        """
        self.assertEqual(dc.view_donor_names(),
                         print('\nWilliam B\nSammy Maudlin\nSkip Bittman\nAshley Lashbrooke'))
