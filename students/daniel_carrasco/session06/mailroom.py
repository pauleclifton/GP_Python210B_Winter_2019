#!/usr/bin/env python3
from datetime import date
import os
import sys
import pytest

donors = {
    'art bart': [1000, 1], 'harry scary': [50, 5], 'hay boo': [50000, 3]
}
for keys in donors:
    donors[keys.title()] = donors.pop(keys)
today = str(date.today())
path = os.getcwd()


def main():
    while True:

        VALID_RESPONSES = (1, 2, 3, 4, 5)
        try:
            user_choice = int(input('\nChoose an action(1 - 4):\n\n\
                    1 - Send a Thank You to a single donor.\n\
                    2 - Create a Report.\n\
                    3 - Send letters to all donors.\n\
                    4 - Add new donor.\n\
                    5 - Add new donation.\n\
                    6 - Quit\n'))
            arg_dict = {
                1: thankyou,
                2: report,
                3: letter,
                4: addnewdonor,
                5: addnewdonation,
                6: quit}
            if arg_dict[user_choice] == 'quit':
                sys.exit()
            else:
                arg_dict[user_choice]()
        except ValueError:
            print("Input must be an integer, try again.")
        except KeyError:
            print('Choice must be a menu input (1-4)')
        continue


def thankyou():
    while True:
        try:
            choice = int(input('\nChoose an action(1-3):\n\
                    1 - See Donor List.\n\
                    2 - Enter Name.\n\
                    3 - Enter New Name.\n\
                    4 - Quit submenu\n'))
            if choice == 1:
                [print(keys.title()) for keys in donors]
            if choice == 2:
                existing_name = input('Enter full name\n').title()
                value = donors[existing_name]
                [print(row) for row in write_letter(existing_name, value)]
            if choice == 3:
                addnewdonor()

            if choice == 4:
                main()
        except ValueError:
            print("Input must be an integer, try again.")
            continue


def report():
    for row in get_report():
        print(row)


def get_report():
    report_list = []
    row_format = "{:>15}" * 4
    report_list.append(
        row_format.format(
            'Name',
            'Donation ($)',
            'Amount',
            'Average ($)'))
    for key, value in donors.items():
        report_list.append(
            f'{key.title():>15}{value[0]:>15.2f}{value[1]:>15}{value[0]/value[1]:>15.2f}')
    return report_list


def letter():
    for key, value in donors.items():
        filename = open(key.title() + "_" + today + '.txt', 'w+')
        for row in write_letter(key, value):
            filename.write(row)
        filename.close()
        name_of_file = (key, today)


def write_letter(key, value=' '):
    written_letter = [
        f'\tDear {key.title()}\n',
        f'Thank you for your very kind donation of ${value[0]}.\n',
        'It will be put to very good use.\n',
        '\tSincerely\n',
        '\t\t-The Team']
    return written_letter


def name_of_file(key, today=str(date.today())):
    return key.title() + "_" + today + '.txt'


def addnewdonor(user_input_name=' '):
    if user_input_name == ' ':
        user_choice_name = input("Enter name of new Donor\n")
        user_choice_donation = float(input("Enter Donation Amount\n"))
    else:
        user_choice_name = user_input_name
        user_choice_donation = float(input("Enter Donation Amount\n"))
    while True:
        user_confirm = input(
            f'Add {user_choice_name:10} with a donation of ${user_choice_donation:10.2f}?\n\n Enter (Y/N)\n')
        try:
            print(user_confirm)
            if user_confirm.upper() == 'Y':
                donors[user_choice_name] = [user_choice_donation, 1]
                break
            else:
                user_choice_name = input("Enter name of new Donor\n")
                user_choice_donation = float(
                    input("Enter Donation Amount\n"))
        except ValueError:
            print("Input must be an integer, try again.")
    return user_choice_name, user_choice_donation


def addnewdonation():
    report()
    user_input_name = input(
        "\nEnter the name of donor adding a new donation.\nSee report for list of current donors\n\n")
    while True:
        keys = [key for key in donors]
        if user_input_name.title() in keys:
            try:
                user_choice_donation
            except NameError:
                user_choice_donation = float(input("Enter Donation Amount\n"))
                donors[user_input_name.title()][0] = donors[user_input_name.title()
                                                            ][0] + user_choice_donation
                donors[user_input_name.title(
                )][1] = donors[user_input_name.title()][1] + 1
            break
        else:
            user_input_name, user_choice_donation = addnewdonor(
                user_input_name)


if __name__ == '__main__':

    main()
