#!/usr/bin/env python3

# Jeff Shabani
# March 2019
# Python 210, Session 9
# donor_models.py

import mock
import shutil
import students
import tempfile
import unittest


from io import StringIO
from cli_main import *
from unittest.mock import patch

"""
Test for mailroom_oo. Note: these are not complete."""

ANSWER = 'New_Donor'
AMOUNT = 4512

donors_test = {'Karsten Willems': [120, 130, 50],
               'Sammy Maudlin': [500, 125, 670, 1000]
               }
#use for testing setting new letter path
new_dir = r'C:\JRS\Python\UW\Intro_Klass\students\jeff_shabani\session09\letter_tests'

class OOMailroomTests(unittest.TestCase):

    def test_add_donor(self):
        d = CommandLineInterface(donors_test)
        d.add_donor(ANSWER, AMOUNT)
        self.assertIn(ANSWER, d.donors)
        self.assertIn(AMOUNT, d.donors[ANSWER])
        #remove new donor from dictionary
        del donors_test[ANSWER]
        del d

    def test_write_a_letter(self):
        """
        Test that a single letter is written, the text is correct
        file and named correctly. Letter is deleted after test completion.
        """
        d = CommandLineInterface(donors_test)
        self.assertEqual(d.write_a_single_letter(ANSWER, AMOUNT), True)
        with open('New_Donor.txt', 'rt') as infile:
            lines = infile.readlines()
            self.assertEqual(lines[0], f'Dear {ANSWER},\n')
            self.assertEqual(lines[1], '\n')
            self.assertEqual(lines[2], f'Thank you for your kind donation of ${AMOUNT:,.0f}\n')
            self.assertEqual(lines[3], '\n')
            self.assertEqual(lines[4], 'Rest assured that these funds will be put to optimal use.\n')
            self.assertEqual(lines[5], '\n')
            self.assertEqual(lines[6], 'Best regards,\n')
            self.assertEqual(lines[7], 'The Charitable Charities Team')
        del d
        os.remove('New_Donor.txt')

    def test_new_dictionary(self):
        """
        Tests content of new dictionary used for report."""
        d = CommandLineInterface(donors_test)
        expected = {k: (sum(v), len(v), (sum(v) / len(v))) for k, v in donors_test.items()}
        self.assertDictEqual(d.create_new_donors_dict(), expected)
        del d

    def test_all_donor_letters_created(self):
        """
        Test that letters were written to all donors. Creates list of
        letters and compares that list against list of expected letters.
        """
        lt = CommandLineInterface(donors_test)
        new_dir = r'C:\JRS\Python\UW\Intro_Klass\students\jeff_shabani\session09\letter_tests'
        os.chdir(new_dir)
        lt.write_letters_to_all_donors()
        cd = os.getcwd()
        for items in os.walk(cd):
            files = [item for item in items[2]]
        letters_to_write = ['Karsten Willems.txt', 'read_letters.py', 'Sammy Maudlin.txt']
        for file in files:
            self.assertIn(file, letters_to_write)
        old_dir = r'C:\JRS\Python\UW\Intro_Klass\students\jeff_shabani\session09\mailroom_oo'
        os.chdir(old_dir)

    def test_letter_text_from_all_donors_letter_creation(self):
        """
        Test letter text from batch letter writing. Test accuracy
        of content of single letter, with the assumption that the
        text for all letters will be the same. Letters are deleted
        after tests are run.
        """
        lt = CommandLineInterface(donors_test)
        new_dir = r'C:\JRS\Python\UW\Intro_Klass\students\jeff_shabani\session09\letter_tests'
        os.chdir(new_dir)
        with open('Karsten Willems.txt', 'rt') as infile:
            lines = infile.readlines()
            self.assertEqual(lines[0], 'Dear Karsten Willems,\n')
            self.assertEqual(lines[1], '\n')
            self.assertEqual(lines[2], 'Thank you for your kind donation of $300\n')
            self.assertEqual(lines[3], '\n')
            self.assertEqual(lines[4], 'Rest assured that these funds will be put to optimal use.\n')
            self.assertEqual(lines[5], '\n')
            self.assertEqual(lines[6], 'Best regards,\n')
            self.assertEqual(lines[7], 'The Charitable Charities Team')
        letters_to_delete = ['Karsten Willems.txt','Sammy Maudlin.txt']
        for letter in letters_to_delete:
            os.remove(letter)
        old_dir = r'C:\JRS\Python\UW\Intro_Klass\students\jeff_shabani\session09\mailroom_oo'
        os.chdir(old_dir)

    def test_view_donor_names(self):
        """Test console output of donors names"""
        d = CommandLineInterface(donors_test)
        with patch ('sys.stdout', new=StringIO()) as mocked_output:
            d.view_donor_names()
            self.assertEqual(mocked_output.getvalue().strip(), f'Karsten Willems\nSammy Maudlin')
        del d

    def test_program_quit(self):
        """Test that the program quits properly"""
        d = CommandLineInterface(donors_test)
        with self.assertRaises(SystemExit):
            d.quit_the_program()
        del d

    def test_run_report(self):
        """Test console output when report is run"""
        d = CommandLineInterface(donors_test)
        header = f'{"Name".ljust(20)}{"| Total Donations".rjust(20)}{"| # of Donations".rjust(20)}' \
            f'{"| Average Donation".rjust(20)}'

        dashes = '-' * len(header)
        donor_one_name= 'Sammy Maudlin'
        donor_one_total = 2295
        donor_one_count = 4
        donor_one_mean = 573.75

        donor_zwei_name= 'Karsten Willems'
        donor_zwei_total = 300
        donor_zwei_count = 3
        donor_zwei_mean = 100.0

        first_line = f'{donor_one_name.ljust(20)}{str(donor_one_total).rjust(20)}{str(donor_one_count).rjust(20)}' \
            f'{str(donor_one_mean).rjust(20)}'
        zweite_line = f'{donor_zwei_name.ljust(20)}{str(donor_zwei_total).rjust(20)}{str(donor_zwei_count).rjust(20)}' \
            f'{str(donor_zwei_mean).rjust(20)}'

        with patch ('sys.stdout', new=StringIO()) as mocked_output:
            d.create_report()
            self.assertEqual(mocked_output.getvalue().strip(), f'{header}\n{dashes}\n{first_line}\n{zweite_line}')
        del d

    @mock.patch('builtins.input', mock.Mock(return_value='54'))
    def test_get_value_2(self):
        self.assertEqual(CommandLineInterface.get_value(self, 'Enter a value:', int), 54)

    @mock.patch('builtins.input', mock.Mock(return_value='54'))
    @unittest.expectedFailure
    def test_get_wrong_input(self):
        self.assertEqual(CommandLineInterface.get_value(self, 'Enter a value:', str), 'Incorrect data type')

    @mock.patch('builtins.input', mock.Mock(return_value=None))
    def test_set_letter_dir_path_no_change(self):
        """
        tests for that letter patch is cwd when no path is entered"""
        expected = os.getcwd()
        self.assertEqual(CommandLineInterface.set_letter_directory_path_path(self), expected)

    @mock.patch('builtins.input', mock.Mock(return_value=new_dir))
    def test_set_letter_dir_path_new(self):
        d = CommandLineInterface(donors_test)
        os.chdir(new_dir)
        expected = os.getcwd()
        d.set_letter_directory_path_path()
        self.assertEqual(new_dir, expected)
        del d


if __name__ == '__main__':
    unittest.main()
