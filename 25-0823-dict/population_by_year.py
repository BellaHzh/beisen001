# City Population Data by Year

population_data = {
    'New York': {
        2017: 8437478,
        2018: 8390081,
        2019: 8336817
    },
    'Los Angeles': {
        2017: 3975788,
        2018: 3977596,
        2019: 3979576,
    },
    'Chicago': {
        2017: 2711069,
        2018: 2701423,
        2019: 2693976
    }
}


def main():
    get_data = 'yes'

    while get_data == 'yes':
        city = input('Enter the city you want the population of: ').title()

        while not (city in population_data):
            city = input(
                'No data available. Please try another city: ').title()

        while True:
            year = input('Enter the year you want this data for: ')
            try:
                year = int(year)
            except:
                print('Please enter the year numerically.')
            else:
                if year in population_data[city]:
                    break
                else:
                    print('No data available. Please try another year.')

        population = population_data[city][year]
        print(f'The population of {city} in {year} was: {population:,}')

        print()
        get_data = input('Would you like to continue? (yes/no) ').lower()


main()
