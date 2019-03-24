# import from the MailP4WJ file to test
from MailP4WJ import send_thankyou_test
from MailP4WJ import create_a_report_test
from MailP4WJ import send_letter_to_all_donors_test

donor_db = {"William Gates, III": [653784.49, 2],
            "Mark Zuckerberg": [16396.10, 3],
            "Jeff Bezos": [877.33, 1],
            "Paul Allen": [708.42, 3],
            }

# tests the sending the thank you test
def test_thankyou():
    expected = ('Paul Allen', [708.42, 3])
    assert send_thankyou_test('Paul Allen' , 100, donor_db) == expected

# tests the making the report function
def test_report():
    expected = "Paul Allen          |    $711.42    |       2       |   $355.71  "
    assert create_a_report_test('Paul Allen', [711.42, 2]) == expected

# tests the contents of the letter created
def test_letter():
    expected = "Dear Paul Allen ,\n\n" \
                "        Thank you for your very kind donation of $    711.42.\n" \
               "\n" \
               "                       Sincerely\n" \
               "                          -The Team"
    assert  send_letter_to_all_donors_test() == expected
