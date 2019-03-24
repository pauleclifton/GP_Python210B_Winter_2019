#!/usr/bin/env python3
#pylint: disable=C0103
""" Donor class pytest """

# Douglas Klos
# March 17th, 2019
# Python 210, Session 9, Mailroom OO
# test_donor.py


from donor import Donor


def test_init():
    """ Test initialization of donor objects """
    d1 = Donor('Maggie')
    d2 = Donor('Doug', 1000)
    d3 = Donor()
    assert d1.name == 'Maggie'
    assert d2.name == 'Doug'
    assert 1000 in d2.donations
    assert d3.name == ''
    d3.name = 'Sam'
    assert d3.name == 'Sam'


def test_donor_str():
    """ Tests donor __str__ method """
    d1 = Donor('Maggie', 1000, 2000, 3000)
    assert str(d1) == 'Maggie : [1000, 2000, 3000]'


def test_donor_repr():
    """ Tests donor __repr__ method """
    d1 = Donor('Maggie', 1000, 2000, 3000)
    assert repr(d1) == 'Maggie : [1000, 2000, 3000]'


def test_add_donation1():
    """ Test ability to add donations to donor """
    d1 = Donor('Maggie')
    d2 = Donor('Doug', 1000)
    d3 = Donor()
    d1.add_donation(1000)
    d2.add_donation(2000)
    d2.add_donation(3000)
    d3.add_donation(5000)
    assert 1000 in d1.donations
    assert 1000 in d2.donations
    assert 2000 in d2.donations
    assert 3000 in d2.donations
    assert 2000 not in d1.donations
    assert 5000 in d3.donations


def test_remove_donatio1():
    """ Test ability to remove donations from donor """
    d1 = Donor('Maggie', 1000, 2000, 3000)
    d2 = Donor('Doug', 1111, 2222, 3333, 4444, 5555)
    d1.remove_donation(1000)
    d1.remove_donation(2000)
    d2.remove_donation(5555)
    d2.remove_donation(1111)
    assert 3000 in d1.donations
    assert 1000 not in d1.donations
    assert 2000 not in d1.donations
    assert 1111 not in d2.donations
    assert 5555 not in d2.donations
    message = d1.remove_donation(1337)
    assert message == f'Donation 1337 not found for {d1.name}'


def test_total_donations():
    """ Test total_donations property """
    d1 = Donor('Maggie', 1000, 2000, 3000)
    assert d1.total_donations == 6000
    d1.add_donation(4000)
    assert d1.total_donations == 10000
    d1.remove_donation(1000)
    assert d1.total_donations == 9000


def test_average_donation():
    """ Test average_donation property """
    d1 = Donor('Maggie', 1000, 2000, 3000)
    assert d1.average_donation == 2000
    d1.add_donation(4000)
    assert d1.average_donation == 2500
    d1.remove_donation(1000)
    assert d1.average_donation == 3000


def test_change_donor_name():
    """ Test ability to change donors name. """
    d1 = Donor('Maggie', 1000, 2000, 3000)
    assert d1.name == 'Maggie'
    d1.name = 'Doug'
    assert d1.name == 'Doug'
