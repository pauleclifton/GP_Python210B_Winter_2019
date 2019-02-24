#!/usr/local/bin/python3
'''
Beginning of my mailroom unittest implementation.
'''

import os
import datetime
import shutil
import mailroom
'''
Importing the modules we will need, and mailroom.py
'''


def test_one(capsys):
    '''
    Testing the report function
    '''

    mailroom.donor_report()
    captured = capsys.readouterr()
    assert captured.out.startswith("\n-----------------------------------\
---------------------------------------------")
    assert "Dave Lombardo     | $9,918.11           | 3             \
  | $3,306.04" in captured.out


def test_two(capsys):
    '''
    Testing the list functions
    '''

    mailroom.donor_list()
    captured = capsys.readouterr()
    assert "Robert Smith" in captured.out
    assert "JD Cronise" in captured.out


def test_three(capsys):
    '''
    Testing the send mail functions
    '''

    current_donor = "Devin Townsand"
    mailroom.mail_send(current_donor)
    captured = capsys.readouterr()
    assert "Devin Townsand" in captured.out
    assert "$6,186.49" in captured.out

    path = os.getcwd()

    directory = path + '/donors/' + current_donor + '/'
    shutil.rmtree(directory)

def test_four():
    '''
    Testing file writing functions
    '''
    path = os.getcwd()
    donors = mailroom.donors
    current_donor = "Chris Stapleton"

    MAIL = mailroom.MAIL #this has to be caps, because of the program we are
                         #testing against.

    donor_math = donors[current_donor]
    directory = path + '/donors/' + current_donor + '/'
    filename = current_donor + ' - ' \
        + datetime.datetime.now().strftime('%s') + '.txt'

    mailroom.mail_format(current_donor, donor_math, directory, filename)

    print('\n')
    print(MAIL.format(current_donor, (sum(donor_math)), (len(donor_math))))

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(directory + filename, 'w+') as outfile:
        outfile.write('{}\n'.format(MAIL.format(current_donor,\
        (sum(donor_math)), (len(donor_math)))))

    with open(directory + filename, 'r+') as infile:
        check = infile.read()
        total = sum(donor_math)
        assert current_donor in check
        assert "$" + str(total) in check

    shutil.rmtree(path + '/donors/')


def test_five(monkeypatch, capsys):
    '''
    Testing valid input
    '''
    def mock_input(prompt):
        print(prompt)
        return 'list'
    monkeypatch.setattr('builtins.input', mock_input)
    i = input("List of Donors")
    captured = capsys.readouterr()
    assert i == "list"
    assert "List of Donors" in captured.out


def test_six(monkeypatch, capsys):
    '''
    Testing invalid input
    '''
    def mock_input(prompt):
        print(prompt)
        return 'asdf'
    monkeypatch.setattr('builtins.input', mock_input)
    i = input("ERROR: Invalid option")
    captured = capsys.readouterr()
    assert i == "asdf"
    assert "ERROR: Invalid option" in captured.out
