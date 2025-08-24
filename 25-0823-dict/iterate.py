# Seasons and Months Dictionary Iteration

# Object, Dict, Hash Map (KV pair)
seasons = {
    'Spring': ['March', 'April', 'May'],
    'Summer': ['June', 'July', 'August'],
    'Fall': ['September', 'October', 'November'],
    'Winter': ['December', 'January', 'February']
}

# access keys individually
# [k1, k2, k3]
for key in seasons.keys():  # or for key in seasons:
    print(key)

print()

# access values individually
# [v1, v2, v3]
for value in seasons.values():
    print(value)

print()

# access keys and values individually
# [[k1,v1],[k2,v2],[k3,v3]]
for key, value in seasons.items():
    print(key, value)

print()

# access keys and values individually . . .
'''
Spring: March April May
Summer: ...
'''
for key, value in seasons.items():
    print(f'{key}:', end=' ')
    # and access individual items of each value
    for month in value:
        print(month, end=' ')
    print()
