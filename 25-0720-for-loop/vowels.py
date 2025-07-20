# vowels: a,e,i,o,u
# Jason -> 2 ; Bella -> 2

s = input("Enter a string: ")
i = 0

for c in s:
    if c in 'aeiou':
        i += 1

print(f'There are {i} vowels in {s}')
