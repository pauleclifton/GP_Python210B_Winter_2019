#------------------------
#!/usr/bin/env python3
#Session 09 Exercise:Mailroom Object Oriented
#Shirin Akther
#-------------------------


import sys
import math
from donor_models import Donor
from donor_models import DonorCollection

"""This is the command line interface for the mailroom.
   All the input()function calls and print() function will
   include in this class. In other words this class will
   handle each of mode of the program
 """


dc = DonorCollection()

class CommandInterface():
    def main_menu():
        mainmenu = input("""
        What would you like to do?

        (1) - Send a Thank You Letter
        (2) - Build a Report
        (3) - Send letters to all donors
        (4) - Quit
        > """)
        
        return mainmenu.strip()

    
def thank_you_message():

    while True:
        name = input("Enter the donor's name\n"
                     "or Enter 'list' to see list of donor's\n"
                      " (or type 'menu to exit\n"
                     ">>>").strip()
        if name == 'list':
            print_donor_list()

        elif name == 'menu':
            return
        else:
            break

# creates loop for donation amount input

    while True:
        donationinput = input("Enter the amount donated\n "
                              "(or 'menu' to exit)>>").strip()
        if donationinput == 'menu':
            return
        try:
            amount = float(donationinput)           
        except ValueError:
            print("please enter a valid donation amount")

        else:
            break

    donor = dc.search_donor(name)
    if donor is None:
        donor = dc.add_donor(name)

        donor.add_donations(amount)
        dc.write_letter(donor)


def print_donor_list():
    print("\nDonor Names:")
    print("-" *15)
    print(dc.donor_list())


def print_donor_report():
    """display donor report"""
    print(dc.donor_report())

      
def exit_program():
    """quits the program when prompted in the menu"""
    print("Bye!")
    sys.exit(0)

    
def runmain():
    """ Updated menu function using dictionary and Error handling """
    selection_dict = {"1":thank_you_message,
                     "2": print_donor_report,
                     "3": dc.save_letters_to_disk,
                     "4": exit_program
                      }

    while True:
        selection = CommandInterface.main_menu()
        try:
            selection_dict[selection]()
        except KeyError:
            print("error: menu selection is invalid!")


if __name__ == "__main__":
    runmain()
    
        
