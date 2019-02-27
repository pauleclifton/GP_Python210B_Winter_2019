#!/usr/bin/env python3

'''Title: Unit testing for send report function
Dev: Marsha Wheeler
Date: 02/22/2019
'''

from mailroom4 import donor_dict, send_thank_you


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


















