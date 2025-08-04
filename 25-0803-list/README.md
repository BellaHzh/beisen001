## Assignments

Look through [list methods](https://cs.nyu.edu/courses/spring25/CSCI-UA.0002-006/notes/list-methods/)

[Fun airport system hw on list](https://cs.nyu.edu/courses/spring25/CSCI-UA.0002-006/assignments/lists/)

## What we learned

indexing
```py
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']

print(colors)
print(len(colors))
print(colors[4])
print(colors[1:5])
print(colors[-3:])
print(colors * 2)
```

mutation
```py
# Color List Mutation

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']

# mutate a single item
colors[2] = 'purple'
print(colors)

# concat
precious_colors = ['silver', 'bronze', 'gold']

colors = colors + precious_colors
print(colors)

# concat part

groceries = ['milk', 'bread', 'juice', 'lettuce']
groceries[2] = 'orange juice'
ingredients = ['sugar', 'eggs', 'vanilla']
new_list = groceries[0:2] + [ingredients[-1]]
print(new_list)
```

methods
```py
shapes = ['square', 'sqaure', 'circle']

# Append - add to the end of list
# shapes += ['triangle']
# shapes.append('triangle')
# print(shapes)

# Insert - add to specified index of list
# shapes.insert(1, 'triangle')
# print(shapes)

# Remove - remove element from list
# shapes.remove('square')
# print(shapes)

# Index - returns index of an element within list (first occurance)
# print(shapes.index('square'))

# del = remove
# del shapes[1]
# print(shapes)
```