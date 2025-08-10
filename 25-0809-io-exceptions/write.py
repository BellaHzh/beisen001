# Write to text file

def write_file(file_name, content):
    file = open(file_name, 'w')
    file.write(content)
    file.close()


def main():
    file_name = input('Enter the file name: ')
    content = input('Enter the file text: ')
    write_file(file_name, content)
    print('File written.')


main()
