#!/usr/local/bin/python3
'''
Beginning of my mailroom implementation.
'''
import sys
import os
import datetime

donors = {'Robert Smith': [435.56, 125.23, 357.10],
          'JD Cronise': [123.12],
          'Chris Stapleton': [243.87, 111.32],
          'Dave Lombardo': [63.23, 422.87, 9432.01],
          'Randy Blythe': [223.50, 8120.32],
          'Devin Townsand': [431.12, 342.92, 5412.45],
          }

PROMPT = '\n'.join(('Welcome to mailroom 0.5!',
                    '',
                    'Please choose from below options:',
                    'report - If you would like a report of donations totals.',
                    'send - If you would like to send a thank you.',
                    'list - If you would like to see a list of donors.',
                    'delete - Remove a donor',
                    'quit   - Exit.',
                    '>>> '))

VALID_INPUT = ('report', 'quit', 'list', 'send', 'all', 'delete')

MAIL = ('\nHello {}, \n'
        '\n'
        'We are writing to thank you for you generous donation\n'
        'to our foundation.  Your contributions for the year \n'
        'total ${:,.2f} in {} disbursements. \n'
        '\n'
        'Again, the foundation thanks you for your support, \n'
        'and we hope to remain in contact with you in this new \n'
        'year.\n'
        '\n'
        'Sincerely, \n'
        'Ecumenical Slobs LLC \n')


def donor_list():
    '''
    This when done properly, will print the list of donor names
    '''
    print(f"\n{'-'*15}\nList of Donors:\n{'-'*15}")
    for donor in donors:
        print(donor)
    print(f"{'-'*15}\n")


def donor_report():
    '''
    This will be the donation report section
    '''
    summary = []
    headers = ['Donor Name', 'Total Given', 'Times Donated', 'Average Gift']

    print(f"\n{'-'*80}\n{{:17}} | {{:<19}} | {{:<15}} | {{:<19}}\n{'-'*80}"\
    .format(headers[0], headers[1], headers[2], headers[3]))

    for k, v in donors.items():
        summary.append([k, (sum(v)), (len(v)), (sum(v) / len(v))])
    summary.sort(key=lambda d: d[1], reverse=True)

    for x_value in summary:
        print('{:17} | ${:<18,.2f} | {:<15} | ${:<16,.2f}'.format
              (x_value[0], x_value[1], x_value[2], x_value[3]))
    print(f"{'-'*80}\n")



def donor_mail_choice():
    '''
    This section allows the user to mail a donor
    '''
    current_donor = ''
    donor_list()
    try:
        current_donor = str(input('Who would you like to mail (all for all): '))
        if current_donor in donors:
            mail_send(current_donor)
        elif current_donor == 'all':
            mail_send(current_donor)
        else:
            donor_add(current_donor)
    except (KeyboardInterrupt, EOFError, ValueError):
        safe_input()


def donor_add(current_donor):
    '''
    This allows addition of new donors
    '''
    donors[current_donor] = []
    while True:
        try:
            d_num = int(input('How many donations were made: '))
            while d_num > 0:
                new_don = float(input('Enter their donation: '))
                donors[current_donor].append(new_don)
                d_num -= 1
            mail_send(current_donor)
        except (KeyboardInterrupt, EOFError, ValueError):
            break


def donor_del():
    '''
    This section allows the user to delete a donor
    '''
    try:
        donor_list()
        del_donor = str(input('Enter the name of the donor to remove: '))
        del donors[del_donor]
        donor_list()
    except (KeyboardInterrupt, EOFError, ValueError):
        safe_input()


def mail_send(current_donor):
    '''
    This function now contains both the singular and the all mails.  I am
    planning on rewriting it to print to terminal and mail for single or all.
    '''
    path = os.getcwd()

    if current_donor in donors:
        donor_math = donors[current_donor]
        directory = path + '/donors/' + current_donor + '/'
        filename = current_donor + ' - ' \
            + datetime.datetime.now().strftime('%s') + '.txt'
        mail_format(current_donor, donor_math, directory, filename)
        print('\nFile created\n')

    else:
        for k in donors:
            current_donor = k
            donor_math = donors[current_donor]
            directory = path + '/donors/' + current_donor + '/'
            filename = current_donor + ' - ' \
                + datetime.datetime.now().strftime('%s') + '.txt'
            mail_format(current_donor, donor_math, directory, filename)
        print('\nFiles created\n')


def mail_format(current_donor, donor_math, directory, filename):
    '''
    This is the formating for the mail print and file.  This allows us to
    have both files and terminal output for single donors as well as multiple
    '''
    print('\n')
    print(MAIL.format(current_donor, (sum(donor_math)), (len(donor_math))))

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(directory + filename, 'w+') as outfile:
        outfile.write('{}\n'.format(MAIL.format(current_donor,\
        (sum(donor_math)), (len(donor_math)))))


def safe_input():
    '''
    This will be for handling keyboard exceptions
    '''
    return None


def goodbye():
    '''
    Gracefully exits
    '''
    print('Goodbye!')
    sys.exit()

MENU_CHOICE = {'report': donor_report,
               'send': donor_mail_choice,
               'list': donor_list,
               'delete': donor_del,
               'quit': goodbye
               }

def main():
    '''
    The main menu and the calls to other functions.  Luis assisted me with fixing
    this, I'm leaving the old code there for a "what not to do" reference.
    The problem appears to have been the double nested while loop.
    '''
    while True:
        try:
            response = input(PROMPT)
        except (KeyboardInterrupt, EOFError):
            continue
        if response not in VALID_INPUT:
            print('\nERROR: Invalid option')
            continue
        MENU_CHOICE[response]()


if __name__ == '__main__':
    main()
