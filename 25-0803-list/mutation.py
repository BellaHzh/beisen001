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
