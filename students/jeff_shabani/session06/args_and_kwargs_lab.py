#!/usr/bin/env python3


def colors(fore_color='white', back_color='black', link_color='green', visited_color='blue'):
    """
    this is the 1st function for the first part
    of the args & kwargs lab
    """
    return fore_color, back_color, link_color, visited_color


def colors_two(*args, **kwargs):
    """
    this is the 2nd function for the first part
    of the args & kwargs lab
    """
    if args:
        if not kwargs:
            return (args)
        else:
            return (args, kwargs)
    else:
        return (kwargs)


if __name__ == '__main__':
    colors()
    colors_two()
