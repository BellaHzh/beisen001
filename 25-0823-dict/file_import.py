# Dictionary from CSV Text File

def main():
    try:
        text_file = open('most-populous.txt', 'r')
    except:
        print('That file is not available.')
    else:
        cities = text_file.read()
        text_file.close()

        population_data = {}

        data = cities.split('\n')

        for city in data:
            city = city.split(',')  # ["New York", "8258035"]
            population_data[city[0]] = int(city[1])

        print('Population Data')
        print()

        for key, value in population_data.items():
            print(f'{key:<14} {value:>10,}')


main()
