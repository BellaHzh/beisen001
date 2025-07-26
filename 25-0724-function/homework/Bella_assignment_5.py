# Part4
import digital_display
import random

# Part5


def print_number(random_number, c):
    if random_number == 0:
        digital_display.number_0(c)
    elif random_number == 1:
        digital_display.number_1(c)
    elif random_number == 2:
        digital_display.number_2(c)
    elif random_number == 3:
        digital_display.number_3(c)
    elif random_number == 4:
        digital_display.number_4(c)
    elif random_number == 5:
        digital_display.number_5(c)
    elif random_number == 6:
        digital_display.number_6(c)
    elif random_number == 7:
        digital_display.number_7(c)
    elif random_number == 8:
        digital_display.number_8(c)
    elif random_number == 9:
        digital_display.number_9(c)


def main():
    problem_number = int(input(
        "How many problems would you like to attempt? "))
    while problem_number <= 0:
        problem_number = int(
            input("Please enter a positive number.\nHow many problems would you like to attempt? "))
    print()
    c = input("What character would you like to print with? ")
    while len(c) != 1:
        c = input(
            "Please enter a single character.\nWhat character would you like to print with? ")
    print()
    print("Here we go!")
    print()
    print("What is . . .")
    print()
    success = 0
    for _ in range(problem_number):
        random_number = random.randint(0, 9)
        print_number(random_number, c)
        print()
        operation = random.choice(['+', '-'])
        if operation == '+':
            digital_display.plus(c)
        else:
            digital_display.minus(c)
        print()
        random_number_2 = random.randint(0, 9)
        print_number(random_number_2, c)
        print()
        answer = int(input("="))
        print()
        correctness = digital_display.check_answer(
            random_number, random_number_2, answer, operation)
        if correctness == True:
            success += 1
            print("Correct.")
        else:
            print("Incorrect.")
    print()
    print(f"You got {success} out of {problem_number} correct.")


main()
