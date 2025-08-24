# Basics

birth_year = {'John': 1968, 'Mary': 1984, 'Lin': 2002,
              'Adib': 1978, 'Isabella': 2002, 'Jason': 2002}  # key value pair
print(birth_year)

number_of_items = len(birth_year)
print(number_of_items)

a = birth_year['Adib']  # access value by key
print(a)

birth_year['Mary'] = 1985  # modify value of key

m = birth_year['Mary']
print(m)
