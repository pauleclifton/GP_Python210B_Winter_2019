
import pytest
from donor_models import Donor
from donor_models import DonorCollection
import cli_main as m
import os

test_donors = {"William Gates": [10000, 20000, 5000, 550000],
          "Mark Zuckerberg": [10, 100, 25, 100],
          "Jeff Bezos": [50,  10, 15, 100],
          "Mark Zuckerberg": [5, 5000.75],
          'David':[3, 2500.17],
        }

def test_donor_init():

    d = Donor('William Gates ')
    assert d.name == 'William Gates '
    d.add_donations(30000)
    d.add_donations(20000)
    assert d.num_donations == 2

    assert d.total_donations == 50000
    assert d.ave_donations == 25000
    
def test_save_letters_disk():
    d = Donor('Paul Allen')
    dc = DonorCollection()
    dc.save_letters_to_disk()  
    assert os.path.isfile('Paul_Allen.txt')



    

