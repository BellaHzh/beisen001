# Sorts an external file of names alphabetically
import os

# find script dir
dir = os.path.dirname(__file__)


file = open(os.path.join(dir, 'Text Files', 'names.txt'), 'r')

names = []  # create an empty list

for line in file:
    line = line.strip()  # remove any extra whitespace characters
    names.append(line)

file.close()
names.sort()

for name in names:
    print(name)
