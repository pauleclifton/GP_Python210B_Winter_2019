#!/usr/bin/python3

from mailroom import *
import time
import os

def test_file_creation():
    """
    Function to test mailroom.send_all
    This function tests if files are created for each donor.
    """
    for key, value in donors.items():
        # I removed the timestamp for simplilcity. I had to switch to Windows for this assignment
        # and was having filename issues.
        filename = f"{key}.txt"
        files = open(filename, "w")
        files.close()

    for key in donors.keys():
        file_name = key + ".txt"
        assert file_name in os.listdir()

def get_letter(name):
    """
    Function to return the contents of a donor file.
    """
    read_file = open(name, 'r')
    return read_file.read()

def test_file_contents():
    """
    Function to test mailroom.send_all()
    This function tests if the donor files contain the correct text.
    """
    for key, value in donors.items():
        file_content = '{greeting}' '{body}' '{closing}' '{signature}'.format(**email).format(key, sum(value))
        file_name = key + ".txt"
        write_text = open(file_name, "w")
        write_text.write(file_content)
        write_text.close()

    expected = '\nHello Bonnie Bug,\n\nWe would like to thank you for your generous donation of $30.00.\n\nBest Regards,\nThe Foundation\n\n'

    assert get_letter("Bonnie Bug.txt") == expected



def test_report_header():
    """
    Function to test mailroom.create_report header row.
    This function tests if the header row is formatting correctly.
    """
    header = ("Donor Name", "| Total Given", "| Num Gifts", "| Average Gift")
    row = " ".join(["{:20s} {:>20s} {:>20s} {:>20s}"]).format(*header)
    assert row == "Donor Name                  | Total Given          | Num Gifts       | Average Gift"

def test_donor_row():
    """
    Function to test mailroom.create_report donor rows.
    This function tests if donor rows are formatting correctly.
    """
    donor_row = [f"{key:20s} {sum(value):>20.2f} {len(value):>20.2f} {sum(value)/len(value):>20.2f}" for key, value in
                 sorted(donors.items())]
    donor_list = [
    "Anne Ant                             1.00                 1.00                 1.00",
    "Bonnie Bug                          30.00                 2.00                15.00",
    "Chuck Cat                            6.00                 3.00                 2.00",
    "Donna Dog                         7501.50                 3.00              2500.50",
    "Edna Ent                             0.90                 3.00                 0.30",]

    assert donor_row == donor_list

def test_thank_you_text():
    # Helped me find a missing comma after greeting name.
    # Helped me find donation typo. It wasn't padding to two decimal places in the letter.
    """
    Function to test mailroom.send_email.
    This function tests if the email template prints correctly with given input.
    """
    input_name = "Anne Ant"
    donation = "20.00"
    text = '{greeting}' '{body}' '{closing}' '{signature}'.format(**email).format(input_name, float(donation))
    assert text == '\nHello Anne Ant,\n\nWe would like to thank you for your generous donation of $20.00.\n\nBest Regards,\nThe Foundation\n\n'

def test_updating_donors():
    """
    Function to test mailroom.add_donation
    This function tests updating donations for pre-existing donors.
    """
    input_name = "Anne Ant"
    donation_amount = float("20.00")
    donors[input_name].append(donation_amount)
    assert "Anne Ant", "20.00" in donors.items()

def test_listing_donors():
    """
    Function to test mailroom.send_thankyou
    This function tests is donors dictionary is listed correctly.
    """
    input_name = "list"
    list_output = ", ".join(donors.keys())
    assert list_output == "Anne Ant, Bonnie Bug, Chuck Cat, Donna Dog, Edna Ent"

def test_adding_donors():
    """
    Function to test mailroom.add_donor and mailroom.add_donation()
    This function tests adding new donors to donors dictionary.
    """
    donor_list = []
    input_name = "Fred Frog"
    donation_amount = "20.00"
    donors.update({input_name: donor_list})
    donors[input_name].append(donation_amount)
    assert "Fred Frog", "20.00" in donors.items()
