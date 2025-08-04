# Rainfall Data with Unit Conversion, Min and Max Value

def inches_to_cm(inches):
    '''
    Takes a value in inches and converts it to centimeters.
    Returns the value in cm.
    '''
    cm = inches * 2.54
    return cm


def main():
    days = int(
        input('How many days of rainfall would you like to enter data for? '))
    print()

    rainfall_inches = [0] * days  # create a list with 0 values for each day

    for day in range(days):  # loop will repeat number of days input
        rain_data = float(input(f'Enter rainfall for day {day + 1}: '))
        # replace data in current index position
        rainfall_inches[day] = rain_data

    print()
    print('Rainfall in inches:')

    for rainfall in rainfall_inches:  # access individual items in list
        print(rainfall, 'inches')

    rainfall_cm = []  # initialize empty list

    for data in rainfall_inches:
        cm_data = inches_to_cm(data)
        rainfall_cm.append(cm_data)  # or, rainfall_cm += [cm_data]

    print()
    print('Rainfall in centimeters:')

    for rainfall in rainfall_cm:
        print(rainfall, 'centimeters')


main()
