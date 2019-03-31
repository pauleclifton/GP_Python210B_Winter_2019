#!/usr/bon/env python3

import os
import sys
import datetime
import unittest

import mailroom4 as mr4

mr4.donor_db = mr4.donor_db()

def test_donor_list():
    """ test to see if donors are showing up in list"""
    donors = mr4.donor_db.keys()
    assert len(donors) == 5
    assert "Tao Chien" in donors
    assert "Eliza Sommers" in donors


def test_no_donor_search():
    """ test that a new donor doesn't show up"""
    donor = mr4.donor_db.get("Mama Fresia")
    assert donor is None


def test_donor_search():
    """ test that an existing donor is there"""
    donors = mr4.donor_db.keys()
    assert "Joaquin Andieta" in donors


def test_gen_single_letter():
    """test that the donor letter/message is generated
    bring in a test donor, then check the letter"""
    expected = "Dear Jacob Todd, \n\n Thank you for your generous donation of $    100.00. \n You have helped make a big impact on the community!"
    assert mr4.generate_letter("Jacob Todd", 100.00) == expected


def test_donor_addition():
    """ test that new donor is added
    created a test new donor and donation, then check that new donor is in the donor_db"""
    name = "Isabel Allende"
    donation = 2500
    mr4.donor_db.setdefault(name, []).append(donation)
    donors = mr4.donor_db.keys()
    don_amt = mr4.donor_db.values()
    assert "Isabel Allende" in donors
    assert mr4.donor_db.get("Isabel Allende") == [2500]


def test_create_report():
    """ test that the donor report is created
    using a random line from the report to test that it displays correctly"""
    expected = "Paulina Rodriguez               $    50000.00                 1  $    50000.00"
    assert mr4.report_line(["Paulina Rodriguez", 50000, 1, 50000]) == expected


def test_gen_letters():
    """ test that letters were generated to separate files
    mailroom4.py, option 2 has to be run first otherwise there's nothing to test against"""
    path = os.getcwd()
    folder = path + '/donor_letters/'
    os.chdir(folder)
    timestamp = str(datetime.date.today())
    assert os.path.isfile('Tao Chien_'+timestamp+'.txt')
    assert os.path.isfile('Joaquin Andieta_'+timestamp+'.txt')

def test_get_letter_text():
    """ test that content of generated letters is pulling in the name correctly
    we don't want the letter to be addressed to the wrong person"""
    expected = "Dear Eliza Sommers, \n\n On behalf of all of us, we thank your for your generous donation. \n You have helped make a big impact on the community!"
    assert mr4.thank_you_all_text('Eliza Sommers') == expected

if __name__ == "__main__":
    test_donor_list()
    test_no_donor_search()
    test_donor_search()
    test_gen_single_letter()
    test_donor_addition()
    test_create_report()
    test_gen_letters()
    print("All the tests passed!")

