#!/usr/bin/env python3
""" Mailroom v4 unittest assertions """

# Douglas Klos
# February 22nd, 2019
# Python 210, Session 6, Mailroom v4 test suite
# unittest_mailroom4.py

import unittest
import os
import sys
import shutil
import mailroom4 as mr


class Mailroom4Test(unittest.TestCase):
    """ Test assertsion for mailroom4 using unittest """

    def test_create_report(self):
        """ Test assertions for create_report """

        report = mr.create_report()

        for donor in mr.mailroom_db:
            if mr.mailroom_db[donor] == []:
                total_given = ' 0'
            else:
                total_given = f'$ {sum(mr.mailroom_db[donor]):18,.2f}'
                number_of_gifts = f'{len(mr.mailroom_db[donor]):10}'
                avg_donation = f'$ {sum(mr.mailroom_db[donor])/len(mr.mailroom_db[donor]):14,.2f}'

            # So we're just checking that the generated report contains the expected information.
            # It doesn't check for spacing errors but does format the numbers.
            # I could recreate the report here locally and compare to the returned string
            # but that felt like I was just copy pasting the function to the test file.
            self.assertIn(donor, report)
            self.assertIn(total_given, report)
            self.assertIn(number_of_gifts, report)
            self.assertIn(avg_donation, report)

    def test_send_thank_you(self):
        """ Test assertions for send_thank_you """

        self.assertEqual(mr.send_thank_you_note('Maggie', 5000),
                         '\nDonation in the amount of 5000 from Maggie not found')
        self.assertEqual(mr.send_thank_you_note('Mark', 5000),
                         '\nNo donation from Mark')
        self.assertEqual(mr.send_thank_you_note('Maggie', 2222),
                         mr.THANK_YOU_NOTE.format('Maggie', 2222))

    def test_write_thank_you_files(self):
        """
        Test assertions for write_thank_you_files

        We're testing the permissions on writeable directories
        and that the proper number of files was written to the
        specified directory.
        """

        self.assertEqual(mr.write_thank_you_files('/'),
                         '\nPermission denied, / is not writeable')
        self.assertEqual(mr.write_thank_you_files('/etc/'),
                         '\nPermission denied, /etc/ is not writeable')
        self.assertEqual(mr.write_thank_you_files('./thanks/'),
                         '\nThank you files written to ./thanks/')
        shutil.rmtree('./thanks/')

    def test_thank_you_file_contents(self):
        """
        Test that the contents of the thank you files is expected

        Writes a new set of thank you files to ./thanks/
        Checks that the correct number of files has been written.
        Loops through a reads new files, checks them against
        mailroom dictionary to verify expected values are present
        """

        mr.write_thank_you_files('./thanks/')
        file_count = len([name for name in os.listdir('./thanks/')])
        expected_count = len([key for key in mr.mailroom_db if mr.mailroom_db[key] != []])
        self.assertEqual(file_count, expected_count)

        for filename in os.listdir('./thanks/'):
            local_file = open('./thanks/' + filename)
            contents = local_file.read()
            local_file.close()
            name = contents[5:]
            name = name.split('\n')
            name[0] = name[0].replace(':', '')
            total_donations = f'{sum(mr.mailroom_db[name[0]]):,.2f}'
            most_recent = f'{mr.mailroom_db[name[0]][len(mr.mailroom_db[name[0]])-1]:,.2f}'
            self.assertIn(total_donations, contents)
            self.assertIn(most_recent, contents)

        shutil.rmtree('./thanks/')

    def test_add_donor_to_database(self):
        """ Test assertions for add_donor_to_databse """

        self.assertEqual(mr.add_donor_to_database('Douglas'),
                         '\nDouglas is already present in database')
        self.assertIn('Douglas', mr.mailroom_db)

        self.assertEqual(mr.add_donor_to_database('Paul'),
                         '\nPaul has been added to database')
        self.assertIn('Paul', mr.mailroom_db)

        self.assertEqual(mr.add_donor_to_database(''),
                         '\n is not a valid name')
        self.assertNotIn('', mr.mailroom_db)

    def test_add_donation_to_donor(self):
        """ Test assertions for add_donation_to_donor """

        self.assertEqual(mr.add_donation_to_donor('Douglas', 1000),
                         '\nDonation 1000 added to donor Douglas')
        self.assertIn(1000, mr.mailroom_db['Douglas'])

        self.assertEqual(mr.add_donation_to_donor('John', 1000),
                         '\nJohn not found in database')
        self.assertNotIn('John', mr.mailroom_db)

        self.assertEqual(mr.add_donation_to_donor('Douglas', 'bad_data'),
                         '\nbad_data is not a valid donation amount')
        self.assertNotIn('bad_data', mr.mailroom_db['Douglas'])

        self.assertEqual(mr.add_donation_to_donor('Douglas', -1000),
                         '\n-1000 is not a valid donation amount')
        self.assertNotIn(-1000, mr.mailroom_db['Douglas'])

    def test_remove_donor_from_database(self):
        """ Test assertions for remove_donor_from_database """

        self.assertEqual(mr.remove_donor_from_database('Douglas'),
                         '\nDouglas removed from database')
        self.assertNotIn('Douglas', mr.mailroom_db)

        self.assertEqual(mr.remove_donor_from_database('Peter'),
                         '\nPeter not found in database')
        self.assertNotIn('Peter', mr.mailroom_db)

    def test_remove_donation_from_donor(self):
        """ Test assertions for remove_donation_from_donor """

        self.assertEqual(mr.remove_donation_from_donor('Peter', 1000),
                         '\nPeter not found in database')
        self.assertNotIn('Peter', mr.mailroom_db)

        self.assertEqual(mr.remove_donation_from_donor('Jo', 8814),
                         '\nDonation 8814 has been removed from donor Jo')
        self.assertNotIn(8814, mr.mailroom_db['Jo'])

        self.assertEqual(mr.remove_donation_from_donor('Jo', 5000),
                         '\nDonation 5000 from donor Jo not found in database')
        self.assertNotIn(5000, mr.mailroom_db['Jo'])

        self.assertEqual(mr.remove_donation_from_donor('Jo', 'foo'),
                         '\nDonation foo from donor Jo not found in database')
        self.assertNotIn('foo', mr.mailroom_db['Jo'])


if __name__ == '__main__':
    if os.getuid() == 0:
        print('Do NOT run as root / sudo')
        sys.exit(1)
    unittest.main()
