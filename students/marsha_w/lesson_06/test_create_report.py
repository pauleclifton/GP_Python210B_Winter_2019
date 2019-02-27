#!/usr/bin/env python3

'''Title: Unit testing for create a report function
Dev: Marsha Wheeler
Date: 02/23/2019
'''

from mailroom4 import create_report, donor_dict


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





