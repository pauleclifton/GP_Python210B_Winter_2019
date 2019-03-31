#!/usr/bin/env python3
#pylint: disable=C0103

# Douglas Klos
# March 7th, 2019
# Python 210, Extra
# run_timer_context.py

""" Run file for context manager testing """

import io
import time
from contextlib import contextmanager
import timer_context as tc


@contextmanager
def local_timer(out_file, name=''):
    """ Context manager that returns execution time """
    local_time = time.time()
    try:
        yield local_time
    finally:
        local_time = time.time() - local_time
        out_file.write(f'{name} execution took {local_time} seconds')


def timer_test():
    """ Runs a loop with context manager and prints execution time """
    outfile = io.StringIO()

    with tc.Timer(outfile, 'timer_test'):
        for i in range(1000000):
            i = i ** 20

    print(outfile.getvalue())


def timer_test2():
    """ Runs a loop with context manager and prints execution time """
    outfile = io.StringIO()

    with local_timer(outfile, 'timer_test2'):
        for i in range(1000000):
            i = i ** 20

    print(outfile.getvalue())


def main():
    """ Main, calls different tests """
    timer_test()
    timer_test2()


if __name__ == '__main__':
    main()
