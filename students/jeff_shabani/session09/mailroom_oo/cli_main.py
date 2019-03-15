#!/usr/bin/env python3

# Jeff Shabani
# March 2019
# Python 210, Session 9
# cli_main.py

import os
import sys
from students.jeff_shabani.session09.mailroom_oo.donor_models import *

"""
Contains mailroom user interaction functions
"""


class CommandLineInterface(DonorCollection, Donor):
    def __init__(self, donors):
        self.donors = donors
        super().__init__(donors)

    def get_value(self, text, check_type):
        """
        Catch non-numeric entries for donation amount.
        """
        while True:
            try:
                value = check_type(input(text))
                return value
            except ValueError:
                print("Invalid value.  Please try again")
                continue

    def set_letter_directory_path_path(self):
        """
        Check if user-entered directory exists and offer them the
        choice to create it if not. Default is current working
        directory
        """
        location = input(f'Please enter the full path of the directory\n'
                         f'where you want to save your letters.\n'
                         f'Hit <Enter> to save to the current working directory.')

        if not location:
            location = os.getcwd()
        else:
            location = Path(f'{location}')
            if not location.exists():
                create_directory_answer = input('Path does\'t exist. Do you want to create it?')
                # accept any version of yes, yep, etc.
                if create_directory_answer.lower() == 'yes':
                    location.mkdir()
                    location = os.chdir(location)
                else:
                    location = os.getcwd()
            else:
                location = os.chdir(location)
        return location

    def add_donations_and_send_thank_you(self):
        while True:

            answer = input('Please enter a donor Full Name.')

            if answer.lower() == 'list':
                DonorCollection.view_donor_names(self)
                continue

            amount = CommandLineInterface.get_value(self, 'How much would this donor like to donate?', int)

            CommandLineInterface.set_letter_directory_path_path(self)

            if answer not in self.donors:
                DonorCollection.add_donor(self, answer, amount)
                Donor.write_a_single_letter(self, answer, amount)
            else:
                DonorCollection.add_donor(self, answer, amount)
                Donor.write_a_single_letter(self, answer, amount)

            print(f'\nThank you {answer.split()[0]} for you generous donation of ${amount:,.0f}\n')
            break

    @classmethod
    def quit_the_program(cls):
        print('Tschüss')
        sys.exit()

    def dictionary_switch(self, response):
        """
        Create the switch dictionary. Tried a defaultdict here
        but it doesn't seem to work as a switch.
        """
        functions = {'1': self.add_donations_and_send_thank_you,
                     '2': self.create_report,
                     '3': self.write_letters_to_all_donors,
                     '4': self.quit_the_program}
        try:
            return functions[response]()
        except KeyError:
            print('Please make a valid selection', '\n')

    def main(self):
        while True:
            response = input(self.prompt)
            self.dictionary_switch(response)

    prompt = "\n".join(("Welcome to my charity!",
                        "Please select and option below:",
                        "1 - Send a Thank You to an individual",
                        "2 - Create a Report",
                        "3 - Send letters to all donors",
                        "4 - Quit",
                        ">>> "))


if __name__ == '__main__':

    # this stuff was used for quick tests
    donors_test = {'Karsten Willems': [120, 130, 50],
                   'Sammy Maudlin': [500, 125, 670, 1000]
                   }

    run = CommandLineInterface(donors_test)
    run.main()
