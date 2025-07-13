## Assignment
[Variables Printing](https://cs.nyu.edu/courses/spring25/CSCI-UA.0002-006/assignments/variables-printing/)

[Input Processing Output](https://cs.nyu.edu/courses/spring25/CSCI-UA.0002-006/assignments/input-processing-output/)

Plus fill in everything blank below

## What we did today
- **Variable**
  - variable types (str, int, float)
  - `type(var)`: returns the type of variable
  - type conversion (`a_string=str(an_int)` and so on)
  - first character cannot be integer
  - case sensitive
- **Print**
  - `print(f"hey {name}")`
  - `print("hey", name)`
  - `print("hey " + name)`
  - `print("Your age is " + age)` throws an error when age is an `int`. Why?
  - 🚫 No Chinese comma and quotes!!! (`“，”`)
- **Arithmitic Operations**
  - **Exercise**: What do they mean? Give an example for each
  - `+`:plus
  - `-`:minus
  - `*`:time
  - `/`:divide
  - `//`:floor division
  - `**`:exponents
  - `%`:gets the remainder
- **Input**
  - syntax: `var=input("prompt goes here")`
  - How to convert?
- **Format**
  ```py
  a = 234.56789
  formatted_a = format(a, '.2f') # leaves two decimal places
  print(formatted_a) #234.56
  ```
  Try this out yourself
  
  ***Reminder: Format turns the float above into str***
- **Error**
  - We briefly went over try catch
  - see src `hello.py` for syntax and use cases

## Bella's Notes
variable=value

integer

floats: 0.3

string: name=’bella’ (string要加引号)

type(variable)

astring_as_int=int(astring):转换

aint_as_str=str(int)

print(’hello world’)>>>hello world

age=22

print(f’age is: {age}’)>>.age is 22

print(f’{age} is: {age}’)>>22 is 22

print(’age is’, age)>>age is 22

print(’age is’+str(age))>>age is22

“，”可以自动create空格

//: 26//5>>5 floor division

%:26//5>>1 remainder

**: 指数 2**5>>32

age=input(”What’s your age”)>>What’s your age

age=input(’What\’s your age’)>>What’s your age

variable 第一位不能是数字

variable is case sensitive: Person1不等于person1

‘’‘comments’‘’

f1=234.567899

formatted_f1=format(f1,’.2f’)>>>234.56 变成了str

*Following notes from [Prof Joshua Clayton](https://cs.nyu.edu/courses/spring25/CSCI-UA.0002-006/notes/)*


