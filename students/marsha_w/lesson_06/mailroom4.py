#!/usr/bin/env python3

'''Title: Mailroom exercise, part3
Dev: Marsha Wheeler
Date: 02/22/2019
'''

import sys
import datetime
import copy


donor_dict = {"William Gates": [653772.32, 12.17],
              "Jeff Bezos": [877.33],
              "Paul Allen": [663.23, 43.87, 1.32],
              "Mark Zuckerberg": [1663.23, 4300.87, 10432.0]
              }

user_prompt = "\n".join(("Please choose from the options below:",
                         "1 - To view a list of donors type 'list'",
                         "2 - Send a Thank You to a single donor",
                         "3 - Create a Report",
                         "4 - Write a Thank you note to all donors",
                         "5 - Exit the Program",
                         ">>> "))


def show_list():
    '''Show list of donors'''
    print("Current donors in the database include:")
    donors = list(donor_dict.keys())
    print(('{} \n' * len(donors)).format(*donors))


def send_thank_you(donor_name, donation_amount):
    thank_you_text = "Dear {:s}, \n We are writing to thank you for your generous donation of ${:.2f} to our organization. \
                     \n Sincerely,"

    if donor_name in donor_dict:
        try:
            user_amount = float(donation_amount)
            donor_dict.setdefault(donor_name, []).append(user_amount)

            # Generate an email using string formatting:
            return thank_you_text.format(donor_name, user_amount)

        except ValueError:
            return 'ValueError: Please enter an integer or a decimal number \n'

    else:
        try:
            user_amount = float(donation_amount)
            donor_dict[donor_name] = [user_amount]

            # Generate an email using string formatting:
            return thank_you_text.format(donor_name, user_amount)

        except ValueError:
            return 'ValueError: Please enter an integer or a decimal number \n'


def get_user_input():
    user_name = input("Please enter a donor name:").title()
    user_amount = float(input("Please enter a donation amount for " + user_name + ":" ))
    print(send_thank_you(user_name, user_amount))

def create_report():
    # create a new list with donor names, total donation, number of donations and average donations
    donor_list = list(donor_dict.items())

    # Use comprehension to create a new list
    donor_summary = [[donor[0], float(sum(donor[1])), int(len(donor[1])), float(sum(donor[1])) / int(len(donor[1]))]
                     for donor in donor_list]

    def sort_key(donor_summary):
        return donor_summary[1]

    sorted_donor_summary = (sorted(donor_summary, key=sort_key, reverse=True))
    return sorted_donor_summary


def display_report_summary():
    sorted_summary = create_report()
    table_header = ["Name", "Total Given", "Numb of Gifts", "Average Gift"]
    sorted_summary.insert(0, table_header)
    dash = '-' * 70
    for i in range(len(sorted_summary)):
        if i == 0:
            print(dash)
            print('{:20} | {:>10s} | {:>15s} | {:>15s}'.format(sorted_summary[i][0], sorted_summary[i][1],
                                                               sorted_summary[i][2], sorted_summary[i][3]))
            print(dash)
        else:
            print('{:20} ${:>10.1f}{:>20d} ${:>16.1f}'.format(sorted_summary[i][0], sorted_summary[i][1],
                                                              sorted_summary[i][2], sorted_summary[i][3]))


def write_text(keys):
    donor_dict_copy = copy.copy(donor_dict)
    donor_sum = donor_dict_copy[keys] = sum(donor_dict_copy[keys])
    email_text = "Dear {:s}, \n We are writing to thank you for your generous total donation of ${:.2f} " \
                 "to our organization. \n Sincerely, ".format(keys, donor_sum)
    return email_text


def write_file():
    date = str(datetime.datetime.now()).split()

    for keys in donor_dict:
        out_name = str(keys.replace(' ', '_') + '_' + date[0] + ".txt")
        out_file = open(out_name, 'w')
        print(write_text(keys))
        out_file.write(write_text(keys))
        out_file.close()

def exit_program():
    print("You chose to exit the program, Bye!")
    sys.exit()  # exit the interactive script


def main():
    while True:
        try:
            user_response = input(user_prompt)
            switch_func_dict = {
                '1': show_list,
                '2': get_user_input,
                '3': display_report_summary,
                '4': write_file,
                '5': exit_program,
            }

            switch_func_dict.get(user_response)()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()