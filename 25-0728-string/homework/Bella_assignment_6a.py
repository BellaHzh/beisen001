import keyword
a = input("Enter your Python variable name: ")


def valid(a):
    if a[0] in '0123456789':
        return False
    elif a.isupper():
        return False
    elif keyword.iskeyword(a):
        return False
    else:
        for c in a:
            if not (c == "_" or c.isalpha()):
                return False
            else:
                return True


if valid(a) == True:
    print("This is a valid variable name.")
else:
    print("This is not a valid varibale name.")
