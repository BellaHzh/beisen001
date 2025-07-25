## Assignment

[Functions](https://cs.nyu.edu/courses/spring25/CSCI-UA.0002-006/assignments/functions-module/)

## What we learned today

Local Variables
```py
def c_to_f(c):
    return (c * 9/5) + 32

f = c_to_f(45)

print(c) # c is not defined here
```

Local vs. Global
```py
radius = 5  # global variable


def area():
    import math
    area = math.pi * radius ** 2  # local variable
    return area


def change_radius(new_radius):
    global radius
    radius = new_radius


print(area())
change_radius(10)
print(area())
```

Default parameters and choose
```py
def add(a=2, b=1, c=20):
    return a + b + c


print(add())
print(add(1))  # only a
print(add(b=1, c=10))  # choose which ones to define
```

Multiple return values
```py
# Multiple Return Values

def get_name():
    first = input('What is your first name? ')
    last = input('What is your last name? ')
    return first, last


def main():
    first_name, last_name = get_name()  # multiple assignment statement
    print('Hello,', first_name, last_name)


main()
```