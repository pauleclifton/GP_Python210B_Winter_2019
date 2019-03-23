#!/usr/bin/env python3
#pylint: disable=C0103
""" Mailroom OO pytest """

# Douglas Klos
# March 17th, 2019
# Python 210, Session 9, Mailroom OO
# test_mailroom.py


import os
import shutil
import datetime
import pytest
import mailroom as mr


def test_display_report():
    """ Tests that reports contain the correct information """
    mr.initialize_donors()
    report = mr.text_report()

    print(report)
    for name in mr.mailroom.database.keys():
        assert name in report
        assert f'{mr.mailroom.database[name].total_donations:,.2f}' in report
        assert f'{mr.mailroom.database[name].average_donation:,.2f}' in report


def test_html_report():
    """ Tests that reports contain the correct information """
    mr.initialize_donors()

    assert mr.html_report() == f'HTML report saved to ./mailroom.html'
    assert os.path.isfile('./mailroom.html')
    with open('./mailroom.html') as filename:
        report = filename.read()

    print(report)
    for name in mr.mailroom.database.keys():
        assert name in report
        assert f'{mr.mailroom.database[name].total_donations:,.2f}' in report
        assert f'{mr.mailroom.database[name].average_donation:,.2f}' in report


def test_thank_you_note(monkeypatch):
    """ Tests that you can send a thank you note """
    mr.initialize_donors()

    monkeypatch.setattr('builtins.input', lambda x: 'Maggie')
    assert mr.thank_you_note() == mr.display_thank_you_note('Maggie')

    monkeypatch.setattr('builtins.input', lambda x: 'Doug')
    assert mr.thank_you_note() == 'Donor Doug not found.'

    assert mr.THANK_YOU_LETTER.format(mr.mailroom.database['Maggie'].name,
                                      mr.mailroom.database['Maggie'].donations[-1],
                                      mr.mailroom.database['Maggie'].total_donations) ==\
           mr.display_thank_you_note('Maggie')


def test_thank_you_files(monkeypatch):
    """ Tests that donordb writes the correct thank you files """
    mr.initialize_donors()

    monkeypatch.setattr('builtins.input', lambda x: '')
    mr.thank_you_files('')
    file_count = len([name for name in os.listdir('./thanks/')])
    assert file_count == 7
    shutil.rmtree('./thanks/')
    assert mr.thank_you_files('/') == f'Permission denied, / is not writeable'
    assert mr.thank_you_files('/etc/nope') == f'Permission denied, /etc/nope is not writeable'


def test_write_thank_you_letter():
    """ Test that a thank you letter is written to the disk containing the correct information """
    mr.initialize_donors()
    now = datetime.datetime.now()
    mr.write_thank_you_letter('.', 'Maggie')
    assert os.path.isfile('Maggie ' + now.strftime("%Y-%m-%d") + ".txt")

    with open('./Maggie ' + now.strftime("%Y-%m-%d") + ".txt") as filename:
        contents = filename.read()
        total_donations = f'{mr.mailroom.database["Maggie"].total_donations:,.2f}'
        most_recent = f'{mr.mailroom.database["Maggie"].donations[-1]:,.2f}'
        assert mr.mailroom.database["Maggie"].name in contents
        assert total_donations in contents
        assert most_recent in contents

    os.remove('./Maggie ' + now.strftime("%Y-%m-%d") + ".txt")

    with pytest.raises(PermissionError):
        mr.write_thank_you_letter('/', 'Maggie')


def test_get_value1(monkeypatch):
    """ Passing test of user input get_value """
    mr.initialize_donors()
    monkeypatch.setattr('builtins.input', lambda x: 4)
    value = mr.get_value('Enter a float', float)
    assert value == float('4')


def test_get_value2(monkeypatch):
    """ Passing test of user input get_value """
    mr.initialize_donors()
    monkeypatch.setattr('builtins.input', lambda x: 'string')
    value = mr.get_value('Enter a string', str)
    assert value == 'string'


def test_get_value3(monkeypatch):
    """ Passing test of user input get_value """
    mr.initialize_donors()
    monkeypatch.setattr('builtins.input', lambda x: 10.2)
    value = mr.get_value('Enter a string', float)
    assert value == 10.2


def test_add_donor(monkeypatch):
    """ Tests adding a donor through UI """
    mr.initialize_donors()
    monkeypatch.setattr('builtins.input', lambda x: 'Koko')
    mr.add_donor()
    assert 'Koko' in mr.mailroom.database
    monkeypatch.setattr('builtins.input', lambda x: 'q')
    mr.add_donor()
    assert 'Kupo' not in mr.mailroom.database


def test_remove_donor(monkeypatch):
    """ Tests removing a donor """
    mr.initialize_donors()
    assert 'Mark' in mr.mailroom.database
    monkeypatch.setattr('builtins.input', lambda x: 'Mark')
    mr.remove_donor()
    assert 'Mark' not in mr.mailroom.database
    monkeypatch.setattr('builtins.input', lambda x: 'q')
    mr.remove_donor()
    assert 'Mark' not in mr.mailroom.database


def test_remove_donation(monkeypatch):
    """ Tests removing a donation """
    #We still need an assert, don't know how to mock two user input on one call
    mr.initialize_donors()
    monkeypatch.setattr('mailroom.get_value', lambda x, y: 'Koko')
    mr.remove_donation()
    monkeypatch.setattr('mailroom.get_value', lambda x, y: 'q')
    mr.remove_donation()
    # assert False


def test_add_donation(monkeypatch):
    """ Tests adding a donation """
    #We still need an assert, don't know how to mock two user input on one call
    mr.initialize_donors()
    monkeypatch.setattr('mailroom.get_value', lambda x, y: 'Koko')
    mr.add_donation()
    monkeypatch.setattr('mailroom.get_value', lambda x, y: 'q')
    mr.add_donation()
    # assert False


def test_rename_donor(monkeypatch):
    """ Tests renaming a donor """
    #Not finished
    mr.initialize_donors()
    monkeypatch.setattr('mailroom.get_value', lambda x, y: 'q')
    mr.rename_donor()
    # assert False
