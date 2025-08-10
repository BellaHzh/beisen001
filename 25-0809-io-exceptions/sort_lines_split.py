# Sorts an external file of names alphabetically using the split method
import os

# find script dir
dir = os.path.dirname(__file__)

file = open(os.path.join(dir, 'Text Files', 'names.txt'), 'r')

names = file.read()
names = names.split('\n')  # split at line breaks

file.close()
names.sort()

for name in names:
    print(name)
