## Assignments

[Count Controlled Loops](https://cs.nyu.edu/courses/spring25/CSCI-UA.0002-006/assignments/count-controlled-loops/) 

Write a prograrm that correctly rounds a given float, no matter of its number of decimal places

## What we learned today

Basic for loop
```py
for i in range(1, 100, 2):
    print(i, end=' ')
```

Nested for loop
```py
for minutes in range(60):
    for seconds in range(60):
        print(minutes, seconds, sep=':')
        sleep(0.2)
    print()  # extra line break at each "minute"
```

How to iterate over a list
```py
gl = ['Milk', 'Egg', 'Mimo Food', 'Bananas', 'Diet Coke']

for item in gl:
    if item.startswith('M'):
        print(item)
```

...and nested
```py
gl = ['Milk', 'Egg', 'Mimo Food', 'Bananas', 'Diet Coke']

for item in gl:
    for char in item:
        print(f'{char}', end=' ')
    print()
```
```sh
M i l k 
E g g 
M i m o   F o o d 
B a n a n a s 
D i e t   C o k e 
```