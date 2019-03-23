
# coding: utf-8

# In[12]:


import sys
import datetime
import operator


def menu():
    return(''''Menu
    Please choose from below options:
    1 - Send a Thank You
    2 - Create a Report
    3 - Exit the program
    4 - Print thank you letter to all current donors''')


# first it will ask to choose a name whoom you would want to send the mail
# along side that when typing list it will give you all the names on the current list
# second if the name is not in the list then it will prompt to add the name into the data base
# lastly it will print the message of the email
#added excepts to close off any errors that has to do with input errors
def send_a_thankyou():
    while True:
        fullname = input("Enter the full name of the donor typing list will give the names of current doners ")
        if fullname.lower() == 'list':
            for donor in donor_db:
                print(donor)
        else:
            while True:
                try:
                    amount = float(input("Please enter the donation amount: "))
                    break
                except ValueError:
                    print("Invalid input please try again")
            send_a_thankyou(fullname, amount, donor_db)
            print(f"${amount} has been updated to {fullname}'s donation history.")
            break
    print(f'Thank you {fullname} for your donation of ${amount:^10.2f}!')
    print()
    menu()


def send_thankyou_test(fullname, amount, donor_list):
    donor_list = [donor.lower() for donor in donor_list]
    if fullname.lower() not in donor_list:
        print(f'{fullname} does not exist in the donor data, '
              f'we will add {fullname} to the donor data.')
        donor_list[fullname] = [amount,1]
    elif fullname.lower() in donor_list:
        donor_list[fullname][0] = donor_list[fullname][0] + amount
        donor_list[fullname][1] = donor_list[fullname][1] + 1
    return  fullname, donor_list[fullname]


# this prints out the database of the donors with their total amaounts and average amount donated
def create_a_report():
    print("Printing report:")
    title = ("Donor Name", "| Total Given", "| Num Gifts", "| Average Gift")
    row = " ".join(["{:<19} | {:^13} | {:^13} | {:^11}"]).format(*title)
    length = len(row)
    print("\n" + row)
    print("=" * length)
    for key, value in sorted(donor_db.items()):
        given = str(sum(value))
        gift = str(len(value))
        average = str(sum(value) / (len(value)))
        row_format = (key, "$" + given, gift, "$" + average)
        donor_row = " ".join(["{:<19} | {:^13} | {:^13} | {:^11}"]).format(*row_format)
        print(donor_row)
    print("\n")


def create_a_report_test():
    print("Printing report:")
    title = ("Donor Name", "| Total Given", "| Num Gifts", "| Average Gift")
    row = " ".join(["{:<19} | {:^13} | {:^13} | {:^11}"]).format(*title)
    length = len(row)
    print("\n" + row)
    print("=" * length)
    for key, value in sorted(donor_db.items()):
        given = sum(value[1])
        gift = len(value[1])
        average = sum(value[1]) / (len(value[1]))
        row_format = (key, "$" + given, gift, "$" + average)
        donor_row = " ".join(["{:<19} | {:^13} | {:^13} | {:^11}"]).format(*row_format)
        print(donor_row)
    print("\n")


def sort_total_donation(number):
    return number[1][0]


# this makes a text that has the thankyou message to all the current doners on the list
# the title of the file has the date and the name of the person on the list
def send_letters_to_all_donors():
    '''generate thank you letter to all donors'''
    for key in donor_db:
        with open(key + "_" + str(datetime.date.today()) + ".txt", 'w') as f:
            f.write(send_letter_to_all_donors_test(key,donor_db))
    print("Thank you letters to all donors have been generated in the local disk.\n")


def send_letter_to_all_donors_test(key, donor_list):
    return ("Dear {name},\n"
            "\n"
            "        Thank you for your very kind donation of ${amount:10.2f}.\n"
            "\n"
            "        It will be put to very good use.\n"
            "\n"
            "                       Sincerely\n"
            "                          -The Team".format(name=key, amount=donor_list[key][0]))

def exit_program():
    print("Exiting the program")
    sys.exit()


def main():
    while True:
        try:
            choice = ''
            choice = int(input(menu()))
            if choice in main_menu:
                main_menu[choice]()
            else:
                print("Not a valid option, try again.")
        except ValueError:
            print("Selection has to be a number, try again.\n")
            
# the main frame of the console
main_menu = {1: send_a_thankyou,
             2: create_a_report,
             3: exit_program,
             4: send_letters_to_all_donors
             }

if __name__ == "__main__":
    donor_db = {"William Gates, III": [653784.49, 2],
                "Mark Zuckerberg": [16396.10, 3],
                "Jeff Bezos": [877.33, 1],
                "Paul Allen": [708.42, 3],
                }

    main()