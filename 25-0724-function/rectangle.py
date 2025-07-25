'''
*********
*       *
*       *
*       *
*********
'''


def edge():
    print("*********")


def side():
    print('*       *')


height = int(input('How high? '))

edge()

for i in range(height):
    side()

edge()
