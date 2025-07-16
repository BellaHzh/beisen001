# Write your part C here
# Part C
print("I'm thinking of a number between 1 and 10. You have three tries to guess it.")
print()
random_number = random.randint(1, 10)
guess_1 = int(input("Guess my number: "))
if guess_1 == random_number:
    print("You got it!")
    print()
elif guess_1 < random_number:
    print("Too low, try again.")
    print()
    guess_2 = int(input("Guess my number: "))
    if guess_2 == random_number:
        print("You got it!")
    elif guess_2 < random_number:
        print("Too low, try again.")
        print()
        guess_3 = int(input("Guess my number: "))
        if guess_3 == random_number:
            print("You got it!")
        else:
            print("Sorry, game over.")
    elif guess_2 > random_number:
        print("Too high, try again.")
        print()
        guess_3 = int(input("Guess my number: "))
        if guess_3 == random_number:
            print("You got it!")
        else:
            print("Sorry, game over.")
elif guess_1 > random_number:
    print("Too high, try again.")
    print()
    guess_2 = int(input("Guess my number: "))
    if guess_2 == random_number:
        print("You got it!")
    elif guess_2 < random_number:
        print("Too low, try again.")
        print()
        guess_3 = int(input("Guess my number: "))
        if guess_3 == random_number:
            print("You got it!")
        else:
            print("Sorry, game over.")
    elif guess_2 > random_number:
        print("Too high, try again.")
        print()
        guess_3 = int(input("Guess my number: "))
        if guess_3 == random_number:
            print("You got it!")
        else:
            print("Sorry, game over.")
print()
print(f"The secret number was {random_number}.")
