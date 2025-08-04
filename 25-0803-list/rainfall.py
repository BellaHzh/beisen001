days = int(input('how many days would you like to record: '))

data = [0] * days

for i in range(days):
    data_to_add = float(
        input(f'please enter rainfall in inches for day {i+1}: '))
    data[i] = data_to_add

print(data)
