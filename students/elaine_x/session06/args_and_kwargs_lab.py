'''
##########################
#Python 210
#Session 06 - Args and Kwargs Lab
#Elaine Xu
#Feb 20,2019
###########################
'''
'''
We are going to do this as test driven development: Your first task for each step below is to write a test
that will ensure your code does what we are telling you it should do.

Keyword arguments:

Write a function that has four optional parameters (with defaults):
fore_color
back_color
link_color
visited_color

Have it return the colors (use strings for the colors, e.g. “blue”, “red”, etc.)
Call it with a couple different parameters set. That is, write tests that verify that all of the following
work as advertised:
Using just positional arguments:
func('red', 'blue', 'yellow', 'chartreuse')
Using just keyword arguments:
func(link_color='red', back_color='blue')
using a combination of positional and keyword
``func('purple', link_color='red', back_color='blue')
using *some_tuple and/or **some_dict
regular = ('red', 'blue')
links = {'link_color': 'chartreuse'}
func(*regular, **links)
'''
def args_and_kwargs(fore_color = 'blue', back_color = 'red', link_color = 'white', visited_color = 'black'):
    return fore_color, back_color, link_color, visited_color


'''
Generic parameters:

Write a new function with the parameters as:
*args and **kwargs

Have it return the colors (use strings for the colors again)
Call it with the same various combinations of arguments used above.
Also have it print args and kwargs directly, so you can be sure you understand what’s going on.
Note that in general, you can’t know what will get passed into **kwargs So maybe adapt your function 
to be able to do something reasonable with any keywords.
'''
'''
def new_args_and_kwargs(*args, fore_color = 'blue', back_color = 'red', link_color = 'white',
                        visited_color = 'black', **kwargs):
    print('the positional arguments are: ', args)
    print('the keyword arguments are: ', kwargs)
    print(fore_color, back_color, link_color, visited_color)
    return fore_color, back_color, link_color, visited_color
'''

def new_args_and_kwargs(*args, **kwargs):
    print('the positional arguments are: ', args)
    print('the keyword arguments are: ', kwargs)

