'''
##########################
#Python 210
#Session 06 - Mailroom Part 4
#Elaine Xu
#Feb 24, 2019
###########################
'''
import sys
import datetime
import operator

def send_a_thankyou():
    '''send a thankyou note to donor'''
    while True:
        # prompt for a full name
        fullname = input("Enter full name of the donor (type 'list' to show all donor names): ")
        if fullname.lower() == 'list':
            for donor in donor_db:
                print(donor)
        else:
            while True:
                try:
                    donation_amount = float(input("Enter the donation amount: "))
                    break
                except ValueError:
                    print("Donation amount has to be a number, try again.")
            send_a_thankyou_text(fullname, donation_amount, donor_db)
            print(f"${donation_amount} has been added to {fullname}'s donation history.")
            break
    #send thankyou note
    print("Composing Thank You email:")
    print(f'Thank you {fullname} for your generous donation of ${donation_amount:^10.2f}!')
    print()

def send_a_thankyou_text(fullname, donation_amount, donor_dict):
    '''send a thankyou note to donor'''
    # creating a list of donors - lower case
    donor_list = [donor.lower() for donor in donor_dict]
    if fullname.lower() not in donor_list:
        print(f'{fullname} does not exist in current donor data, '
              f'adding {fullname} to the donor data.')
        donor_dict[fullname] = [donation_amount, 1]
    elif fullname.lower() in donor_list:
        donor_dict[fullname][0] = donor_dict[fullname][0] + donation_amount
        donor_dict[fullname][1] = donor_dict[fullname][1] + 1
    return fullname, donor_dict[fullname]

def create_a_report():
    '''create a report in tabular and return to original prompt'''
    sorted_donor_db = sorted(donor_db.items(), key=operator.itemgetter(1), reverse=True)
    print("Printing report:")
    title = ('Donor Name', 'Total Given', "Num Gifts", 'Average Gift')
    print("{:<24} | {:^13} | {:^11} | {:^11}".format(*title))
    print("-"*70)
    for key, val in sorted_donor_db:
        print(create_a_report_text(key, val))
    print()

def create_a_report_text(key, val):
    '''create a report in tabular and return to original prompt'''
    return "{:<25} ${:>13.2f} {:>13}  ${:>12.2f}".format(key, val[0], val[1], val[0]/val[1])

def sort_total_donation(number):
    '''sort donors by total historical donation amount'''
    return number[1][0]

def send_letters_to_all_donors():
    '''generate thankyou letter to all donors'''
    for key in donor_db:
        with open(key+"_"+str(datetime.date.today())+".txt", 'w') as f:
            f.write(send_letters_to_all_donors_text(key, donor_db))
    print("Thank you letters to all donors have been generated in the local disk.\n")

def send_letters_to_all_donors_text(key, donor_dict):
    '''generate thankyou letter to all donors'''
    return ("Dear {name},\n"
            "\n"
            "        Thank you for your very kind donation of ${amount:10.2f}.\n"
            "\n"
            "        It will be put to very good use.\n"
            "\n"
            "                       Sincerely\n"
            "                          -The Team".format(name=key, amount=donor_dict[key][0]))

def exit_program():
    '''exit program'''
    print("Exiting the program")
    sys.exit()

def main():
    '''main operation of the program'''
    choice = ''
    while True:
        try:
            choice = int(input(PROMPT))
            if choice in DIC_MENU:
                DIC_MENU[choice]()
            else:
                print("Not a valid option, try again.\n")
        except ValueError:
            print("Selection has to be a number, try again.\n")

DIC_MENU = {1: send_a_thankyou,
            2: create_a_report,
            3: send_letters_to_all_donors,
            4: exit_program
            }

PROMPT = ('Menu\n'
          'Please choose from below options:\n'
          '1 - Send a Thank You\n'
          '2 - Create a Report\n'
          '3 - Send letters to all donors\n'
          '4 - Quit\n'
          'Enter your selection: ')

#############################################################
if __name__ == "__main__":

    donor_db = {"William Gates, III": [653772.32, 2],
                "Jeff Bezos": [877.33, 1],
                "Paul Allen": [663.23, 3],
                "Mark Zuckerberg": [1663.23, 3],
                "Bob Smith": [500.00, 1],
                }

    main()
