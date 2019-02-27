#-------------------
#!/usr/bin/env python3
#Session 06 Exercise:mailroom_part4
#Shirin Akther
#-------------------------


import sys

#Write a mailroom program where it should have a data structure that holds
#a list donors and a history of the amounts they have donated.
#This structure should be populated at first with at least five donors, with
# between 1 and 3 donations each.
#It should prompt the user (you) to choose from a menu of 3 actions:
#“Send a Thank You”, “Create a Report” or “quit”.
#If the user (you) selects “Send a Thank You” option, prompt for a Full Name.
#If the user types list show them a list of the donor names and re-prompt.
#If the user types a name not in the list, add that name to the data structure and use it.
#If the user types a name in the list, use it.
#Once a name has been selected, prompt for a donation amount.
#Convert the amount into a number 
#Add that amount to the donation history of the selected user.
#Finally, use string formatting to compose an email thanking the donor for their
#generous donation. Print the email to the terminal and return to the original prompt.


DONORS_NAME = {'william gates':[3, 3000.45],
               'Jeff Bezos':[2, 3452.00],
               'Paul Allen':[2, 9970.65],
               'Mark Zuckerberg': [5, 5000.75],
               'David':[3, 2500.17],
               'Michael':[4, 1500.00],
               'Allen':[1, 2400.35]}



PROMPT = "\n".join(("Please select a menu option below:",
                    "1 - Send a Thank You to an individual",
                    "2 - Create a Report",
                    "3 - Send letters to all donors",
                    "4 - Quit",
                    ">>> "))


def create_report():
    """Create a detailed report of donors and their history of the amounts they have donated"""
    
    donor_report = []    
    for name in DONORS_NAME:
        total_donation = (DONORS_NAME[name][1])
        donation_times = (DONORS_NAME[name][0])
        avg_donate = round((total_donation / donation_times), 2)
        donor_report.append((name, total_donation, donation_times, avg_donate))
        donor_report.sort(key=lambda x: x[1], reverse=True)
        report = []
    for i in donor_report:        
        report.append("{:16} {:<20} {:<17} {:<22}".format(i[0], i[1], i[2], i[3]))
    return '\n'.join(report)


def display_report():
    print("{:12} {:<16} {:<25} {:<20}\n".format("Name", "Total Donation",
                                             " Number of Gifts", "Average Gifts"))
    print('-'*70)
    print(create_report())
    print("\n")

    
def add_donor():
    """ prompt for a Full Name.if user types 'list' show donor names,if types 'quit'
        return to the main menu ,if types a name not in the list add that to the list,
        if types a name in the list use it and prompt for donation amount,Add that amount
        to the donation history """

    while True:
        print("\nEnter 'list' to see list of names.")
        print("Enter 'quit' to go back.")
        print("Enter 'name' to add new donor.")
        name = input("Please enter a name: ")
        if name == 'list':
            print_donor_list()
        elif name == 'quit':
            break
        else:
            donation_amount = get_donation()
            
            if name not in DONORS_NAME:
                DONORS_NAME[name] = [1, donation_amount]
            else:
                DONORS_NAME[name][0] = DONORS_NAME[name][0] + 1
                DONORS_NAME[name][1] = DONORS_NAME[name][1] + donation_amount
            send_thank_you_letter(name, donation_amount)
            break

        
def donor_list():
    """ Updated by Comprehensions"""
    name_list = [name for name in DONORS_NAME]    
    return '\n'.join(name_list)   
        

def print_donor_list():
    print("\nDonor Names:")
    print("-" *15)
    print(donor_list())

    
def get_donation():
    """ updated this function using Error handling.
        It gets donation from the donor"""
    while True:       
        donation = input("\nPlease Enter a Valid Amount.""\n$")
                               
        try:
            donation = float(donation)
            return donation
        except ValueError:
             print("\nError.It is not valid amount.")

             
def send_thank_you_letter(name, donation_amount):
    """ Create a thank you message """
    message = f"{name},Thank you for your most recent donation of ${DONORS_NAME[name][1]}."
    return message


def file_name(name):
    'Return a txt file name based on the donor name and using underscores instead of spaces'
    return name.replace(' ', '_') + '.txt'     


def save_letter_disk(letter, name, amount):
    """ Save a copy of a Thank You letter when the letter is sent"""
    out_file = open(file_name(name), 'w')    
    out_file.write(letter)      
    out_file.close()

    
def send_letter_for_all():
    """ Send a thank you message to all donors"""
    print("***\nloading letters for all donors\n***")
    for name in list(DONORS_NAME.keys()):
        amount = DONORS_NAME[name][0] * DONORS_NAME[name][1]
        message = send_thank_you_letter(name, amount) 
        save_letter_disk(message, name, str(amount))

        
def exit_program():
    print("Bye!")
    sys.exit(0)

    
def main():
    """ Updated menu function using dictionary and Error handling """
    selection_dict = {"1": add_donor, 
                      "2": display_report,
                      "3": send_letter_for_all,
                      "4": exit_program,
                      }
    while True:
        selection = input(PROMPT)
        try:  
            selection_dict[selection]()
        except KeyError:
            print("error: menu selection is invalid!")
     

if  __name__ == '__main__':
    main()





