#!/usr/bin/env python3
#pylint: disable=R1710, C0321, W1113
""" Mailroom OO Donor class """

# Douglas Klos
# March 17th, 2019
# Python 210, Session 9, Mailroom OO
# donor.py


class Donor():
    """
    Donor class

    Attributes:
        name : The name of the donor
        donations : The donations for the donor
    """

    def __init__(self, name='', *args):
        """
        Donor class initializer

        :param name: The name of the donor being created
        :param args: The initial donations for the donor
        """
        self._name = name
        self._donations = [value for value in args]

    def __str__(self):
        return f'{self.name} : {self.donations}'

    def __repr__(self):
        return f'{self.name} : {self.donations}'

    def add_donation(self, donation):
        """
        Adds a new donation to the donor

        :param donation: The new donation to be added
        """
        self._donations.append(donation)

    def remove_donation(self, donation):
        """
        Removes a donation from the donor

        :param donation: The donation to be removed
        """
        if donation in self.donations:
            self._donations.remove(donation)
            return f'Donation {donation} has been removed from {self.name}'
        return f'Donation {donation} not found for {self.name}'

    @property
    def name(self):
        """ Sets or returns the donor's name """
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def donations(self):
        """ Returns the donations list """
        return self._donations

    @property
    def total_donations(self):
        """ Returns the total amount of donations """
        return sum(self.donations)

    @property
    def average_donation(self):
        """ Returns the average amount of donations """
        if self.donations == []:
            return 0
        return sum(self.donations) / len(self.donations)
