# a = 'hello'

# print(a)

# s = '20'
# int(s)

# def add1(a):
#     # return a + 1

# b = add1(20)

# print(b)

# LOCAL VARIABLES

# def c_to_f(c):
#     bella = 'jason'
#     return (c * 9/5) + 32


# f = c_to_f(45)

# print(bella)


# PARAMETERS

def add(a=2, b=1, c=20):
    return a + b + c


print(add())
print(add(1))  # only a
print(add(b=1, c=10))  # choose which ones to define
