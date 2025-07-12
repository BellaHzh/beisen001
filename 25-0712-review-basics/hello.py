# ----PRINT----

# print('hello world')  # most basic

# age = 22

# print(f'{age} is: {age}')

# print('age is ', str(age))

# ----INPUT----

# age = input("What\'s your age? ")

# print(f"Hello {age}-year-old person!")


# ----VAIRIABLE NAMING----
# Person1 = "jason"
# person1 = "bella"

# print(person1, Person1)


# ----FORMATTING----
# f1 = 234.23456789

# formatted_f1 = format(f1, '.2f')

# print(f1, formatted_f1)
# print(type(formatted_f1))

# ----ERROR-----

# age = int(input('What is your age'))
# bmn = age//12
# print("You have had", bmn, "本命年")

# try:
#     number_of_eggs = int(input("How many eggs did you buy"))
#     money = float(input("How much money did you spend"))
#     average_cost = money/number_of_eggs
#     formatted_cost = format(average_cost, '.2f')
#     print(f"The average cost of the eggs is {formatted_cost}")
# except ZeroDivisionError:
#     print('Asshole! Cannot buy 0 eggs!')
# except ValueError:
#     print("Cannot enter non-numbers!")
