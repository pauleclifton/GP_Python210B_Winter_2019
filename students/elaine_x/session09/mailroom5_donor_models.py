'''
##########################
#Python 210
#Session 09 - Mailroom Part 5
#Elaine Xu
#Mar 13, 2019
###########################
'''

import operator

class Donor():
    '''Generate donor info'''
    def __init__(self, fullname, donation_data):
        self.fullname = fullname
        self.donation_amount = donation_data[0]
        self.donation_number = donation_data[1]

    @staticmethod
    def send_a_thankyou(fullname, donation_amount):
        '''send a thankyou note to donor'''
        return f'Composing Thank You email:\n' \
               f'Thank you {fullname} for your generous donation of ${donation_amount:^10.2f}!'

class DonorCollection():
    '''Create Donors database'''
    donor_dict = {}

    @staticmethod
    def add_donor(fullname, donation_data):
        '''add a new donor to the collection'''
        DonorCollection.donor_dict[fullname] = donation_data

    @staticmethod
    def add_donation(fullname, donation_amount):
        '''add a donation to an existing donor'''
        DonorCollection.donor_dict[fullname][0] += donation_amount
        DonorCollection.donor_dict[fullname][1] += 1
        return f"${donation_amount} has been added to {fullname}'s donation history."

    @staticmethod
    def list_all_names():
        '''list all donor names'''
        return str(DonorCollection.donor_dict.keys())

    @staticmethod
    def create_a_report():
        '''create a donor and donation report'''
        sorted_donor_dict = sorted(DonorCollection.donor_dict.items(), key=operator.itemgetter(1),
                                   reverse=True)
        report_string = ''
        for key, val in sorted_donor_dict:
            report_string += DonorCollection.create_a_report_text(key, val)
        return report_string

    @staticmethod
    def create_a_report_text(key, val):
        '''create a report in tabular and return to original prompt'''
        return "{:<25} ${:>13.2f} {:>13}  ${:>12.2f}\n".format(key, val[0], val[1], val[0] / val[1])

    @staticmethod
    def create_a_report_header():
        '''create header of the report'''
        title = ('Donor Name', 'Total Given', "Num Gifts", 'Average Gift')
        line = "-" * 70
        return "Printing report:\n" \
               "{:<24} | {:^13} | {:^11} | {:^11}\n" \
               "{}".format(*title, line)
