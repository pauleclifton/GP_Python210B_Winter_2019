#!/usr/bin/env python3

from pathlib import Path
from write_a_letter import write_a_letter

"""
Framework for individual donors.
"""


# Jeff Shabani
# March 1st, 2019
# Python 210, Session 9
# donors.py

class Donor():
    donors = {}
    donations = list()

    def __init__(self, name=''):
        self.name = name
        self.donation = []

    def add_donor(self, answer, amount):
        """
        Adds a donor to the donors list
        :param answer: name
        :param amount: amount to donate
        :return: updated donors dictionary
        """
        self.donations.append(amount)
        self.donors[answer] = self.donations

    def write_a_single_letter(self, answer, amount):
        """
        writes and saves a single letter as a txt file
        :param answer: the donor name entered
        :param amount: the amount to be entered
        :return: text file and path object
        """
        with open(f'{answer}.txt', 'wt') as letter:
            letter.write(write_a_letter(answer, amount))
        letter_path = f'{Path.cwd()}//{answer}.txt'
        return Path(letter_path).exists()

    def view_donor_names(self):
        [print(name) for name in self.donors]

