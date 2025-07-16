
# Part A
print("NYC Screen Printing")
print()
number_of_shirts = int(
    input("How many T-shirts would you like to have printed? "))
color = int(
    input("How many colors will each shirt be printed with (1, 2, or 3)? "))
print()
if color == 1:
    if 1 <= number_of_shirts <= 99:
        shirts_price = (number_of_shirts*9)*1.08875
    elif 100 <= number_of_shirts <= 249:
        shirts_price = (number_of_shirts*8)*1.08875
    elif number_of_shirts >= 250:
        shirts_price = (number_of_shirts*7)*1.08875
elif color == 2:
    if 1 <= number_of_shirts <= 99:
        shirts_price = (number_of_shirts*10)*1.08875
    elif 100 <= number_of_shirts <= 249:
        shirts_price = (number_of_shirts*9)*1.08875
    elif number_of_shirts >= 250:
        shirts_price = (number_of_shirts*8)*1.08875
elif color == 3:
    if 1 <= number_of_shirts <= 99:
        shirts_price = (number_of_shirts*11)*1.08875
    elif 100 <= number_of_shirts <= 249:
        shirts_price = (number_of_shirts*10)*1.08875
    elif number_of_shirts >= 250:
        shirts_price = (number_of_shirts*9)*1.08875
shirts_price_new = format(shirts_price, ".2f")
print(f"{number_of_shirts} shirts printed with 3 colors: ${shirts_price_new}")

# Part B
print("In the quiet hours just after dawn, you wander the city streets. Passing by a favorite café, you stroll at an unhurried pace without any particular destination. As you continue along a familiar route you notice, for the first time, an open staircase along the side of a building that leads upward and inward.")
print()
first_choice = input("Would you like to climb the stairs? (yes/no): ")
print()
if first_choice == "yes":
    print("You climb the stairs with ease in the cool of the morning. The view along the way is not so much impressive as it is unique to your perspective on the neighborhood. As you reach the top of the stairs, you find a group of cats gathered on the roof in the midst of what appears to be a cat ceremony. Wordlessly, an old man suddenly appears and gives you a cushion.")
    print()
    second_choice = input(
        "Would you like to sit with the group or watch from far away? (sit/watch): ")
    print()
    if second_choice == "sit":
        print("You approach the group quietly and several turn with curious looks on their faces, giving you pause. That's scary, you want to run away.")
        print()
        third_choice = input(
            "Would you like to sit with the cats or run away? (sit/run):")
        print()
        if third_choice == 'sit':
            print("OK. That's it. I don't want to write this story anymore!!!")
        else:
            print("NOOOO MOREEEE Stories!!!! TIREDDDDD")
    elif second_choice == "watch":
        print("The old man gives you an angry glimpse, and he walked towards the cat group with his arms open. Then he says 'My dearest meow meow army. We are now in a tough situation! Mimo, our cat country's prince, is getting tired of helping his owner creating the stupid stories. Shall we help him?' The cats respond positively.The cats jump up and shout 'save the prince!'They run down the stairs to the street. You notice each of them has a little bag on their back. Ah! That must be the weapon, you think.")
        print()
        third_choice = input("Do you want to follow them? (yes/no): ")
        print()
        if third_choice == "yes":
            print("You follow them to run on the street. They suddenly stop infront of a girl, who looks struggled and has a laptop on her legs. The cats take something out of their pocket. You are too nervous to stop them. However, you see each of them is holding a cat toy and meow at the girl. The girl plays with them and feeds them. What a happy picture!")
        else:
            print("You walk away and think you must be crazy. This must be your dream.")
else:
    print("You walk by the stairs. Suddenly, you hear a voice calling you to wait a moment. You notice it was from an old man came out from the staircase. He has a black cat in his arm. It seems he wants to give the cat to you.")
    print()
    second_choice = input(
        "Would you like to accept the cat or ignore him? (accept/ignore): ")
    print()
    if second_choice == "accept":
        print("The old man gives you the cat, and he tells you that the cat is a magical cat called Mimo. He smiled at you weirdly and disappeared with a crowd of people.")
        print()
        third_choice = input(
            "Would you like to call the cat's name? (yes/no): ")
        print()
        if third_choice == "yes":
            print("The cat answers with a delightful voice 'Meow?' and says 'if you buy me ten purina wet food, I can warm your bed every day. Plus, you can collect my fur and make scarfs to sell. I will help you to become the richest business man in the world.'")
        else:
            print("The cat is so nervous. He screams and shows his little white teeth. Suddently, he says 'can you send me back home? I was kidnapped by that old man. I live in Jersey City, can you send me to my parents? They can pay you, I promise. Plzzzzz'")
    else:
        print("The old man says 'you will miss the greatest creature in the world. He then approaches to a girl and ask her instead. You notice she is your girlfriend, Isabella.")
        print()
        third_choice = input("Do you want Isabella accept the cat? (yes/no): ")
        if third_choice == 'yes':
            print("You get Mimo! The old man can never know that you are a couple. Ahah!")
        else:
            print("Mimo runs away. He is so angry. How can you let him go! Get him back!")
