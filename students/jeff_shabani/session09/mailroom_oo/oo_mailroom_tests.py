#!/usr/bin/env python3

# Jeff Shabani
# March 2019
# Python 210, Session 9
# donor_models.py

import mock
import students
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
        d = CommandLineInterface(donors_test)
        """
        test that a single letter is written, the text is correct
        file and named correctly.
        """
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


    def test_all_donor_letters_created(self):
        """
        test that letters were written to all donors"""
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
        # os.remove(letters_to_write[0])
        # for letter in letters_to_write[2]:
        #     os.remove(letter)
        old_dir = r'C:\JRS\Python\UW\Intro_Klass\students\jeff_shabani\session09\mailroom_oo'
        os.chdir(old_dir)

    def test_letter_text_from_all_donors_letter_creation(self):
        """
        test letter text from batch letter writing"""
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
        """test console output of donors names"""
        d = CommandLineInterface(donors_test)
        with patch ('sys.stdout', new=StringIO()) as mocked_output:
            d.view_donor_names()
            self.assertEqual(mocked_output.getvalue().strip(), f'Karsten Willems\nSammy Maudlin')
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

    @mock.patch('builtins.input', mock.Mock(return_value=None))
    def test_set_letter_dir_path_no_change(self):
        #tests for that letter patch is cwd
        expected = os.getcwd()
        self.assertEqual(CommandLineInterface.set_letter_directory_path_path(self), expected)




if __name__ == '__main__':
    unittest.main()
