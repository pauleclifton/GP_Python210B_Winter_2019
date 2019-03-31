def function_builder(n):
    functions = [lambda x, e=i: x + e for i in range(n)]
    return functions


if __name__ == '__main__':
    the_list = function_builder(4)
    for f in the_list:
        print(f(5))
