import sys  # imports go at the top of the file

# Data Structure
donor_db = {"William Gates, III": [653772.32, 12.17],
            "Jeff Bezos": [877.33],
            "Paul Allen": [663.23, 43.87, 1.32],
            "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
            "Elon Musk": [2263.23, 3300.87, 15432.0],
            }

''' First Comprehesion'''
new_donor_dic = \
    {d: donors for d, donors in donor_db.items()}

# Input/Output
prompt = "\n".join(("Mail Distribution Center!",
                    "Please choose from below options:",
                    "1 - Send a Thank You to a single donor",
                    "2 - Create a Report",
                    "3 - Send letters to all donors",
                    "4 - Exit",
                    ">>> "))

# Features
''' Second Comprehension'''
dict_comp = {d for d in donor_db.keys()}


def view_donor_names():
    for donor in donor_db.keys():
        print(donor)


def write_a_letter(donor, amount):
    letter = f"Dear {donor},\n\nThank you for your kind donation of ${str(amount)}\n\n" \
        f"It will be put to very good use.\n\n" \
        f"Sincerely,\n" \
        f"The Fundraising Committee"
    return letter


def write_a_letter_all(donor):
    letter = f"Dear {donor},\n\nThank you for your kind donation. \n\n" \
        f"It will be put to very good use.\n\n" \
        f"Sincerely,\n" \
        f"The Fundraising Committee"
    return letter


def dir_for_letter():
    input("Hit <Enter/Return> key to save to the current working directory.")


def thank_you_letter():
    answer = input("Please enter Full Name.>>>")
    if answer.lower() == 'list':
        for donor in donor_db.keys():
            print(donor)
    else:
        if answer in donor_db:
            current_donor(answer)
        else:
            add_donor(answer)


def letter_to_all_donors():
    dir_for_letter()
    for donor in donor_db.keys():
        with open(f'{donor}.txt', 'wt') as letter:
            letter.write(switch_func_dict.get(1)(donor))


def get_letter_text(donor):
    letter_to_all_donors()
    return f"{donor}, Thank you for your kind donation"


def get_value(text, check_type):
    while True:
        try:
            value = check_type(input(text))
            return value
        except ValueError:
            print("Invalid value. Please try again")
            continue


def current_donor(donor):
    amount = get_value("Please enter donor amount.>>>", float)
    donor_db[donor].append(float(amount))
    dir_for_letter()
    with open(f'{donor}.txt', 'wt') as letter:
        letter.write(switch_func_dict.get(0)(donor, amount))
    print('Thanks, {} for your generous donation.'.format(donor))


def sort_key(donor_db):
    return donor_db[:]


def add_donor(new_donor):
    donor_amount = get_value("What is the donation amount?.>>>", float)
    donor_db[new_donor] = [float(donor_amount)]
    print(donor_db)
    dir_for_letter()
    with open(f'{new_donor}.txt', 'wt') as letter:
        letter.write(switch_func_dict.get(0)(new_donor, donor_amount))
    print('Thanks, {} for your generous donation.'.format(new_donor))


def report():

    headers = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]
    print()
    print("{:20} | {:10} | {:10} | {}".format(headers[0], headers[1], headers[2], headers[3]))
    print("-" * 80)

    summary = create_summary()
    for i in summary:
        print("{:20}  ${:>12,.2f}{:>10}     ${:>14,.2f}".format(i[0], i[1], i[2], i[3]))
        print("")


def create_summary():
    summary = []
    for k, v in donor_db.items():
        total = (sum(v))
        times = (len(v))
        avg = (sum(v) / len(v))
        summary.append([k, total, times, avg])

    summary.sort(key=lambda d: d[1], reverse=True)
    return summary


def exit_program():
    print("Good-Bye!")
    sys.exit()  # exit the interactive script


# Processing
def main():
    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "1":
            thank_you_letter()
        elif response == "2":
            report()
            pass
        elif response == "3":
            letter_to_all_donors()
        elif response == "4":
            exit_program()
        else:
            print("Not a valid option!")


''' Switch with the above functions "write_a_letter and write_a_letter_all" '''

switch_func_dict = {
    0: write_a_letter,
    1: write_a_letter_all,
}

if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()
