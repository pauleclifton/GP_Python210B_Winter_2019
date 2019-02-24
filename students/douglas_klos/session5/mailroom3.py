#!/usr/bin/env python3
""" Mailroom V4.0, now with more error trapping """

# Douglas Klos
# February 15th, 2019
# Python 210, Session 5, Mailroom v3
# mailroom3.py

import os
import datetime

mailroom_db = {'Douglas': [5000, 2000],
               'Maggie': [2222, 3333, 4444],
               'Light Yagami': [124, 8975],
               'Makise Kurisu': [235987],
               'Youjo Senki': [13498.00, 9876, 1234],
               'Motoko Kusanagi': [57892, 239857, 87265],
               'Jo': [8814, 2320]}

MAIN_PROMPT = ('\nWelcome to the Mail Room\n'
               'Please choose from the following options:\n'
               '1: Send a Thank You\n'
               '2: Write thank you files\n'
               '3: Create a report\n'
               '4: Add or Remove a Donor or Donation\n'
               'p: Print database\n'
               'q: Quit\n'
               '>>> ')

ADD_REMOVE_PROMPT = ('\n1: Add donation\n'
                     '2: Remove donation\n'
                     '3: Add donor\n'
                     '4: Remove donor\n'
                     'p: Print database\n'
                     'q: Return to main menu\n'
                     '>>> ')

THANK_YOU_PROMPT = ('\nPlease enter one of the following:\n'
                    '<Name>: Name of person to send a thank you note to\n'
                    'list: Display donors in the database\n'
                    'q: Return to main menu\n'
                    '>>> ')

THANK_YOU_NOTE = ('\nDear {}:\n'
                  '\tThank you for your very kind donation of ${:,.2f}.\n'
                  '\tIt will be put to very good use.\n'
                  '\t\tSincerely,\n'
                  '\t\t\tThe Team')

THANK_YOU_LETTER = ('Dear {}:\n'
                    '\tThank you for your most recenet donation of ${:,.2f}.\n'
                    '\tYour total generosity towards us is ${:,.2f}.\n'
                    '\tIt will be put to very good use.\n'
                    '\t\tSincerely,\n'
                    '\t\t\tThe Team\n')


def display_database():
    """ Displays all donors and their donations """

    print()

    # for key in mailroom_db:
    #     print(f'{key:>24} : {mailroom_db[key]:}')

    # Assignment asked for a comprehension.  Gregor suggested trying here.
    # The text does state you wouldn't typcially use them for printing.
    # IDK, this feels clunky to me, just mushing two lines of code into one.
    # Though perhaps it's the pythonic way to do things.
    # Included for the sake of completeness.
    [print(f'{key:>24} : {mailroom_db[key]:}') for key in mailroom_db]


def create_report():
    """ Prints a report of donors and their donations """

    print()
    print("Donor Name\t\t| Total Given\t\t| Num Gifts | Average Gift")
    print("-" * 79)

    for key in mailroom_db:
        if mailroom_db[key] == []:
            print(f'{key:24s}\t\t       {len(mailroom_db[key]):10}')
        else:
            print(f'{key:24s} '
                  f'$ {sum(mailroom_db[key]):16,.2f}    '
                  f'{len(mailroom_db[key]):10}    '
                  f'$ {sum(mailroom_db[key])/len(mailroom_db[key]):16,.2f}')


def add_donor(name_input=''):
    """ Adds name_input to the database """

    # Check to see if a name was passed in, if not, read user input
    while name_input in '':
        name_input = input("Please enter new donor's name: ")
        if name_input in mailroom_db.keys():
            print('Already exists')
            name_input = ''
        if name_input.lower() in ('q', 'quit'):
            return

    mailroom_db[name_input] = []


def add_donation():
    """ Add new donations to a current donor """

    display_database()
    while True:
        name = input('\nPlease select a donor to add a donation to: ')
        if name.lower() in ('q', 'quit'):
            return
        if name not in mailroom_db.keys():
            print('Donor not found, please select from list')
        else:
            break

    while True:
        try:
            donation_input = float(input('Please enter a donation: '))
        except ValueError:
            print(f'Donation must be a positive number')
        else:
            if donation_input < 0:
                print('Donation must be a positive number')
            else:
                mailroom_db[name].append(donation_input)
                break


