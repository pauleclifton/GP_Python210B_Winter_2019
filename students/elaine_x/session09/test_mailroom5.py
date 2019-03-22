'''
##########################
#Python 210
#Session 09 - Mailroom Part 5 Unit Test
#Elaine Xu
#Mar 13, 2019
###########################
'''
from mailroom5_donor_models import *

donor_db = {"William Gates, III": [653772.32, 2],
            "Jeff Bezos": [877.33, 1],
            "Paul Allen": [663.23, 3],
            "Mark Zuckerberg": [1663.23, 3],
            "Bob Smith": [500.00, 1],
            }
def test_donor_initialization():
    d1 = Donor("Paul Allen", [663.23, 3])
    assert d1.fullname == "Paul Allen"
    assert d1.donation_amount == 663.23
    assert d1.donation_number == 3

def test_send_a_thankyou():
    '''send a thankyou note to donor'''
    expected = "Composing Thank You email:\n" \
               "Thank you {} for your generous donation of ${:^10.2f}!".format('Paul Allen', 100)
    assert Donor.send_a_thankyou('Paul Allen', 100) == expected

def test_add_donation():
    '''add a new donor to the collection'''
    for donor in donor_db:
        DonorCollection.add_donor(donor, donor_db[donor])
    expected = "$500 has been added to Paul Allen's donation history."
    assert DonorCollection.add_donation('Paul Allen', 500) == expected

def test_list_all_name():
    expected = "dict_keys(['William Gates, III', 'Jeff Bezos', 'Paul Allen', 'Mark Zuckerberg', 'Bob Smith'])"
    assert DonorCollection.list_all_names() == expected

def test_create_a_report():
    '''test the text created by create_a_report'''
    expected = "Mark Zuckerberg           $      1663.23             3  $      554.41\n"
    assert DonorCollection.create_a_report_text('Mark Zuckerberg', [1663.23, 3]) == expected

def test_create_a_report_header():
    title = ('Donor Name', 'Total Given', "Num Gifts", 'Average Gift')
    line = "-" * 70
    expected = "Printing report:\n" \
               "{:<24} | {:^13} | {:^11} | {:^11}\n" \
               "{}".format(*title, line)
    assert DonorCollection.create_a_report_header() == expected