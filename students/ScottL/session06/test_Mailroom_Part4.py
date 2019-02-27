#!/usr/bin/env python3

import Mailroom_Part4
import pytest
import os


def test_donation_calcs1():
    """Test average donations are calculated correctly."""
    assert Mailroom_Part4.donation_calcs()[0][3] == 30000


def test_donation_calcs2():
    """Test number of donations is calculatd correctly."""
    assert Mailroom_Part4.donation_calcs()[2][2] == 2


def test_donation_calcs3():
    """Test that donor name is stored correctly."""
    assert Mailroom_Part4.donation_calcs()[1][0] == 'Neil Diamond'


def test_donation_calcs4():
    """Test total donations calculates correctly."""
    assert Mailroom_Part4.donation_calcs()[4][1] == 20000


def test_validate_donation_amount_number():
    """Test that a string entry for donation amount is correctly converted to a number"""
    assert Mailroom_Part4.validate_donation_amount('5000') == 5000


def test_validate_donation_amount_exception():
    """Test that a non-number entered as an amount raises an Exception."""
    with pytest.raises(Exception):
        Mailroom_Part4.validate_donation_amount('a')


def test_validate_donation_quit():
    """Test that the function returns 'None' when 'quit' is entered as an amount."""
    assert Mailroom_Part4.validate_donation_amount('quit') is None


def test_validate_name_quit():
    """Test that the function returns 'None' when 'Quit' is entered as a donor name."""
    assert Mailroom_Part4.validate_name_input("Quit") is None


def test_validate_name():
    """Test that the name validation returns back the name."""
    assert Mailroom_Part4.validate_name_input('John Doe') == 'John Doe'


def test_create_file_location():
    """Tests that a blank file name is created in the current working directory."""
    assert Mailroom_Part4.create_file_location('John Doe') in os.listdir(os.curdir)


def test_create_email_text():
    """Tests that a representative row of donor data is correctly formatted into an email."""
    assert Mailroom_Part4.create_email_text(["John Doe", 1000, 1, 1000]) == "" \
           "Dear John Doe,\n\nThank you so much for your very generous donation of " \
           "$1,000.\nWe wouldn't be able to do this without you." \
           "\n\nSincerely,\nFundraising Team"


def test_save_email_text():
    """Tests that sample text is correctly written into a sample file."""
    test_file = "John Doe.txt"
    test_text = "Thank you for the donation."
    Mailroom_Part4.save_email_text(test_file, test_text)
    with open(test_file, "r") as file:
        assert file.read() == test_text