def remove_donor(name_input=''):
    """ Remove donor from the database """

    # Check to see if a name was passed in, if not, read user input
    while name_input in '':
        name_input = input("Please enter donor's name to remove: ")
        if name_input.lower() in ('q', 'quit'):
            return
        if name_input in mailroom_db.keys():
            del mailroom_db[name_input]
        else:
            print(f'Donor {name_input} not found')


def remove_donation():
    """ Remove donation from the database """

    display_database()

    while True:
        name_input = input("Please enter donor's name to remove: ")
        if name_input.lower() in ('q', 'quit'):
            return
        if name_input not in mailroom_db:
            print(f'{name_input} not found in database')
        else:
            break

    while True:
        try:
            donation_input = float(
                             input("Please enter donation amount to remove: "))
        except ValueError:
            print(f'Invalid Entry')
        else:
            for donation in mailroom_db[name_input]:
                if donation_input == donation:
                    mailroom_db[name_input].remove(donation_input)
                    return
            print(f'Donation {donation_input} not {name_input} not found')


def add_remove_menu():
    """ Menu to add/remove donors and donations """

    menu = {'1': add_donation,
            '2': remove_donation,
            '3': add_donor,
            '4': remove_donor,
            'p': display_database}

    selection = input(ADD_REMOVE_PROMPT)

    while selection.lower() not in ('q', 'quit'):

        if selection in menu.keys():
            menu[selection]()
        else:
            print('Invalid Input')

        selection = input(ADD_REMOVE_PROMPT)


def thank_you_menu():
    """ Menu for Thank You options """

    while True:
        name_input = input(THANK_YOU_PROMPT)
        if name_input.lower() in ('q', 'quit'):
            return
        if name_input.lower() in ('l', 'list'):
            display_database()
            continue
        elif name_input in '':
            pass
        if name_input not in mailroom_db.keys():
            add_donor(name_input)
            print(f'\nAdding {name_input} to the database')
        else:
            send_thank_you(name_input)


def send_thank_you(name_input):
    """ Send thank you to donor for selected donation """

    if mailroom_db[name_input] == []:
        print(f'No donation from {name_input}')
        return

    print(f'Donation amounts for {name_input}: {mailroom_db[name_input]}')

    # All this try if else except is for error checking input
    while True:
        try:
            donation_input = float(input('Enter donation: '))
        except ValueError:
            print(f'Invalid Entry\n'
                  f'Donation amounts for {name_input}: '
                  f'{mailroom_db[name_input]}')
        else:
            if donation_input in mailroom_db[name_input]:
                print(THANK_YOU_NOTE.format(name_input, donation_input))
                return
            print(f'Donation from {name_input} '
                  f'in the amount of {donation_input} '
                  f'not found')


def write_thank_you_files():
    """ Write thank you files to ./thank_you_files/donor.txt for each donor """

    # Current datetime to append to filename
    now = datetime.datetime.now()

    # Get path from user for file writing
    path = input('Enter path for thank you files or blank for default: ')

    # If path left blank, set to default
    if path == '':
        path = "./thank_you_notes/"

    # Make sure there's a trailing slash on path
    elif path[-1] != '/':
        path += '/'

    # Create directory and parents if they do not exist
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except PermissionError:
        print(f'Permission denied, {path} is not writeable')
        return

    for donor in mailroom_db:
        filename = path + donor + ' ' + now.strftime("%Y-%m-%d %H:%M") + ".txt"

        # No donations from donor, no thank you note needed
        if mailroom_db[donor] == []:
            continue

        # Open file for writing
        try:
            with open(filename, 'w') as donor_file:
                donor_file.write(
                    THANK_YOU_LETTER.format(
                        donor,
                        mailroom_db[donor][len(mailroom_db[donor])-1],
                        sum(mailroom_db[donor])))
        except PermissionError:
            print(f'Permission denied, {path} is not writeable')
            return

    print(f'\nDonor letters written to {path}')


def main():
    """ Mailroom main function """

    menu = {'1': thank_you_menu,
            '2': write_thank_you_files,
            '3': create_report,
            '4': add_remove_menu,
            'p': display_database}

    selection = input(MAIN_PROMPT)

    while selection.lower() not in ('q', 'quit'):

        if selection in menu.keys():
            menu[selection]()
        else:
            print('Invalid Input')

        selection = input(MAIN_PROMPT)


if __name__ == '__main__':
    main()
