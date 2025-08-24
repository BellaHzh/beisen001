# Seasons and Months Dictionary

seasons = {
    'Fall': ['September', 'October', 'November'],  # list as value of key
    'Spring': ['March', 'April', 'May']
}

# add to dictionary
seasons['Summer'] = ['June', 'July', 'August']

# new dictionary
winter_season = {'Winter': ['December', 'January', 'February']}

# merge dictionaries
seasons.update(winter_season)

print(seasons)
