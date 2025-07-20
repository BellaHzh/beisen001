from time import sleep
# Hour Timer

# for i in range(20):
#     print(i, end=' ')

for minutes in range(60):
    for seconds in range(60):
        print(minutes, seconds, sep=':')
        sleep(0.2)
    print()  # extra line break at each "minute"
