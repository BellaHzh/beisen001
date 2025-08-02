import random
import string

# Function to Add Letters


def add_letters(word, num):
    new_word = ""
    for c in word:
        added_letters = ""
        for i in range(num):
            random_number_1 = random.randint(65, 90)
            random_number_2 = random.randint(65, 90)
            random_number = random.choice([random_number_1, random_number_2])
            random_letter = chr(random_number)
            added_letters += random_letter
        new_word += c+added_letters
    return new_word

# Function to Remove Letter


def remove_letters(word, num):
    new_word = ""
    for i in range(0, len(word), num+1):
        new_word += word[i]
    return new_word

# Function to Shift Characters


def shift_characters(word, num):
    new_word = ""
    for c in word:
        number = ord(c)
        new_number = number+num
        new_character = chr(new_number)
        new_word += new_character
    return new_word


def main():
    print("Secret Message Encoder/Decoder")
    print()
    while True:
        choice = input("(e)ncode, (d)ecode or (q)uit: ")
        if choice == "q":
            break
        while choice not in ["e", "d", "q"]:
            choice = input("(e)ncode, (d)ecode or (q)uit: ")

        num = int(input("Enter a number between 1 and 5: "))
        while num <= 0 or num > 5:
            num = int(input("Enter a number between 1 and 5: "))
        word = input("Enter a phrase to encode: ")
        if choice == "e":
            word_added = add_letters(word, num)
            word_encoded = shift_characters(word_added, num)
            print(f"Your encoded word is: {word_encoded}")
        elif choice == "d":
            word_deleted = remove_letters(word, num)
            shift_number = num*-1
            word_decoded = shift_characters(word_deleted, shift_number)
            print(f"Your decoded word is: {word_decoded}")
        print()


main()
