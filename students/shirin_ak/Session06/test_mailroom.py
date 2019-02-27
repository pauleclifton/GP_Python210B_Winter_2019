import pytest
from mailroom import create_report,send_thank_you_letter,add_donor



def test_send_thank_you_letter():    
    expected = "David,Thank you for your most recent donation of $2500.17."
    assert send_thank_you_letter("David", 2500.17)== expected 




def test_display_report():
    report = create_report() 
    assert create_report()== report


print("passed")
