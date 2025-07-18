from time import sleep

base = float(input('how much do you wanna invest: '))
apr = float(input('input rate as a float (0.05): '))
years = float(input('how many years: '))

i = 1

while i <= years:
    base *= (1 + apr)
    print(f'after year {i}, you now got {format(base, '.2f')}')
    i += 1
    sleep(1)

print(f'OK, you got {base} in the end')
