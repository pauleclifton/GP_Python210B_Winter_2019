#!/usr/bin/env python3

import sys
from students.jeff_shabani.session09.donor_models import *

"""
Contains mailroom user interaction functions
"""

# Jeff Shabani
# March 1st, 2019
# Python 210, Session 9
# donors.py

donors = {'William B': [120, 130, 50],
          'Sammy Maudlin': [500, 125, 670, 1000],
          'Bobby Bittman': [10],
          'Skip Bittman': [75, 125, 19],
          'Ashley Lashbrooke': [10000, 15000]}


prompt = input("\n".join(("Welcome to my charity!",
                        "Please select and option below:",
                        "1 - Send a Thank You to an individual",
                        "2 - Create a Report",
                        "3 - Send letters to all donors",
                        "4 - Quit",
                        ">>> ")))

class CommandLineInterface(Donor, DonorCollection):
    def __init__(self):
        if prompt == '4':
            print('Tschüss')
            sys.exit()
        else:
            print('nicht vier')
        super().__init__()



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

    def add_donations_and_send_thank_you(self):
        while True:

            answer = input('Please enter a donor Full Name.')

            if answer.lower() == 'list':
                Donor.view_donor_names()
                continue

            amount = get_value('How much would this donor like to donate?', int)

            set_letter_directory_path_path()

            if answer not in donors:
                add_donor(answer, amount)
                write_a_single_letter(answer, amount)
            else:
                add_donor(answer, amount)
                write_a_single_letter(answer, amount)

            print(f'\nThank you {answer.split()[0]} for you generous donation of ${amount:,.0f}\n')
            break



c=CommandLineInterface()




