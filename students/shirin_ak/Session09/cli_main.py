
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
    PROMPT = "\n".join(("Please select a menu option below:",
                    "1 - Send a Thank You to an individual",
                    "2 - Create a Report",
                    "3 - Send letters to all donors",
                    "4 - Quit",
                    ">>> "))



    def thank_you_message():
         while True:                         
             name = input("Enter 'name' to add new donor\n"
                         " or Enter 'list' to see list of donors\n"
                         " (or type 'menu to exit)>>").strip()             

             if name == 'list':                
                print(print_donor_list())
             elif name == 'menu':
                 return
             else:

                break

         while True:
             donation_input = input("Enter the amount donated "
                              "(or 'menu' to exit)>").strip()
             if donation_input == 'menu':

                 return
             try:
               amount = float(donation_input)
               return donation_input
             except ValueError:
               print("please enter a valid donation amount")

             else:
                 break
         # If this is a new user, ensure that the database has the necessary
         # data structure.                   
         donor = dc.find_donor(name)
         if donor is None:
             donor = dc.add_donor(name)
         #record the donation    
             donor.add_donation(amount)
             print(dc.write_letter(donor))


def print_donor_report():
       print(dc.donor_report())

def print_donor_list():
    print("\nDonor Names:")
    print("-" *15)
    print(dc.donor_list())       

       
def exit_program():
    print("Bye!")
    sys.exit(0)

    
def runmain():
    
    selection_dict = {"1": CommandInterface.thank_you_message,
                     "2": print_donor_report,
                     "3": dc.save_letters_to_disk,
                     "4": exit_program
                      }

    while True:
        selection = input(CommandInterface.PROMPT)
        try:
            selection_dict[selection]()
        except KeyError:
            print("error: menu selection is invalid!")


if __name__ == "__main__":

    runmain()

    
        
