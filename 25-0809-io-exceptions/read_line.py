# Print the individual lines of a file

import os
# find script dir
dir = os.path.dirname(__file__)

file_name = input('Enter a file name: ')
file = open(os.path.join(dir, 'Text Files', file_name), 'r')
for line in file:
    print(line, end='')
file.close()  # best practice
