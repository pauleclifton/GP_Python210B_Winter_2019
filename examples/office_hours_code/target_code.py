def get_value(text, check_type):
    while True:
        try:
            value = check_type(input(text))
            return value
        except ValueError:
            return "Invalid value.  Please try again"