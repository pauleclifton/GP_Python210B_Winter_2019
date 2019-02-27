'''
##########################
#Python 210
#Session 06 - Mailroom Part 4 Unit Test
#Elaine Xu
#Feb 24, 2019
###########################
'''
from mailroom4 import send_a_thankyou_text
from mailroom4 import create_a_report_text
from mailroom4 import send_letters_to_all_donors_text

donor_db = {"William Gates, III": [653772.32, 2],
            "Jeff Bezos": [877.33, 1],
            "Paul Allen": [663.23, 3],
            "Mark Zuckerberg": [1663.23, 3],
            "Bob Smith": [500.00, 1],
            }

def test_send_a_thankyou1():
    '''send a thankyou note to donor'''
    expected = ('Paul Allen', [763.23, 4])
    assert send_a_thankyou_text('Paul Allen', 100, donor_db) == expected

def test_send_a_thankyou2():
    '''send a thankyou note to donor'''
    expected = ('Sarah Smith', [100.00, 1])
    assert send_a_thankyou_text('Sarah Smith', 100, donor_db) == expected

def test_create_a_report():
    '''test the text created by create_a_report'''
    expected = "Mark Zuckerberg           $      1663.23             3  $      554.41"
    assert create_a_report_text('Mark Zuckerberg', [1663.23, 3]) == expected

def test_send_letters_to_all_donors_text():
    '''test the text generated by send_letters_to_all_donor'''
    expected = "Dear Jeff Bezos,\n\n" \
                "        Thank you for your very kind donation of $    877.33.\n" \
                "\n" \
                "        It will be put to very good use.\n" \
                "\n" \
                "                       Sincerely\n" \
                "                          -The Team"
    assert send_letters_to_all_donors_text('Jeff Bezos', donor_db) == expected
