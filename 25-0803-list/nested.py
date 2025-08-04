# Nested Dice Roll List

import random


def main():
    all_rolls = []

    for roll in range(10):
        dice_roll = []
        die_1 = random.randint(1, 6)  # first dice
        dice_roll.append(die_1)
        die_2 = random.randint(1, 6)  # second dice
        dice_roll.append(die_2)
        all_rolls.append(dice_roll)  # [1,2]

    print(all_rolls)  # [[1,2], [2,3], [4,4]]

    # Access all items in nested list with nested loop and print each die roll
    print()

    for dice in all_rolls:
        for die in dice:
            print(die, end=' ')
        print()

    # Access all items in nested list and print sum of dice pair
    print()

    for dice in all_rolls:
        total = 0
        for die in dice:
            total += die
        print(total)


main()
