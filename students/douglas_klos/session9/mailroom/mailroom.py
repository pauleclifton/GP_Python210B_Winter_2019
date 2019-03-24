#!/usr/bin/env python3
#pylint: disable=C0103, R1710, C0321
""" Mailroom OO User Interface """

# Douglas Klos
# March 17th, 2019
# Python 210, Session 9, Mailroom OO
# mailroom.py


import os
import argparse
import datetime
from io import StringIO
from donor import Donor
from donordb import DonorDB as DB
import html_render as hr

mailroom = DB()

THANK_YOU_LETTER = ('Dear {}:\n'
                    '\tThank you for your most recenet donation of ${:,.2f}.\n'
                    '\tYour total generosity towards us is ${:,.2f}.\n'
                    '\tIt will be put to very good use.\n'
                    '\t\tSincerely,\n'
                    '\t\t\tThe Team\n')


def initialize_donors():
    """  Initialize the database """
    donor1 = Donor('Douglas', 5000, 2000)
    donor2 = Donor('Maggie', 2222, 3333, 4444)
    donor3 = Donor('Light Yagami', 124, 8975)
    donor4 = Donor('Makise Kurisu', 235987)
    donor5 = Donor('Youjo Senki', 13498.00, 9876, 1234)
    donor6 = Donor('Motoko Kusanagi', 57892, 239857, 87265)
    donor7 = Donor('Jo', 8814, 2320)
    donor8 = Donor('Mark')

    mailroom.add_donor(donor1)
    mailroom.add_donor(donor2)
    mailroom.add_donor(donor3)
    mailroom.add_donor(donor4)
    mailroom.add_donor(donor5)
    mailroom.add_donor(donor6)
    mailroom.add_donor(donor7)
    mailroom.add_donor(donor8)


def get_value(text, check_type, valid_inputs=None):
    """ Gets a value from the user of specified type """

    while True:
        try:
            value = check_type(input(text))
        except ValueError:
            print("Invalid value. Please try again")
            continue
        else:
            if valid_inputs:
                if value not in valid_inputs:
                    print(f"Valid inputs are {valid_inputs}. Please try again")
                    continue
            return value


def display_menu(menu, value_type, prompt):
    """
    Displays a menu and prompts the user for input

    :param menu: Dictionary of functions to select from
    :param value_type: Type of input requested (int, str, etc...)
    :param prompt: Prompt that is displayed to the user
    """
    selection = get_value(prompt, value_type)

    while selection.lower() not in ('q', 'quit'):
        if selection in menu.keys():
            output = menu[selection]()
            if output:
                print(output)
        else:
            print('Invalid Input')
        selection = get_value(prompt, value_type)


def add_remove_menu():
    """ Menu to add/remove donors and donations """

    menu = {'1': add_donor,
            '2': add_donation,
            '3': remove_donor,
            '4': remove_donation,
            '5': rename_donor,
            'p': display_database}

    ADD_REMOVE_PROMPT = ('\n1: Add donor\n'
                         '2: Add donation\n'
                         '3: Remove donor\n'
                         '4: Remove donation\n'
                         '5: Rename donor\n'
                         'p: Print database\n'
                         'q: Return to main menu\n'
                         '>>> ')

    return display_menu(menu, str, ADD_REMOVE_PROMPT)


def add_donor():
    """ Prompts user for name to enter into database """
    display_database()
    name = get_value("Please enter new donor's name: ", str)
    if name.lower() in ('q', 'quit', ''):
        return

    return mailroom.add_donor(name)


def add_donation():
    """ Prompts user for donor name and donation amount to add """
    display_database()
    name = get_value("Please enter name of donor: ", str)
    if name.lower() in ('q', 'quit'):
        return

    donation = get_value("Please enter donation amount: ", float)

    return mailroom.add_donation(name, donation)


def remove_donor():
    """ Prompts user for name to remove from database """
    display_database()
    name = get_value("Please enter name of donor to remove: ", str)
    if name.lower() in ('q', 'quit'):
        return

    return mailroom.remove_donor(name)


def remove_donation():
    """ Prompts user for donation amount and donor to remove """
    display_database()
    name = get_value("Please enter name of donor: ", str)
    if name.lower() in ('q', 'quit'):
        return

    donation = get_value("Please enter donation amount: ", float)

    return mailroom.remove_donation(name, donation)


def rename_donor():
    """ Prompts user for a name and renames donor """
    display_database()
    name = get_value("Please enter name of donor: ", str)
    new_name = get_value("Please enter new name for donor: ", str)

    return mailroom.rename_donor(name, new_name)


def thank_you_menu():
    """ Menu for thank you notes """
    menu = {'1': thank_you_note,
            '2': thank_you_files,
            'p': display_database}

    thank_you_prompt = ('\n1: Send a thank you note to a donor\n'
                        '2: Write thank you files for each donor\n'
                        'p: Display donors in the database\n'
                        'q: Return to main menu\n'
                        '>>> ')

    return display_menu(menu, str, thank_you_prompt)


def thank_you_note():
    """ Send thank you to donor for selected donation """
    display_database()
    name = get_value('Please enter a donors name: ', str)

    try:
        return display_thank_you_note(name)
    except KeyError:
        return f'Donor {name} not found.'


def display_thank_you_note(name):
    """ Displays formatted thank you letter """
    if mailroom.database[name].total_donations > 0:
        return THANK_YOU_LETTER.format(mailroom.database[name].name,
                                       mailroom.database[name].donations[-1],
                                       mailroom.database[name].total_donations)
    return 'No donations found for donor'


