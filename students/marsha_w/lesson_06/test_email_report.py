#!/usr/bin/env python3

'''Title: Unit testing for write a report function
Dev: Marsha Wheeler
Date: 02/22/2019
'''


from mailroom4 import write_text, write_file, donor_dict
import os.path
import datetime



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
