#!/usr/bin/env python3

import sys

global_donation_list = {"Tom Petty": [5000, 15000],
                        "Neil Diamond": [20000, 30000],
                        "Elton John": [25000, 25000, 40000],
                        "John Lennon": [25000],
                        "Mick Jagger": [20000, 10000]}
MENU_HEADER_1 = "\nMenu Options:"
MENU_HEADER_2 = "\n" + "-" * len(MENU_HEADER_1)
MENU_SELECTIONS = {1: "Send a 'Thank You' note to individual donor",
                   2: "Display a report",
                   3: "Send 'Thank You' letters to all donors",
                   4: "Quit"}
REPORT_HEADER_1 = "\n{:<26}{:<12}{:^17}{:>11}".format(
                    "Donor Name", "Total Dollars", "Number", "Avg Amount")
REPORT_HEADER_2 = "\n" + "-" * len(REPORT_HEADER_1)
DONOR_LIST_HEADER = "\nDonor Name:\n" + "-" * 20


def display_user_menu():
    """Display the contents of the menu options for the user."""
    print(MENU_HEADER_1, MENU_HEADER_2)
    [print(item, ": ", MENU_SELECTIONS[item]) for item in MENU_SELECTIONS]


def donation_calcs_error(name):
    """"""
    error_message = "Error: A value other than a number is listed as a " \
                    "donation 'amount' for '{}'.".format(name)
    print(error_message)


def donation_calcs():
    """
    Calculate the number of donations, and the total and average amounts.
    :return: Return a list of donors with their total donations in descending order.
    """
    sorted_donation_list = []
    for item in global_donation_list:
        try:
            total_donation = round(sum(global_donation_list[item]))
        except TypeError:
            donation_calcs_error(item)
        else:
            number_of_donations = len(global_donation_list[item])
            try:
                sorted_donation_list.append([item, total_donation, number_of_donations,
                                            round(total_donation / number_of_donations)])
            except ZeroDivisionError:
                sorted_donation_list.append([item, total_donation, number_of_donations, 0])
    sorted_donation_list.sort(key=lambda x: x[1], reverse=True)
    return sorted_donation_list


def display_donor_names():
    """Print the list of full donor names for the user."""
    print("\n", DONOR_LIST_HEADER)
    [print(entry) for entry in global_donation_list]


def draft_email(name, amount):
    """
    Display text reminiscent of an email thanking a donor.
    :param name: donor name
    :param amount: amount of donation
    """
    print("\nDear {},\nThanks for the generous donation of ${:,.2f}."
          "\n\nSincerely,\nFundraising Team".format(name, amount))


def get_donation_amount():
    """
    Receive input from user on the amount of the donation
    :return: a string containing either the amount or 'quit' to be further processed
    """
    input_prompt = "Please enter the donation amount (or enter 'Quit' to return to Main Menu): "
    return input(input_prompt).strip('$')


def validate_donation_amount(donation_amount):
    """
    Receive input from user on amount of donation. Process accordingly.
    :param donation_amount: amount of donation input from user
    """
    value_error_message = "The entry for 'amount' count was not a valid number. Please try again."
    if donation_amount.strip().lower() != "quit":
        try:
            donation_amount = float(donation_amount)
        except ValueError:
            print(value_error_message)
            get_donation_amount()
        else:
            return donation_amount


def get_donor_name():
    """
    Receive input from user on the name of the donor.
    :return: a string containing the response to the input prompt to be further processed
    """
    input_prompt = "\nPlease enter the full name of the donor, " \
                   "'List' to see a list of existing donors, " \
                   "or 'Quit' to return to the Main Menu: "
    return input(input_prompt)


def validate_name_input(donor_name):
    """
    Process user input accordingly for optional inputs of 'quit' and 'list'.
    :param donor_name: the name of the donor input from the user
    :return: the name of the donor to be further processed
    """
    if donor_name.strip().lower() != "quit":
        if donor_name.strip().lower() == "list":
            display_donor_names()
            process_new_donation()
        else:
            return donor_name


def add_donation_to_list(name, amount):
    """
    Input the validated donor name and amount to the donation list.
    :param name: name of donor
    :param amount: amount of donation
    """
    if name in global_donation_list:
        global_donation_list[name].append(float(amount))
    else:
        global_donation_list[name] = [float(amount)]


def process_new_donation():
    """Call other functions to add new donations to the master list."""
    donor_name = validate_name_input(get_donor_name())
    if donor_name is not None:
        donation_amount = validate_donation_amount(get_donation_amount())
        if donation_amount is not None:
            add_donation_to_list(donor_name, donation_amount)
            draft_email(donor_name.title(), float(donation_amount))


def display_report():
    """Call the function to calculate total & avg donations and then display a report."""
    print(REPORT_HEADER_1, REPORT_HEADER_2)
    for item in donation_calcs():
        print("{:<26}${:>12,}{:^17}${:>11,}".format(item[0], item[1], item[2], item[3]))


def create_file_location(donor_name):
    """
    Create a file in the current working directory named {donor's name}.txt.
    :param donor_name: the full name of the donor
    :return: a string containing the donor's name
    """
    with open("{}.txt".format(donor_name), "w") as file:
        file.close()
    return "{}.txt".format(donor_name)


def create_email_text(donor):
    """
    Format the text for the email for an individual donor.
    :param donor: a list containing name, total donations, number, and avg. amount
    :return: the formatted string to be saved in the file
    """
    if donor[2] > 1:
        plurality = "s totaling"
    else:
        plurality = " of"
    return "Dear {},\n\nThank you so much for your very generous donation{} " \
           "${:,}.\nWe wouldn't be able to do this without you." \
           "\n\nSincerely,\nFundraising Team" \
           "".format(donor[0], plurality, donor[1])


def save_email_text(file_location, text):
    """
    Open the .txt file for the corresponding donor and add the text.
    :param file_location: string containing the donor's name and .txt
    :param text: The body of the 'email' that will be saved in the file
    """
    with open(file_location, "w") as file:
        file.write(text)


def process_email_creation():
    """Organize the flow of functions to execute 'sending emails', aka saving .txt files"""
    for donor in donation_calcs():
        file_name = create_file_location(donor[0])
        email_text = create_email_text(donor)
        save_email_text(file_name, email_text)


def main_menu():
    """Loop through the main menu to receive and process user input."""
    menu_switch = {1: process_new_donation,
                   2: display_report,
                   3: process_email_creation,
                   4: sys.exit}
    input_prompt = "\nSelect a number from the menu options (1-4): "
    value_error_message = "An invalid input was entered; " \
                          "please enter a valid number from the menu."
    while True:
        display_user_menu()
        try:
            menu_selection = int(input(input_prompt))
        except ValueError:
            print(value_error_message)
        else:
            menu_switch[menu_selection]()


if __name__ == "__main__":
    main_menu()
