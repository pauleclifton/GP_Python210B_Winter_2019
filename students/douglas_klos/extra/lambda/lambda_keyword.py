#!/usr/bin/env python3

# Douglas Klos
# March 6th, 2019
# Python 210, Extra
# lambda_keyword.py


def function_builder(value):

    # This is the working line with list comprehension
    # return [(lambda y: (lambda x: y + x))(i) for i in (range(value))]

    # This is the working multiline
    return_list = []
    for i in range(value):
        return_list.append((lambda y: (lambda x: y + x))(i))
    return return_list

    # These were the failures that look like they should work

    # return_list = []
    # for i in range(value):
    #     print(i)
    #     return_list.append(lambda x: x + i)
    # return return_list

    # return [lambda x: x+i for i in range(value)]


def main():

    func_list = function_builder(10)

    print(func_list[0](0))
    print(func_list[1](0))
    print(func_list[2](0))
    print(func_list[3](0))
    print(func_list[4](0))

if __name__ == '__main__':
    main()