'''
##########################
#Python 210
#Session 09 - Mailroom Part 5
#Elaine Xu
#Mar 13, 2019
###########################
'''
import sys
from mailroom5_donor_models import Donor
from mailroom5_donor_models import DonorCollection

#############################################################
if __name__ == "__main__":
    DIC_MENU = ('''
                1: send_a_thankyou,
                2: create_a_report,
                3: exit_program'''
                )

    PROMPT = ('Menu\n'
              'Please choose from below options:\n'
              '1 - Send a Thank You\n'
              '2 - Create a Report\n'
              '3 - Quit\n'
              'Enter your selection: ')

    donor_db = {"William Gates, III": [653772.32, 2],
                "Jeff Bezos": [877.33, 1],
                "Paul Allen": [663.23, 3],
                "Mark Zuckerberg": [1663.23, 3],
                "Bob Smith": [500.00, 1],
                }
    donor_db_lower = [donor.lower() for donor in donor_db]

    for donor in donor_db:
        DonorCollection.add_donor(donor, donor_db[donor])

    while True:
        try:
            choice = int(input(PROMPT))
            if choice == 1:
                while True:
                    fullname = input("Enter full name of the donor (type 'list' to show all "
                                     "donor names): ")
                    if fullname.lower() == 'list':
                        print(DonorCollection.list_all_names())
                    elif fullname.lower() not in donor_db_lower:
                        add_name = str(input(f'"{fullname}" does not exist in current donor data, '
                                             f'adding "{fullname}" to the donor data? (Y/N): '))
                        if add_name.lower() == 'y':
                            while True:
                                try:
                                    donation_amount = float(input("Enter the donation amount: "))
                                    Donor(fullname, [donation_amount, 1])
                                    DonorCollection.add_donor(fullname, [donation_amount, 1])
                                    print(f"${donation_amount} has been added to {fullname}'s "
                                          f"donation history.")
                                    break
                                except ValueError:
                                    print("Donation amount has to be a number, try again.")
                            break

                        elif add_name.lower() == 'n':
                            print("Name is not added, try again.\n")
                        else:
                            print("Not a valid option, try again.\n")
                    else:
                        print(f"'{fullname}' exists in donor database, donation will be added "
                              f"to history.")
                        while True:
                            try:
                                donation_amount = float(input("Enter the donation amount: "))
                                print(DonorCollection.add_donation(fullname, donation_amount))
                                break
                            except ValueError:
                                print("Donation amount has to be a number, try again.")
                        break
                print('\n'+Donor.send_a_thankyou(fullname, donation_amount))

            elif choice == 2:
                print(DonorCollection.create_a_report_header())
                print(DonorCollection.create_a_report())

            elif choice == 3:
                print("Exiting the program")
                sys.exit()

            else:
                print("Not a valid option, try again.\n")

        except ValueError:
            print("Selection has to be a number, try again.\n")
