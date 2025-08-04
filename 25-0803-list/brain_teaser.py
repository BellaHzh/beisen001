# 1
x = 'abcde12345'
y = [[20, 17], 82, [32, 4, 33], [16, 90], 47]
print(y[int(x[6])][2])

# 33

# 2
# What will be the output of the following?


def add_character(string, character):
    string += character


letters = 'AB'
add_character(letters, 'C')
print(letters)

print()


def add_item(lst, item):
    lst.append(item)


numbers = [1, 2]
add_item(numbers, 3)
print(numbers)
