calculat_tip = 'yes'

while calculat_tip == 'yes':
    total = float(input('How much did you spend today: '))
    tip_percent = float(
        input('How much do you wanna tip (in float such as 0.01): '))
    print(f'ok your grand total is {total * (1 + tip_percent)}')
    calculat_tip = input('Continue? (yes or no): ')
    print()
