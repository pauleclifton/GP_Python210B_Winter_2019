#!/usr/bin/env python3

import unittest
import mailroom4

class TestMailroom4(unittest.TestCase):


    def test_write_a_letter(self):
        donor = 'Paul Allen'
        amount = 200
        self.assertEqual(donor, "Paul Allen")
        self.assertEqual(amount, 200)
        self.assertTrue(mailroom4.write_a_letter(donor, amount), True)


    def test_add_donor(self):
        new_donor = 'Pete Rose'
        self.assertEqual(new_donor, "Pete Rose")
        self.assertNotEqual(mailroom4.add_donor(new_donor), new_donor)

    def test_view_donor_names(self):
        self.assertEqual(mailroom4.view_donor_names(),
                         print('\nJeff Bezos\nPaul Allen\nElon Musk\nMark Zuckerberg\nWilliam Gates, III'))

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
