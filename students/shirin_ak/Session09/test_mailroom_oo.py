import os
import pytest
from donor_models import Donor
from donor_models import DonorCollection

def test_donor_init():
    donor1 = Donor('William Gates ')
    assert donor1.name == 'William Gates '
    donor1.add_donations(30000)
    donor1.add_donations(20000)
    assert donor1.num_donations == 2

def test_add_donation():
    """test donation is adding"""
    test_donor = Donor("David")
    test_donor.add_donations(1000)
    assert test_donor.donation == [1000.00]
    test_donor.add_donations(800.50)
    assert test_donor.donation == [1000.00, 800.50]

def test_count_donation():
    """test count donation is working"""
    test_donor = Donor('William Gates ')
    assert test_donor.name == 'William Gates '
    test_donor.add_donations(30000)
    test_donor.add_donations(20000)
    assert test_donor.num_donations == 2


def test_total_donation():
    test_donor = Donor('William Gates ')
    assert test_donor.name == 'William Gates '
    test_donor.add_donations(3000)
    test_donor.add_donations(2000)
    assert test_donor.total_donations == 5000

def test_average_donation():
    """test that avarage donation is working correctly"""
    test_donor = Donor('William Gates ')
    assert test_donor.name == 'William Gates '
    test_donor.add_donations(3000)
    test_donor.add_donations(2000)
    assert test_donor.ave_donations == 2500

def test_send_thank_you_letter():    
    donor1 = Donor("David")
    donor1.add_donations(100.00)
    donor_col = DonorCollection()
    letter = donor_col.write_letter(donor1)    
    expected = "Dear David,\nWe greatly appreciate your generous donation of $100.00.\nThank you,\nThe Team"
    assert letter == expected


def test_donors_list():
    """testing the donor list function"""
    donor1 = Donor('Paul Allen')
    donor_col = DonorCollection()
    donor_col.add_donor(donor1)
    donor2 = Donor('Jeff Bezos')    
    donor_col.add_donor(donor2)
    test_list = donor_col.donor_list()
    assert 'Paul Allen' in test_list
    assert 'Jeff Bezos' in test_list

def test_add_new_donor():
    """test that a donor is created"""
    test_donor = DonorCollection()
    test_donor.add_donor('David')
    assert 'David' in test_donor.donors_dict
    assert test_donor.donors_dict['David'].donation == []


def test_save_letters_disk():
    """check if file is exist"""
    donor1 = Donor('Paul Allen')
    donor2 = Donor('David')
    donor_col = DonorCollection()
    donor_col.save_letters_to_disk()
    donor_col.save_letters_to_disk()
    assert os.path.isfile('Paul_Allen.txt')
    assert os.path.isfile('David.txt')


def test_donor_report():
    """testing the donor report function"""
    test_donor = DonorCollection()
    test_donor.add_donor('Jeff Bezos').add_donations(100.00)
    test_donor.add_donor('David').add_donations(500.50)
    test_donor.add_donor('Allen').add_donations(2500.00)
    report = test_donor.donor_report()
    assert 'Allen' in report
    assert '500.50' in report


  

     
