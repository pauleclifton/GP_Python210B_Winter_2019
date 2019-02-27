#!/usr/bin/env python3

'''Title: Unit testing for create a report function
Dev: Marsha Wheeler
Date: 02/23/2019
'''

from mailroom4 import create_report, write_text, write_file, send_thank_you, donor_dict
import os.path
import datetime

# test create report function
def test_donationsum_order():
    report_dict = create_report()
    assert report_dict[0][1] > report_dict[1][1]
    assert report_dict[0][1] > report_dict[2][1]
    assert report_dict[1][1] > report_dict[2][1]


def test_num_donations(donor="William Gates"):
    report_dict = create_report()
    dict_num = len(donor_dict[donor])
    for i in report_dict:
        if donor in i:
            assert dict_num == (i[2])

def test_check_sum(donor="Mark Zuckerberg"):
    report_dict = create_report()
    dict_sum = sum(donor_dict[donor])
    assert dict_sum == report_dict[1][1]


def test_check_mean(donor="Paul Allen"):
    report_dict = create_report()
    dict_mean = sum(donor_dict[donor]) / len(donor_dict[donor])
    assert dict_mean == report_dict[3][3]

#test write email functions

def test_write_text():
    expected_text = "Dear Jeff Bezos, \n We are writing to thank you for your generous total donation of $877.33 " \
                 "to our organization. \n Sincerely, "
    assert expected_text == write_text("Jeff Bezos")


def test_write_text2():
    expected_text = "Dear William Gates, \n We are writing to thank you for your generous total donation of $653784.49 " \
                 "to our organization. \n Sincerely, "
    assert expected_text == write_text("William Gates")


def test_write_file():
    write_file()
    for keys in donor_dict:
        date = str(datetime.datetime.now()).split()
        out_name = str(keys.replace(' ', '_') + '_' + date[0] + ".txt")
        assert os.path.isfile(
            '/Users/marshawheeler/GP_Python210B_Winter_2019/students/marsha_w/lesson_06/' + out_name)


#test appending send_thank_you function

def test_donor_name1(donor="Paul Allen", amount=float(500)):
    send_thank_you(donor, amount)
    assert donor in donor_dict


def test_append_value1(donor="Paul Allen", amount=float(500)):
    send_thank_you(donor, amount)
    assert amount in donor_dict[donor]

def test_donor_name2(donor="Mark Zuckerberg", amount=float(1000)):
    send_thank_you(donor, amount)
    assert donor in donor_dict


def test_append_value2(donor="Mark Zuckerberg", amount=float(10000)):
    send_thank_you(donor, amount)
    assert amount in donor_dict[donor]


def test_append_name3(donor="Amy Klobuchar", amount=float(1000)):
    send_thank_you(donor, amount)
    assert amount in donor_dict[donor]


def test_append_value3(donor="Marsha Wheeler", amount=float(1000)):
    send_thank_you(donor, amount)
    assert amount in donor_dict[donor]


def test_thank_you(donor="Amy Klobuchar", amount=float(1000)):
    thank_you_test = send_thank_you(donor, amount)
    if donor in thank_you_test and str(amount) in thank_you_test:
        return True





