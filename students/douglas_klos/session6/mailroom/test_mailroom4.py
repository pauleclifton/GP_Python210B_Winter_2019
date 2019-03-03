#!/usr/bin/env python3
""" Mailroom v4 assertions """

# Douglas Klos
# February 22nd, 2019
# Python 210, Session 6, Mailroom v4 test suite
# test_mailroom4.py

import os
import shutil
import mailroom4 as mr


# Test cases for send_thank_you

def test_get_value1(monkeypatch):
    """ Passing test of user input get_value """

    monkeypatch.setattr('builtins.input', lambda x: 4)
    value = mr.get_value('Enter a float', float)
    assert value == float('4')


def test_get_value2(monkeypatch):
    """ Passing test of user input get_value """

    monkeypatch.setattr('builtins.input', lambda x: 'string')
    value = mr.get_value('Enter a string', str)
    assert value == 'string'


def test_get_value3(monkeypatch):
    """ Passing test of user input get_value """

    monkeypatch.setattr('builtins.input', lambda x: 10.2)
    value = mr.get_value('Enter a string', float)
    assert value == 10.2


def test_create_report():
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
        assert donor in report
        assert total_given in report
        assert number_of_gifts in report
        assert avg_donation in report


def test_send_thank_you1():
    """ Test case for send_thank_you """

    assert mr.send_thank_you_note('Maggie', 5000)\
           == '\nDonation in the amount of 5000 from Maggie not found'


def test_send_thank_you2():
    """ Test case for send_thank_you """

    assert mr.send_thank_you_note('Mark', 5000)\
           == '\nNo donation from Mark'


def test_send_thank_you3():
    """ Test case for send_thank_you """

    assert mr.send_thank_you_note('Maggie', 2222)\
           == mr.THANK_YOU_NOTE.format('Maggie', 2222)


# Test cases for writing thank you files

def test_write_thank_you_files1():
    """ Test case for write_thank_you_files """

    # if root / sudo this will make a mess, so we double check
    if os.getuid() != 0:
        assert mr.write_thank_you_files('/')\
               == '\nPermission denied, / is not writeable'


def test_write_thank_you_files2():
    """ Test case for write_thank_you_files """

    # if root / sudo this will make a mess, so we double check
    if os.getuid() != 0:
        assert mr.write_thank_you_files('/etc/')\
               == '\nPermission denied, /etc/ is not writeable'


def test_write_thank_you_files3():
    """ Test case for write_thank_you_files """

    assert mr.write_thank_you_files('./thanks/')\
           == '\nThank you files written to ./thanks/'


def test_write_thank_you_files4():
    """ Test case for write_thank_you_files """

    file_count = len([name for name in os.listdir('./thanks/')])
    expected_count = len([key for key in mr.mailroom_db if mr.mailroom_db[key] != []])
    assert file_count == expected_count


def test_thank_you_file_contents():
    """
    Test that the contents of the thank you files is expected

    Loops through a reads thank you files, checks them against
    mailroom dictionary to verify expected values are present.
    """

    for filename in os.listdir('./thanks/'):
        local_file = open('./thanks/' + filename)
        contents = local_file.read()
        local_file.close()
        name = contents[5:]
        name = name.split('\n')
        name[0] = name[0].replace(':', '')
        total_donations = f'{sum(mr.mailroom_db[name[0]]):,.2f}'
        most_recent = f'{mr.mailroom_db[name[0]][len(mr.mailroom_db[name[0]])-1]:,.2f}'
        assert total_donations in contents
        assert most_recent in contents

    shutil.rmtree('./thanks/')


# Test cases for add_donor_to_database

def test_add_donor_to_database1():
    """ Test case for add_donor_to_database """

    assert mr.add_donor_to_database('Douglas')\
           == '\nDouglas is already present in database'
    assert 'Douglas' in mr.mailroom_db


def test_add_donor_to_database2():
    """ Test case for add_donor_to_database """

    assert mr.add_donor_to_database('Paul')\
           == '\nPaul has been added to database'
    assert 'Paul' in mr.mailroom_db


def test_add_donor_to_database3():
    """ Test case for add_donor_to_database """

    assert mr.add_donor_to_database('')\
           == '\n is not a valid name'
    assert '' not in mr.mailroom_db


# Test cases for add_donation_to_donor

def test_add_donation_to_donor1():
    """ Test case for add_donation_to_donor """

    assert mr.add_donation_to_donor('Douglas', 1000)\
           == '\nDonation 1000 added to donor Douglas'
    assert 1000 in mr.mailroom_db['Douglas']


def test_add_donation_to_donor2():
    """ Test case for add_donation_to_donor """

    assert mr.add_donation_to_donor('John', 1000)\
           == '\nJohn not found in database'
    assert 'John' not in mr.mailroom_db


def test_add_donation_to_donor3():
    """ Test case for add_donation_to_donor """

    assert mr.add_donation_to_donor('Douglas', 'bad_data')\
           == '\nbad_data is not a valid donation amount'
    assert 'bad_data' not in mr.mailroom_db['Douglas']


def test_add_donation_to_donor4():
    """ Test case for add_donation_to_donor """

    assert mr.add_donation_to_donor('Douglas', -1000)\
           == '\n-1000 is not a valid donation amount'
    assert -1000 not in mr.mailroom_db['Douglas']


# Test cases for remove_donor_from_databse

def test_remove_donor_from_database1():
    """Test case for remove_donor_from_database """

    assert mr.remove_donor_from_database('Douglas')\
           == '\nDouglas removed from database'
    assert 'Douglas' not in mr.mailroom_db


def test_remove_donor_from_database2():
    """Test case for remove_donor_from_database """

    assert mr.remove_donor_from_database('Peter')\
           == '\nPeter not found in database'
    assert 'Peter' not in mr.mailroom_db


# Test cases for remove_donation_from_donor

def test_remove_donation_from_donor1():
    """ Test case for remove_donation_from_donor """

    assert mr.remove_donation_from_donor('Peter', 1000)\
           == '\nPeter not found in database'
    assert 'Peter' not in mr.mailroom_db


def test_remove_donation_from_donor2():
    """ Test case for remove_donation_from_donor """

    assert mr.remove_donation_from_donor('Jo', 8814)\
           == '\nDonation 8814 has been removed from donor Jo'
    assert 8814 not in mr.mailroom_db['Jo']


def test_remove_donation_from_donor3():
    """ Test case for remove_donation_from_donor """

    assert mr.remove_donation_from_donor('Jo', 5000)\
           == '\nDonation 5000 from donor Jo not found in database'
    assert 5000 not in mr.mailroom_db['Jo']


def test_remove_donation_from_donor4():
    """ Test case for remove_donation_from_donor """

    assert mr.remove_donation_from_donor('Jo', 'foo')\
           == '\nDonation foo from donor Jo not found in database'
    assert 'foo' not in mr.mailroom_db['Jo']
