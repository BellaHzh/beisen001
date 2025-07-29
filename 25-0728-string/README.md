## Assignment

Go to `assignment/` and complete all midterm reviews

[Strings](https://cs.nyu.edu/courses/spring25/CSCI-UA.0002-006/assignments/strings/)

## What we learned today

The Basics

```py
'''concatenation'''
print('bella' + 'jason')

'''repeating'''
print('bella'*30)

'''comparison'''
print('bella' == 'jason')
print('bella' == 'bella')
print('apple' < 'Apple')
print(ord('a'))
print(chr(97))
```

Indexing and Slicing

```py
a = 'heybellaandjason'

'''indexing'''
print(a[3])

'''slicing'''
print(a[:3])
print(a[0:3])
print(a[11:16])
print(a[-5:])

'''length'''
print(len(a))
```

String Methods

```py
a = 'jasonandbella'

print(a.isalpha())  # True
print(a.islower())  # True
print(a.isupper())  # F
print(a.capitalize())  # Jasonandbella
print(a.upper())  # JASONANDBELLA
print(a.lower())  # jasonandbella

s2 = 'Hey Bella What A Sunny Day!'

print(s2.swapcase())

print(s2.split(' ')[-2])
print(s2.replace(' ', '+'))
```