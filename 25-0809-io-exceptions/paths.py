# File Paths with OS Module

# import operating system module
import os

# get current working directory
cwd = os.getcwd()
print(cwd)

print()

# list files in the cwd
files = os.listdir()
print('All files:', files)

print()

# check for file
print(os.path.isfile('republic.txt'))  # is there a file of this name here?

# create a new directory
# os.mkdir('Text Files')

# change to subdirectory
os.chdir('Text Files')

# change to parent directory
os.chdir('..')

print(os.getcwd())
print(os.listdir())
