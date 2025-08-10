# Read file
# This program assumes the text file is in the same directory as the Python program
import os

# find script dir
dir = os.path.dirname(__file__)

# open file
file = open(
    os.path.join(dir, 'Text Files/whitman.txt'), 'r')  # absolute path
# print(file) # print file object
beginning_my_studies = file.read()  # read the contents of the file
file.close()  # close the file object
print(beginning_my_studies)
