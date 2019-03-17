#!/usr/bin/env python3

# Jeff Shabani
# March 2019
# Python 210, Session 9
# donor_models.py

from collections import OrderedDict
from operator import itemgetter
from pathlib import Path

"""
Framework accessing multiple donor classes.
"""


class Donor:

    def __init__(self, donors):
        self.donors = donors
    @classmethod
    def write_a_letter(cls, name, amount):
        return f'Dear {name},\n\nThank you for your kind donation of ${amount:,.0f}\n\n' \
            f'Rest assured that these funds will be put to optimal use.\n\n' \
            f'Best regards,\n' \
            f'The Charitable Charities Team'


    def write_a_single_letter(self, answer, amount):
        """
        writes and saves a single letter as a txt file
        :param answer: the donor name entered
        :param amount: the amount to be entered
        :return: text file and path object
        """
        with open(f'{answer}.txt', 'wt') as letter:
            letter.write(self.write_a_letter(answer, amount))
        letter_path = f'{Path.cwd()}//{answer}.txt'
        return Path(letter_path).exists()


class DonorCollection(Donor):

    def view_donor_names(self):
        [print(name) for name in self.donors]

    def add_donor(self, answer, amount):
        """
        Adds a donor to the donors list
        :param answer: name
        :param amount: amount to donate
        :return: updated donors dictionary
        """
        self.donors[answer] = [amount]

    def add_donation_to_existing_donor(self, answer, amount):
        """
        Adds a new donation to previous donor's record"""
        self.donors[answer].append(amount)

    def create_new_donors_dict(self):
        """
        dictionay comprehension of donors with sum, len, and average of values.
        """
        new_donors = {k: (sum(v), len(v), (sum(v) / len(v))) for k, v in self.donors.items()}
        return OrderedDict(sorted(new_donors.items(), key=itemgetter(1), reverse=True))

    def write_letters_to_all_donors(self):
        for donor, total in self.create_new_donors_dict().items():
            with open(f'{donor}.txt', 'wt') as letter:
                letter.write(self.write_a_letter(donor, total[0]))

    def create_report(self):
        header = f'{"Name".ljust(20)}{"| Total Donations".rjust(20)}{"| # of Donations".rjust(20)}' \
            f'{"| Average Donation".rjust(20)}'
        print(header)
        print('-' * len(header))

        # get donors and totals from new_donors dictionary
        for k, v in self.create_new_donors_dict().items():
            print(f'{str(k).ljust(20)}{str(v[0]).rjust(20)}{str(v[1]).rjust(20)}{str(v[2]).rjust(20)}')
