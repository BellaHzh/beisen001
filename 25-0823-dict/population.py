# City Population Data

population_data = {
    'New York': 8258035,
    'Los Angeles': 3820914,
    'Chicago': 2664452
}


def main():
    city = input('Enter the city you want the population of: ').title()

    while not (city in population_data):  # or (city in population_data) != True
        city = input('No data available. Please try another city: ').title()

    population = population_data[city]  # or population_data.get(city)

    print(f'The population of {city} is: {population:,}')


main()
