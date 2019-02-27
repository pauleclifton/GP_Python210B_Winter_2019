import mailroom as mp
from datetime import date


def test_get_report():
    expected = [
        '           Name   Donation ($)         Amount    Average ($)',
        '       Art Bart        1000.00              1        1000.00',
        '    Harry Scary          50.00              5          10.00',
        '        Hay Boo       50000.00              3       16666.67']
    for row in mp.get_report():
        assert row in expected


def test_write_letter():
    name = 'Daniel Carrasco'
    value = [666]
    expected = [f'\tDear {name}\n',
                f'Thank you for your very kind donation of ${value[0]}.\n',
                'It will be put to very good use.\n',
                '\tSincerely\n',
                '\t\t-The Team']
    print(expected)
    assert mp.write_letter('Daniel Carrasco', [666]) == expected


def test_name_of_file():
    today = str(date.today())
    expected = 'Art Bart_2019-02-24.txt'
    assert mp.name_of_file('Art Bart') == expected
