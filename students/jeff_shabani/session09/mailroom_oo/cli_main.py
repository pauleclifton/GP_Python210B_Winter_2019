#!/usr/bin/env python3

import os
import sys
from students.jeff_shabani.session09.mailroom_oo.donor_models import *

"""
Contains mailroom user interaction functions
"""

# Jeff Shabani
# March , 2019
# Python 210, Session 9
# donors.py




# prompt = input("\n".join(("Welcome to my charity!",
#                           "Please select and option below:",
#                           "1 - Send a Thank You to an individual",
#                           "2 - Create a Report",
#                           "3 - Send letters to all donors",
#                           "4 - Quit",#                           ">>> ")))


class CommandLineInterface(DonorCollection):
    def __init__(self):
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

            if answer not in donors:
                DonorCollection.add_donor(self, answer, amount)
                Donor.write_a_single_letter(self, answer, amount)
            else:
                DonorCollection.add_donor(self, answer, amount)
                Donor.write_a_single_letter(self, answer, amount)

            print(f'\nThank you {answer.split()[0]} for you generous donation of ${amount:,.0f}\n')
            break

    def quit_the_program(self):
        print('Tschüss')
        sys.exit()


if __name__ == '__main__':
    donors = {'William B': [120, 130, 50],
              'Sammy Maudlin': [500, 125, 670, 1000],
              'Bobby Bittman': [10],
              'Skip Bittman': [75, 125, 19],
              'Ashley Lashbrooke': [10000, 15000]}

    c = CommandLineInterface()
    #c.add_donations_and_send_thank_you()
    c.create_report()

    # prompt = input("\n".join(("Welcome to my charity!",
    #                           "Please select and option below:",
    #                           "1 - Send a Thank You to an individual",
    #                           "2 - Create a Report",
    #                           "3 - Send letters to all donors",
    #                           "4 - Quit",
    #                           ">>> ")))
