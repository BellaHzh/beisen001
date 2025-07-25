# Multiple Return Values

def get_name():
    first = input('What is your first name? ')
    last = input('What is your last name? ')
    return first, last


def main():
    first_name, last_name = get_name()  # multiple assignment statement
    print('Hello,', first_name, last_name)


main()
