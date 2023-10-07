import random
generate = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("I'm thinking of a number between 1 and 10!")
guessed = False
for i in range(3):
    guess = int(input("What's your guess?"))
    if guess == generate:
        print("You got it!")
        print("The secret number was", generate)
        print("It took you", i+1, "try to guess the number.")
        guessed = True
        break
    elif guess < generate:
        print("Too low, try again.")
    elif guess > generate:
        print("Too high, try again.")
if not guessed:
    print("The secret number was", generate)
    print("You didn't guess the number.")
