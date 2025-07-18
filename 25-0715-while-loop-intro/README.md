## Assignments

[cond controlled loops](https://cs.nyu.edu/courses/spring25/CSCI-UA.0002-006/assignments/condition-controlled-loops/)

fill in the blanks below for `#a-d`

## What we learned today

### While loop aka Condition-controlled Loops (infinite and controlled)
```py
#infinite loop
while x > 0:
    print(x, i)
    i += 1
    sleep(0.1)

while 1 == 2:
    print('1 == 2')

while False:
    print('False!')
    sleep(1)

while True:
    print('True!')
    sleep(1)
```
```py
# controlled loop
while x > 0:
    x -= 1  # x = x - 1
    print(x)
    sleep(1)
```
How will the code below behave?
```py
# a
while 1 != 2:
  print('1 != 2')

# b
while not 1 != 2:
  print('not 1 != 2')

# c
while not False:
  print('not false')

# d
while not 'jason' != 'bella':
  print('not jason != bella')
```

