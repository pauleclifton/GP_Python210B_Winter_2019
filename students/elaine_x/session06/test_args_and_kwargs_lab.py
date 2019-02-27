'''
##########################
#Python 210
#Session 06 - Args and Kwargs Lab
#Elaine Xu
#Feb 20,2019
###########################
'''
'''Keyword arguments:

Write a function that has four optional parameters (with defaults):
fore_color
back_color
link_color
visited_color

1. Have it return the colors (use strings for the colors, e.g. “blue”, “red”, etc.)

Call it with a couple different parameters set. That is, write tests that verify that all of the following
work as advertised:
2. Using just positional arguments:
func('red', 'blue', 'yellow', 'chartreuse')
3. Using just keyword arguments:
func(link_color='red', back_color='blue')
4. using a combination of positional and keyword
``func('purple', link_color='red', back_color='blue')
5. using *some_tuple and/or **some_dict
regular = ('red', 'blue')
links = {'link_color': 'chartreuse'}
func(*regular, **links)
'''
#you can change this import to test different versions
from args_and_kwargs_lab import args_and_kwargs

def test_1():
    assert args_and_kwargs() == ('blue', 'red', 'white', 'black')

def test_2():
    assert args_and_kwargs('red', 'blue', 'yellow', 'chartreuse') == ('red', 'blue', 'yellow', 'chartreuse')

def test_3():
    assert args_and_kwargs(link_color = 'red', back_color = 'blue') == ('blue', 'blue', 'red', 'black')

def test_4():
    assert args_and_kwargs('purple', link_color = 'red', back_color = 'blue') == ('purple', 'blue', 'red', 'black')

def test_5():
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    assert args_and_kwargs(*regular, **links) == ('red', 'blue', 'chartreuse', 'black')

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
from args_and_kwargs_lab import new_args_and_kwargs

def test_6():
    #assert new_args_and_kwargs('blue', 'red', 'white', 'black') == ('blue', 'red', 'white', 'black')
    #new_args_and_kwargs('blue', 'red', 'white', 'black')
    new_args_and_kwargs()
    print()

def test_7():
    #assert args_and_kwargs('red', 'blue', 'yellow', 'chartreuse') == ('red', 'blue', 'yellow', 'chartreuse')
    new_args_and_kwargs('red', 'blue', 'yellow', 'chartreuse')
    print()

def test_8():
    #assert args_and_kwargs(link_color = 'red', back_color = 'blue') == ('blue', 'blue', 'red', 'black')
    new_args_and_kwargs(link_color = 'red', back_color = 'blue')
    print()

def test_9():
    #assert args_and_kwargs('purple', link_color = 'red', back_color = 'blue') == ('purple', 'blue', 'red', 'black')
    new_args_and_kwargs('purple', link_color='red', back_color='blue')
    print()


def test_10():
    regular = ('red', 'blue')
    links = {'link_color': 'chartreuse'}
    #assert args_and_kwargs(*regular, **links) == ('red', 'blue', 'chartreuse', 'black')
    new_args_and_kwargs(*regular, **links)

print('test 6')
test_6()

print('test 7')
test_7()

print('test 8')
test_8()

print('test 9')
test_9()

print('test 10')
test_10()
