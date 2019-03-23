#!/usr/bin/env python3
#pylint: disable=C0103
"""DonorDB class pytest """

# Douglas Klos
# March 17th, 2019
# Python 210, Session 9, Mailroom OO
# test_donordb.py


import os
import pytest
from donor import Donor
from donordb import DonorDB as db


def test_init_donordb():
    """ Tests ability to initialze a databse of multiple donor objects """
    Donor('Maggie')
    Donor('Doug', 1000)
    Donor('ｷﾗ', 9001)


def test_donordb_str():
    """ Tests donordb __str__ method """
    d1 = Donor('Maggie', 1000, 2000, 3000)
    d2 = Donor('Doug', 1111, 2222, 3333, 4444, 5555)
    d3 = Donor('ｷﾗ', 9001)
    db1 = db()
    db1.add_donor(d1)
    db1.add_donor(d2)
    db1.add_donor(d3)
    string = f'{d1.name:>24} : {d1.donations}\n'
    string += f'{d2.name:>24} : {d2.donations}\n'
    string += f'{d3.name:>24} : {d3.donations}\n'
    assert string == str(db1)


def test_donordb_repr():
    """ Tests donordb __repr__ method """
    d1 = Donor('Maggie', 1000, 2000, 3000)
    d2 = Donor('Doug', 1111, 2222, 3333, 4444, 5555)
    d3 = Donor('ｷﾗ', 9001)
    db1 = db()
    db1.add_donor(d1)
    db1.add_donor(d2)
    db1.add_donor(d3)
    string = f'{d1.name:>24} : {d1.donations}\n'
    string += f'{d2.name:>24} : {d2.donations}\n'
    string += f'{d3.name:>24} : {d3.donations}\n'
    assert string == repr(db1)


def test_add_donor():
    """ Tests that you can add a donor to the database """
    d1 = Donor('Maggie')
    d2 = Donor('Doug', 1000)
    d3 = Donor('ｷﾗ', 9001)
    db1 = db(d1)
    db1.add_donor(d2)
    db1.add_donor(d3)
    assert str(d1) in str(db1.database)
    assert str(d2) in str(db1.database)
    assert str(d3) in str(db1.database)
    assert db1.add_donor('Maggie') == 'Maggie already exists in database'
    assert db1.add_donor('Kurami') == 'Kurami has been added to the database'
    assert 'Kurami' in str(db1.database)


def test_add_donation2():
    """ Tests that you can add a donation to the database """
    d1 = Donor('Maggie')
    db1 = db(d1)
    assert 2000 not in db1.database['Maggie'].donations
    db1.add_donation('Maggie', 2000)
    assert 2000 in db1.database['Maggie'].donations
    db1.add_donation('Maggie', 5000)
    assert 5000 in db1.database['Maggie'].donations
    assert db1.add_donation('Maggie', int('-1000')) == '-1000 is not a valid donation amount'
    assert -1000 not in db1.database
    assert db1.add_donation('Maggie', 'foobar') == 'foobar is not a valid donation amount'
    assert 'foobar' not in db1.database
    assert db1.add_donation('Doug', 1000) == 'Doug not found in database'
    assert 1000 not in db1.database


def test_remove_donor():
    """ Tests ability to remove a donor from donordb """
    d1 = Donor('Maggie', 1000, 2000, 3000)
    d2 = Donor('Doug', 1111, 2222, 3333, 4444, 5555)
    d3 = Donor('ｷﾗ', 9001)
    db1 = db()
    db1.add_donor(d1)
    db1.add_donor(d2)
    db1.add_donor(d3)
    assert str(d1) in str(db1.database)
    db1.remove_donor('Maggie')
    assert str(d1) not in str(db1.database)
    assert str(d2) in str(db1.database)
    db1.remove_donor('Doug')
    assert str(d2) not in str(db1.database)
    assert db1.remove_donor('Kurami') == 'Kurami not found in database'
    assert 'Kurami' not in db1.database


def test_remove_donation():
    """ Test ability to remove a donation from a donor """
    d1 = Donor('Maggie', 1000, 2000, 3000)
    db1 = db(d1)
    assert 1000 in d1.donations
    db1.remove_donation('Maggie', 1000)
    assert 1000 not in d1.donations
    assert 2000 in d1.donations
    db1.remove_donation('Maggie', 2000)
    assert 2000 not in d1.donations
    assert db1.remove_donation('Doug', 2000) ==\
        'Donation 2000 from donor Doug not found in database'


def test_save_db_to_disk():
    """ Tests that you can save the database to disk """
    d1 = Donor('Maggie', 1000, 2000, 3000)
    d2 = Donor('Doug', 1111, 2222, 3333, 4444, 5555)
    d3 = Donor('ｷﾗ')
    db1 = db()
    db1.add_donor(d1)
    db1.add_donor(d2)
    db1.add_donor(d3)
    db1.save_db_to_disk('./test_db.pkl')
    assert os.path.isfile('./test_db.pkl')
    os.remove('./test_db.pkl')


def test_read_db_from_disk():
    """ Tests that database can be loaded from disk """
    d1 = Donor('Maggie', 1000, 2000, 3000)
    d2 = Donor('Doug', 1111, 2222, 3333, 4444, 5555)
    d3 = Donor('ｷﾗ')
    db1 = db()
    db1.add_donor(d1)
    db1.add_donor(d2)
    db1.add_donor(d3)
    db2 = db()
    db1.save_db_to_disk('./test_db.pkl')
    db2.read_db_from_disk('./test_db.pkl')
    assert str(d1) in str(db2.database)
    assert str(d2) in str(db2.database)
    assert str(d3) in str(db2.database)
    os.remove('./test_db.pkl')

    with pytest.raises(FileNotFoundError):
        db2.read_db_from_disk('./test_db.pkl')


def test_rename_donor():
    """ Tests that you can rename a donor """
    d1 = Donor('Light', 1000, 2000, 3000)
    d2 = Donor('Doug', 1111, 2222, 3333, 4444, 5555)
    db1 = db()
    db1.add_donor(d1)
    db1.add_donor(d2)

    db1.rename_donor('Light', 'ｷﾗ')
    assert 'Light' not in str(db1.database)
    assert 'ｷﾗ' in str(db1.database)
    assert db1.rename_donor('Light', 'ｷﾗ') == 'Donor ｷﾗ already exists in database'
    assert db1.rename_donor('ｷﾗ', 'Doug') == 'Donor Doug already exists in database'
