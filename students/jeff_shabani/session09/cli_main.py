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



c=CommandLineInterface()




