# Part1
def horizontal_line(c):
    print(c*5)


def vertical_line(c, s, h):
    for _ in range(h):
        print(" "*s+c)


def two_vertical_lines(c, h):
    for _ in range(h):
        print(c+" "*3+c)

# Part2


def number_0(c):
    print(c*5)
    two_vertical_lines(c, 3)
    print(c*5)


def number_1(c):
    vertical_line(c, 4, 5)


def number_2(c):
    print(c*5)
    vertical_line(c, 4, 1)
    print(c*5)
    vertical_line(c, 0, 1)
    print(c*5)


def number_3(c):
    print(c*5)
    vertical_line(c, 4, 1)
    print(c*5)
    vertical_line(c, 4, 1)
    print(c*5)


def number_4(c):
    two_vertical_lines(c, 2)
    print(c*5)
    vertical_line(c, 4, 2)


def number_5(c):
    print(c*5)
    vertical_line(c, 0, 1)
    print(c*5)
    vertical_line(c, 4, 1)
    print(c*5)


def number_6(c):
    print(c*5)
    vertical_line(c, 0, 1)
    print(c*5)
    two_vertical_lines(c, 1)
    print(c*5)


def number_7(c):
    print(c*5)
    vertical_line(c, 4, 4)


def number_8(c):
    print(c*5)
    two_vertical_lines(c, 1)
    print(c*5)
    two_vertical_lines(c, 1)
    print(c*5)


def number_9(c):
    print(c*5)
    two_vertical_lines(c, 1)
    print(c*5)
    vertical_line(c, 4, 2)


def plus(c):
    vertical_line(c, 2, 2)
    print(c*5)
    vertical_line(c, 2, 2)


def minus(c):
    horizontal_line(c)

# Part3


def check_answer(num_1, num_2, ans, op):
    if op == "+":
        if num_1+num_2 == ans:
            return True
        else:
            return False
    elif op == "-":
        if num_1-num_2 == ans:
            return True
        else:
            return False
