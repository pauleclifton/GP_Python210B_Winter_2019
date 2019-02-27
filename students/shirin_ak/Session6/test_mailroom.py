
import os
import pytest
from mailroom_4 import create_report, send_thank_you_letter
from mailroom_4 import save_letter_disk, file_name, donor_list, get_donation

def test_send_thank_you_letter():    
    expected = "David,Thank you for your most recent donation of $2500.17."
    assert send_thank_you_letter("David", 2500.17) == expected


def test_create_report():
    """testing report function"""
    report = create_report() 
    assert 'David' in report
    assert '2500.17' in report


def test_file_name():
    """ testing file is created"""
    expected = 'william_gates.txt' 
    assert file_name('william gates') == expected


def test_donor_list():
    donors = donor_list()
    assert 'william gates' in donors
    assert 'Allen' in donors

    
def test_save_letter_disk():
    """check if some of the files exist and that they are not empty"""
    assert os.path.isfile('william_gates.txt')
    assert os.path.isfile('Allen.txt')
    with open('william_gates.txt') as f:
        size = len(f.read())
    assert size > 0
    with open('Allen.txt') as f1:
        size1 = len(f1.read())
    assert size1 > 0

    
def test_get_donation(monkeypatch):
    """testing the donation amount"""
    monkeypatch.setattr('builtins.input', lambda x: 2150.50)
    donation = input("What is your amount?")
    assert donation == 2150.50


def test_valid_input(monkeypatch, capsys):
    "testing valid input"   
    def mock_input(prompt):        
        print(prompt)
        return "list"
    monkeypatch.setattr('builtins.input', mock_input)
    name = input("List of donors")
    captured = capsys.readouterr()    
    assert name == "list"
    assert "List of donors" in captured.out

print("passed")
