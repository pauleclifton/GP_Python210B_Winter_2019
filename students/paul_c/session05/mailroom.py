#!/usr/local/bin/python3

import sys
import time

donors = {
    "Anne Ant": [1.00],
    "Bonnie Bug": [20.00, 10.00],
    "Chuck Cat": [2.00, 2.00, 2.00],
    "Donna Dog": [5000.00, 2500.00, 1.50],
    "Edna Ent": [.30, .50, .10]
}

email = {
    "greeting": "\nHello {}\n\n",
    "body": "We would like to thank you for your generous donation of ${}.\n\n",
    "closing": "Best Regards,\n",
    "signature": "The Foundation\n\n"
}


def send_all():
    """
    Function to send a thank you letter to all donors.
    This function sums total donations and writes letters to timestamped files.
    """
    for key, value in donors.items():
        timestamp = time.strftime("%b %d %Y %H:%M:%S")
        filename = f"{timestamp}-{key}.txt"
        file_content = '{greeting}' '{body}' '{closing}' '{signature}'.format(**email).format(key, sum(value))
        files = open(filename, "w")
        files.write(file_content)
        files.close()
        print(str(files) + "  ---File created.\n")


def create_report():
    """
    This function prints out a report with the following parameters:
    Donor Name, Total Given, Number of Gifts, Average Gift Amount
    """
    header = ("Donor Name", "| Total Given", "| Num Gifts", "| Average Gift")
    row = " ".join(["{:20s} {:>20s} {:>20s} {:>20s}"]).format(*header)
    header_length = len(row)
    print("\n" + row)
    print("=" * header_length)
    donor_row = [f"{key:20s} {sum(value):>20.2f} {len(value):>20.2f} {sum(value)/len(value):>20.2f}" for key, value in
                 sorted(donors.items())]
    for donor in donor_row:
        print(donor)
    print("\n")


def send_email(input_name, donation):
    """
    Function to send automated "Thank you" email to donor.
    :param input_name: User provided full name of donor.
    :param donation: Donation amount in dollars.

    This function uses a dictionary as a template for the letter.
    """
    print('{greeting}' '{body}' '{closing}' '{signature}'.format(**email).format(input_name, donation))


def list_donors():
    # Provides a list of donor names when "list" is chosen in send_thankyou().
    print("\nDonor List:")
    print(", ".join(donors.keys()))
    print("\n")


def add_donation(input_name):
    """
    Function to add new donations to accounts.
    :param input_name: User provided full name of donor.
    """
    while True:
        try:
            # If the user's input cannot be converted to a float,
            # an exception is raised and they are asked to try again.
            donation_amount = float(input("Please enter " + input_name + "'s donation as an integer or float:  "))
        except ValueError:
            print("\nInput not recognized. Please try again...\n")
            continue
        else:
            donors[input_name].append(donation_amount)
            print(str(donation_amount) + " added to " + input_name)
            send_email(input_name, str(donation_amount))
        break


def add_donor(input_name):
    """
    Function to add new donors if they are not in the donors dictionary.
    :param input_name: User provided full name of donor
    """
    # Adds new donors if their name is not found in the donors dictionary.
    donor_list = []
    donors.update({input_name: donor_list})
    print(input_name + " has been added to the list.")
    add_donation(input_name)


def send_thankyou():
    """
    Function to provide user options for "Send thank you prompt".
    This function does not use a try block because any unknown input is to be handled as a new donor name.
    """
    while True:
        input_name = input("\nPlease provide the full name of the donor. Use or use 'list' to see a list of donors, "
                           "or use q to return to main menu.\nEnter full name here:  ")
        if input_name == "q":
            break
        elif input_name in donors.keys():
            add_donation(input_name)
            break
        elif input_name == 'list':
            list_donors()
        elif input_name not in donors.keys():
            add_donor(input_name)
            break


def exit_system():
    print("\nExiting program...\n")
    sys.exit()


def main():
    """
    Function to provide a main menu. A dictionary is used as a dispatch table for the rest of the program.
    """
    main_menu = {
        "1": send_thankyou,
        "2": create_report,
        "3": send_all,
        "4": exit_system,
    }
    while True:
        try:
            # If the user does not choose an available option,
            # an exception is raised and the user is asked to try again.
            user_input = input("Choose the number of the operation you wish to perform:"
                               "\n(1) Send a Thank You to a single donor.\n(2) Create a Report.\n"
                               "(3) Send letters to all donors.\n(4) Quit\nEnter here: ")
            main_menu.get(user_input)()
        except TypeError:
            print("\nOption not recognized. Please try again...\n")
            continue


if __name__ == '__main__':
    main()
