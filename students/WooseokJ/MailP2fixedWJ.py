
# coding: utf-8

# In[3]:


# print of the main menu
import sys
import datetime
import operator

def menu():
    print(''''Menu
    Please choose from below options:
    1 - Send a Thank You
    2 - Create a Report
    3 - Exit the program
    4 - Print thank you letter to all current doners''')
#first it will ask to choose a name whoom you would want to send the mail
#along side that when typing list it will give you all the names on the current list
#second if the name is not in the list then it will prompt to add the name into the data base
#lastly it will print the message of the email
# have a problem here where when asked for the amount of donation if the value type is not a number we get a error how to loop around this?
def send_a_thankyou():
    donor_list = []
    for donor in donor_db:
        donor_list.append(donor.lower())
    while True:
        fullname = input("Enter the full name of the donor typing list will give the names of current doners ")
        if fullname.lower() == 'list':
            for donor in donor_db:
                print(donor)
        elif fullname.lower() not in donor_list:
            print(f'{fullname} does not exist in the donor data, '
                  f'we will add {fullname} to the donor data.')
            amount = float(input("Please enter the donation amount: "))
            donor_db.append((fullname, [amount, 1]))
            print(f"{amount} has been added to {fullname}'s donation history.")
            break
        elif fullname.lower() in donor_list:
            fullname = donor_list.index(fullname.lower())
            amount = float(input("Please Enter the donation amount: "))
            donor_db[fullname][1][0] = donor_db[fullname][1][0] + amount
            donor_db[fullname][1][1] = donor_db[fullname][1][1] + 1
            print(f"{amount} has been added to {fullname}'s donation history.")
            break
    print("Creating a Thank You email:")
    print(f'Thank you {fullname} for your donation of {amount:^10.2f}!')
    print()
    menu()
#this prints out the database of the donors with their total amaounts and average amount donated
def create_a_report():
    sorted_donor_db = sorted(donor_db.items(), key=operator.itemgetter(1), reverse=True)
    print("Printing report:")
    title = ('Donor Name', 'Total Given', "Num Gifts", 'Average Gift')
    print("{:<19} | {:^13} | {:^13} | {:^11}".format(*title))
    print("-"*70)
    for i, row in enumerate(donor_db):
        print("{:<21} ${:>13.2f} {:>13}  ${:>12.2f}"
              .format(donor_db[i][0], donor_db[i][1][0], donor_db[i][1][1],
                      donor_db[i][1][0]/donor_db[i][1][1]))
    print()
    menu()
    
def sort_total_donation(number):
    return number[1][0]
#this makes a text that has the thankyou message to all the current doners on the list
#the title of the file has the date and the name of the person on the list
def send_letters_to_all_donors():
    '''generate thankyou letter to all donors'''
    for key in donor_db:
        with open(key+"_"+str(datetime.date.today())+".txt", 'w') as f:
            f.write("Dear {name},\n"
                    "\n"
                    "        Thank you for your very kind donation of ${amount:10.2f}.\n"
                    "\n"
                    "        It will be put to very good use.\n"
                    "\n"
                    "                       Sincerely\n"
                    "                          -The Team".format(name=key, amount=donor_db[key][0]))
    print("Thank you letters to all donors have been generated in the local disk.\n")

def exit_program():
    print("Exiting the program")
    sys.exit()

def main():
    choice = ''
    while True:
        choice = int(input(menu()))
        if choice in main_menu:
            main_menu[choice]()
        else:
            print("Not a valid option, try again.")
#the main frame of the console 
main_menu = {1: send_a_thankyou,
            2: create_a_report,
            3: exit_program,
            4: send_letters_to_all_donors
            }

if __name__ == "__main__":

    donor_db = {"William Gates, III": [ 653784.49, 2],
                "Mark Zuckerberg": [16396.10, 3],
                "Jeff Bezos": [877.33, 1],
                "Paul Allen": [708.42, 3],
               }

    main()

