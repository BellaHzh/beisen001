# Write or append to text file

import os


def write_file(file_name, content):
    file = open(file_name, 'w')
    file.write(content)
    file.close()


def append_file(file_name, content):
    file = open(file_name, 'a')
    file.write('\n')
    file.write(content)
    file.close()


def main():
    file_name = input('Enter file name: ')
    content = input('Enter file text: ')

    if os.path.isfile(file_name):  # check if file already exists
        overwrite = input(
            'This file already exists. Overwrite? (yes/no) ').lower()
        if overwrite == 'yes' or overwrite == 'y':
            write_file(file_name, content)
            print('File written.')
        else:
            append_file(file_name, content)
            print('Ok. File added to.')
    else:
        write_file(file_name, content)
        print('File written.')


main()
