#!/usr/bin/env python3



# def get_non_negative(x=int(input('Please enter a postive number'))):
#     while x < 1:
#         x = int(input('Please enter a postive number'))
#     return x
#
# print(get_non_negative())

def get_non_negative(text, test):
    while True:
        try:
            value = test(int(input(text)))
            return value
        except ValueError:
            print('Problem')
            continue

print(get_non_negative('Enter a pos amount', ))

# def get_value(text, check_type):
#     """
#     Catch non-numeric entries for donation amount.
#     """
#     while True:
#         try:
#             value = check_type(input(text))
#             return value
#         except ValueError:
#             print("Invalid value.  Please try again")
#             continue


