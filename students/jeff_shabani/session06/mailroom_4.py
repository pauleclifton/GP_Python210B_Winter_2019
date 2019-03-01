#!/usr/bin/env python3
import os
import sys

from collections import OrderedDict
from operator import itemgetter
from pathlib import Path


donors = {'William B': [120, 130, 50],
          'Sammy Maudlin': [500, 125, 670, 1000],
          'Bobby Bittman': [10],
          'Skip Bittman': [75, 125, 19],
          'Ashley Lashbrooke': [10000, 15000]}

prompt = "\n".join(("Welcome to my charity!",
                    "Please select and option below:",
                    "1 - Send a Thank You to an individual",
                    "2 - Create a Report",
                    "3 - Send letters to all donors",
                    "4 - Quit",
                    ">>> "))


def get_value(text, check_type):
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

def get_input(text):
    return input(text)

def get_value_test(text, check_type):
    def get_value_test(text, check_type):
        """
        Catch non-numeric entries for donation amount.
        """
        text = get_input('Please enter a value')
        try:
            value = check_type(text)
            return True
        except ValueError:
            return False


def view_donor_names():
    [print(name) for name in donors]


def write_a_letter(name, amount):
    return f'Dear {name},\n\nThank you for your kind donation of ${amount:,.0f}\n\n' \
        f'Rest assured that these funds will be put to optimal use.\n\n' \
        f'Best regards,\n' \
        f'The Charitable Charities Team'



def set_letter_directory_path_path():
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


def add_donor(answer, amount):
    """
    adds a new donor to the donor list
    :param answer: the donor name entened
    :param amount: the amount to be donated
    :return: length of donor list post-change
    """
    donors[answer] = [amount]
    return len(donors)

def write_a_single_letter(answer, amount):
    """
    writes and saves a single letter as a txt file
    :param answer: the donor name entered
    :param amount: the amount to be entered
    :return: text file and path object
    """
    with open(f'{answer}.txt', 'wt') as letter:
        letter.write(write_a_letter(answer, amount))
    letter_path = f'{Path.cwd()}//{answer}.txt'
    return Path(letter_path).exists()


def add_donations_and_send_thank_you():
    while True:

        answer = input('Please enter a donor Full Name.')

        if answer.lower() == 'list':
            view_donor_names()
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


def create_new_donors_dict():
    """
    dictionay comprehension of donors with sum, len, and average of values.
    """
    new_donors = {k: (sum(v), len(v), (len(v) / len(v))) for k, v in donors.items()}
    return OrderedDict(sorted(new_donors.items(), key=itemgetter(1), reverse=True))
    # return new_donors


def write_letters_to_all_donors():
    set_letter_directory_path_path()
    for donor, total in create_new_donors_dict().items():
        with open(f'{donor}.txt', 'wt') as letter:
            letter.write(write_a_letter(donor, total[0]))


def create_report():
    header = f'{"Name".ljust(20)}{"| Total Donations".rjust(20)}{"| # of Donations".rjust(20)}' \
        f'{"| Average Donation".rjust(20)}'
    print(header)
    print('-' * len(header))

    # get donors and totals from new_donors dictionary
    for k, v in create_new_donors_dict().items():
        print(f'{str(k).ljust(20)}{str(v[0]).rjust(20)}{str(v[1]).rjust(20)}{str(v[2]).rjust(20)}')


def quit_the_program():
    print('Tschüss')
    sys.exit()


def dictionary_switch(selection):
    """
    Create the switch dictionary. Tried a defaultdict here
    but it doesn't seem to work as a switch.
    """
    functions = {'1': add_donations_and_send_thank_you,
                 '2': create_report,
                 '3': write_letters_to_all_donors,
                 '4': quit_the_program}
    try:
        return functions[selection]()
    except KeyError:
        print('Please make a valid selection', '\n')


def main():
    while True:
        response = input(prompt)
        dictionary_switch(response)


if __name__ == '__main__':
    main()
