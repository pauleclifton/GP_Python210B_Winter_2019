#!/usr/bin/env python3
""" Lab to test and play with args and kwargs """

# Douglas Klos
# February 19th, 2019
# Python 210, Session 6
# args_kwargs_lab.py


def colors1(fore_color='white', back_color='white',
            link_color='white', visited_color='white'):
    """ Returns the input values """

    return(fore_color, back_color, link_color, visited_color)


def colors2(*args, **kwargs):
    """ Returns the input values with *args and **kwargs """

    return(args, kwargs)


def main():
    print(colors1())
    print(colors1('red', 'blue', 'yellow', 'chartreuse'))
    print(colors1(link_color='red', back_color='blue'))
    print(colors1('purple', link_color='red', back_color='blue'))

    color_tuple = ('light blue', 'grey')
    print(colors1(*color_tuple))

    color_dict = {'link_color': 'blue', 'visited_color': 'black'}
    print(colors1(*color_tuple, **color_dict))

    print(colors2())
    print(colors2(*color_tuple, **color_dict))

    print(colors2('red', *color_tuple, **color_dict))
    print(colors2('red', *color_tuple, 'blue', **color_dict))
    pass


if __name__ == '__main__':
    main()
