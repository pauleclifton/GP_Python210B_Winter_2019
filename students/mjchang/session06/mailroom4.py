#!/usr/bin/env python3

import os
import datetime
import sys
import unittest


def donor_db(): #defining donor database to make it easier to test
    return {"Eliza Sommers": [4000, 250, 70],
            "Tao Chien": [350, 1000, 225], 
            "Joaquin Andieta": [100, 25], 
            "Paulina Rodriguez": [50000], 
            "Jacob Todd": [75, 80]} 

def donor_list(): #splitting thank_you_one function into multiple parts in mailroom4
    print('\n'.join(donor_db.keys())) #displays list of donors


def generate_letter(name, donation):
    message = "Dear {}, \n\n Thank you for your generous donation of ${:10.2f}. \n You have helped make a big impact on the community!".format(name, donation)
    return message

def add_new_donor(name):
    print("Adding {} to the donor list".format(name))
        #adding exception for donation input that isn't a number
    try:
        donation = input("Enter the donation amount from {}: ".format(name)) #adding donation from new donor
        donation = float(donation) #converting to a float
    except (ValueError, EOFError): 
        print("Donation amount must be a number")   
    donor_db.setdefault(name, []).append(donation)
    print(generate_letter(name, donation))

def add_new_donation(name):
    try:
        donation = input("Enter the new donation amount: ")
        donation = float(donation)
    except (ValueError, EOFError):
        print("Donation amount must be a number")
    donor_db[name].append(donation)
    print(generate_letter(name, donation))


def thank_you_one(): # adding a new vendor
    while True:
        name = input("Please enter a full name (or 'list' for a list of current donors): ")
        name = name.title() #keeps capitalization format the same
        if name.lower() == "list":
            donor_list()
        
        elif name not in donor_db.keys(): #adding new donor
            add_new_donor(name)
            break
        
        elif name in donor_db.keys(): #adding donation for existing donor
            add_new_donation(name)
            break

def thank_you_all_text(key):
    return "Dear {}, \n\n On behalf of all of us, we thank your for your generous donation. \n You have helped make a big impact on the community!".format(key)

# send the thank you letter to all donors
def thank_you_all():
    path = os.getcwd()
    folder = path + '/donor_letters/'
    os.mkdir(folder)
    os.chdir(folder)
    for key in donor_db:
        timestamp = str(datetime.date.today())
        with open(key + '_' + timestamp + ".txt", "w+") as f:
            f.write(thank_you_all_text(key))
            f.close()

    print("Letters to all donors were generated.")


# set up for donor report
def sort_key(data):
    return data[1]

def report_line(data):
    return "{:<30}  ${:12.2f}   {:>15}  ${:12.2f}".format(data[0], data[1], data[2], data[3])

# create a report of donors and amounts
def donor_report():
    #using a list comprehension to simplify building the donor report 
    spreadsheet = [(name, sum(gifts), len(gifts), sum(gifts)/len(gifts))
    for name, gifts in donor_db.items()]

    #sort the report by total donation
    spreadsheet.sort(key = sort_key)

    print("{:<30} | {:<12} | {:>15} | {:12}".format("Donor Name", "Total Given", "Number of Gifts", "Average Gift")) #print the header
    print("-"*79) #print the dashed line
    for data in spreadsheet:    
       print(report_line(data)) 


def quit_program():
    print("Goodbye!\n")
    sys.exit()


def main():
    while True:
        response = ''
        response = int(input("""
        Please enter a number from the following options:
            1 - Send a Thank You to One Donor
            2 - Send a Thank You to All Donors
            3 - Create a Report
            4 - Quit
        """))
        selection = {1: thank_you_one, 
                2: thank_you_all, 
                3: donor_report,
                4: quit_program
                }
        #adding exception to handle responses other than 1-4
        try:
            if response in selection.keys():
                selection.get(response)()
            else:
                print("Please make a valid selection")
        except (ValueError, EOFError):
            print("Please select from the available options")
            continue
        

if __name__ == "__main__":  


    donor_db = donor_db()

    main()             