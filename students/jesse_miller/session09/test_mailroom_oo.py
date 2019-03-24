#!/usr/bin/env python3
'''
Here we go testing again!
'''
import datetime
import pytest

from mail_box import MailBox
from donor_models import DonorTools, DonorCollection
from cli_main import MailRoom
################################################################################
'''
donor_models.py testing. We'll start with testing the DonorTools class.
'''
################################################################################
def test_donor_init():
    '''
    This tests adding a donor
    '''
    donor = DonorTools('James Hetfield')
    assert donor.name == 'James Hetfield'
    assert donor.donations == []


def test_donor_init_error():
    '''
    Now, let's see if we can break it
    '''
    with pytest.raises(TypeError):
        #pylint: disable=E1121
        DonorTools('Kirk Hammett', 400)


def test_donation_add():
    '''
    Let's try to add money the right way
    '''
    donor = DonorTools('James Hetfield')
    donor.donation_add(400)
    assert donor.donations == [400.00]

    donor.donation_add(3000.25)
    assert donor.donations == [400.00, 3000.25]


def test_donation_count():
    '''
    Let's make sure I can count
    '''
    donor = DonorTools('Kirk Hammett')
    donor.donation_add(1400)
    assert donor.donation_count == 1

    donor.donation_add(2300)
    assert donor.donation_count == 2


def test_donation_total():
    '''
    Let's make sure I can add
    '''
    donor = DonorTools('Kirk Hammett')
    donor.donation_add(1400)
    donor.donation_add(2300)
    donor.donation_add(5400)
    assert donor.donation_total == 9100


def test_donation_avg():
    '''
    Testing if I can divide
    '''
    donor = DonorTools('Kirk Hammett')
    donor.donation_add(3000)
    donor.donation_add(700)
    donor.donation_add(5300)
    assert donor.donation_average == 3000


def test_letter():
    '''
    This is the one that I'm not confident over.  The formatting worries at me,
    it should work... but...
    '''
    donor = DonorTools('James Hetfield')
    donor.donation_add(1310)
    count = int(donor.donation_count)
    total = float(donor.donation_total)
    letter = MailBox.letter_template(donor, total, count)
    date = datetime.datetime.now().strftime("%B %d, %Y")

    assert letter == f'{date} \n'\
    f'\nHello {donor}, \n'\
    f'\n'\
    f'We are writing to thank you for you generous donation\n'\
    f'to our foundation.  Your contributions for the year \n'\
    f'total $1,310.00 in 1 disbursements.'\
    f'\n'\
    f'\n'\
    f'Again, the foundation thanks you for your support, \n'\
    f'and we hope to remain in contact with you in this new \n'\
    f'year.\n'\
    f'\n'\
    f'Sincerely, \n'\
    f'Ecumenical Slobs LLC \n'


'''
Moving on to testing donor manipulation
'''
def test_init():
    '''
    Testing the init function
    '''
    testing = DonorCollection()
    assert 'Chris Stapleton' in testing.donors_dict


def test_donor_creation():
    '''
    Here, we create a donor
    '''
    testing = DonorCollection()
    testing.donor_creation('Kirk Hammett')

    assert 'Kirk Hammett' in testing.donors_dict
    assert testing.donors_dict['Kirk Hammett'].donations == []
    #assert testing.donors_dict['Kirk Hammett'].append(1312.25)


def test_donor_list():
    '''
    Testing our listing function
    '''
    testing = DonorCollection()
    test_list = testing.list_donor()
    assert 'Devin Townsand' in test_list


def test_find_donor_exists():
    '''
    This is to test if it can find an existing donor
    '''
    testing = DonorCollection()
    assert 'JD Cronise' in testing.donors_dict
    assert testing.donors_dict['JD Cronise'].donations == [125.23]
    assert testing.find_donor('JD Cronise') == testing.donors_dict['JD Cronise']


def test_delete_donor():
    '''
    Testing the delete function
    '''
    testing = DonorCollection()
    testing.delete_donor('JD Cronise')
    test_list = testing.list_donor()
    assert test_list == ['Chris Stapleton', 'Dave Lombardo', 'Devin Townsand', \
    'Randy Blythe', 'Robert Smith']


################################################################################
'''
cli_main.py testing
'''
################################################################################
def test_main_donor_list(capsys):
    '''
    Testing our listing function
    '''
    MailRoom.list_donors()
    captured = capsys.readouterr()
    assert "Robert Smith" in captured.out
    assert "JD Cronise" in captured.out


def test_main_report(capsys):
    '''
    Testing the full reporting
    '''
    MailRoom.print_report()
    captured = capsys.readouterr()
    assert '$2,062.16' in captured.out