def thank_you_files(path=''):
    """ Prompts user for path to write thank you files to, defaults to ./thanks/ """
    if os.name == 'nt':
        raise NotImplementedError

    if path == '':
        path = get_value('Enter path for thank you files or blank for default (./thanks/): ', str)
        if path == '':
            path = './thanks/'

    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except PermissionError:
        return f'Permission denied, {path} is not writeable'

    for name in mailroom.database:
        # No donations from donor, no thank you note needed
        if mailroom.database[name].donations == []:
            continue
        try:
            write_thank_you_letter(path, name)
        except PermissionError:
            return f'Permission denied, {path} is not writeable'

    return f'Thank you files written to {path}'


def write_thank_you_letter(path, name):
    """
    Writes a thank you letter to the specified path

    :param path: Path to write thank you letter to
    """
    now = datetime.datetime.now()
    if path == '': path = './thanks/'
    if path[-1] != '/': path += '/'
    filename = path + name + ' ' + now.strftime("%Y-%m-%d") + ".txt"

    try:
        with open(filename, 'w') as donor_file:
            donor_file.write(THANK_YOU_LETTER.format
                             (mailroom.database[name].name,
                              mailroom.database[name].donations[-1],
                              mailroom.database[name].total_donations))
    except PermissionError:
        raise PermissionError

    return f'Thank you letter for {name} has been written to {filename}'


def display_database():
    """ Displays the database """
    print(mailroom)


def save_load_menu():
    """ Menu to add/remove donors and donations """

    menu = {'1': save_to_disk,
            '2': load_from_disk}

    SAVE_LOAD_PROMPT = ('\n1: Save database to disk\n'
                        '2: Load database from disk\n'
                        'q: Return to main menu\n'
                        '>>> ')

    return display_menu(menu, str, SAVE_LOAD_PROMPT)


def report_menu():
    """ Menu to add/remove donors and donations """

    menu = {'1': text_report,
            '2': html_report}

    REPORT_PROMPT = ('\n1: Generate txt report\n'
                     '2: Generate HTML report\n'
                     'q: Return to main menu\n'
                     '>>> ')

    return display_menu(menu, str, REPORT_PROMPT)


def text_report():
    """ Prints a report of donors and their donations """
    report = '\n' + "-" * 79 + '\n'
    report += 'Donor Name\t\t|           Total Given | Num Gifts |      Average Gift\n'
    report += "-" * 79 + '\n'

    for name in mailroom.database:
        report += (f'{mailroom.database[name].name:24s}   '
                   f'$ {mailroom.database[name].total_donations:18,.2f}')
        if mailroom.database[name].donations == []:
            report += f'\t\t0    '
        else:
            report += f'{len(mailroom.database[name].donations):10}    '
        report += f'$ {mailroom.database[name].average_donation:14,.2f}\n'

    report += "-" * 79 + '\n'

    return report


def html_report():
    """ Saves a report in HTML format """
    now = datetime.datetime.now()
    rendered_page = StringIO()
    page = hr.Html()
    head = hr.Head()
    head.append(hr.Meta(charset="UTF-8"))
    head.append(hr.Title("Mailroom OO Report"))
    page.append(head)
    body = hr.Body()
    body.append(hr.H(2, "Donation Report"))
    table = hr.Table(border=1, width=900)
    table.append(hr.Caption(f'Mailroom Database'))
    table.append(hr.Th('Name'))
    table.append(hr.Th('Total Given'))
    table.append(hr.Th('# of Gifts'))
    table.append(hr.Th('Average Gift'))

    for name in mailroom.database:
        # style="text-align:(left,center,right)"" can go on TR for the whole row or each TD
        table_row = hr.Tr(style="text-align:right")
        table_row.append(hr.Td(f'{mailroom.database[name].name}'))
        table_row.append(hr.Td(f'${mailroom.database[name].total_donations:,.2f}'))
        if mailroom.database[name].donations == []:
            table_row.append(hr.Td('0'))
        else:
            table_row.append(hr.Td(f'{len(mailroom.database[name].donations)}'))
        table_row.append(hr.Td(f'${mailroom.database[name].average_donation:,.2f}'))
        table.append(table_row)

    table_row = hr.Tr()
    table_row.append(hr.Td(f'Generated {now.strftime("%Y-%m-%d %H:%M:%S")}', colspan=4))
    table.append(table_row)
    body.append(table)
    page.append(body)
    page.render(rendered_page, '    ')
    with open('./mailroom.html', 'w') as outfile:
        outfile.write(rendered_page.getvalue())
    return f'HTML report saved to ./mailroom.html'


def save_to_disk():
    """ Save the current database to disk """
    return mailroom.save_db_to_disk()


def load_from_disk():
    """ Load database from disk """
    return mailroom.read_db_from_disk()


def main():
    """ Mailroom main """
    parser = argparse.ArgumentParser()
    parser.add_argument("-O", "--open", help="Open database file")
    args = parser.parse_args()

    if args.open:
        try:
            print(mailroom.read_db_from_disk(args.open))
        except FileNotFoundError:
            print(f'File {args.open} not found, initializing default database\n')
            initialize_donors()
    else:
        initialize_donors()

    display_database()

    menu = {'1': add_remove_menu,
            '2': thank_you_menu,
            '3': report_menu,
            '4': save_load_menu,
            'p': display_database}

    main_prompt = ('\nWelcome to the Mail Room\n'
                   'Please choose from the following options:\n'
                   '1: Add or Remove a Donor or Donation\n'
                   '2: Send a thank you\n'
                   '3: Report menu\n'
                   '4: Save / Load database\n'
                   'p: Print database\n'
                   'q: Quit\n'
                   '>>> ')

    display_menu(menu, str, main_prompt)


if __name__ == '__main__':
    main()
