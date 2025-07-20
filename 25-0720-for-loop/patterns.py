# Square pattern with nested loop
from time import sleep

for row in range(10):
    for col in range(10):
        print('+', end=' ')
    print()  # line break as part of "row" loop
    sleep(0.5)

# Triangle pattern with nested loop

for row in range(10):
    for col in range(row + 1):
        print('+', end=' ')
    print()  # line break as part of "row" loop
    sleep(0.5)
