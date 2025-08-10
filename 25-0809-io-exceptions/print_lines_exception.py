# Print the lines of a file with exception handling

file_name = input('Enter a file name: ')
try:
    file = open(file_name, 'r')
except FileNotFoundError:
    print('File not found.')
except:
    print('There was a problem opening the file.')
else:
    contents = file.read()
    print(contents)
    file.close()
