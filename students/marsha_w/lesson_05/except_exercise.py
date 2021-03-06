#!/usr/bin/python

"""
An exercise in playing with Exceptions.
Make lots of try/except blocks for fun and profit.
Make sure to catch specifically the error you find, rather than all errors.
"""

from except_test import fun, more_fun, last_fun


# Figure out what the exception is, catch it and while still
# in that catch block, try again with the second item in the list

first_try = ['spam', 'cheese', 'mr death']

try:
    joke = fun(first_try[0])
    joke2 = fun(first_try[1])  # this only runs if there are no exceptions
except NameError:
    print("There is a NameError! 's' is not defined")


# Here is a try/except block. Add an else that prints not_joke
try:
    not_joke = fun(first_try[2])
except NameError:
    print('Run Away!')
else:
    print('not_joke')  # this only runs when the exception is not raised


# Figure out what the exception is, catch it and in that same block
#
# try calling the more_fun function with the 2nd language in the list,
# again assigning it to more_joke.
#
# If there are no exceptions, call the more_fun function with the last
# language in the list

# Finally, while still in the try/except block and regardless of whether
# there were any exceptions, call the function last_fun with no
# parameters. (pun intended)

langs = ['java', 'c', 'python']

try:
    more_joke = more_fun(langs[1])
except IndexError:
    print('There is an IndexError:list assignment index out of range')
finally:
    last_fun()  # takes you to xkcd website
