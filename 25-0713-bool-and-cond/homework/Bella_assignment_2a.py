
# Part A
print("NYC Screen Printing")
print()
number_of_shirts = int(
    input("How many T-shirts would you like to have printed? "))
color = int(
    input("How many colors will each shirt be printed with (1, 2, or 3)? "))
print()
if color == 1:
    if 1 <= number_of_shirts <= 99:
        shirts_price = (number_of_shirts*9)*1.08875
    elif 100 <= number_of_shirts <= 249:
        shirts_price = (number_of_shirts*8)*1.08875
    elif number_of_shirts >= 250:
        shirts_price = (number_of_shirts*7)*1.08875
elif color == 2:
    if 1 <= number_of_shirts <= 99:
        shirts_price = (number_of_shirts*10)*1.08875
    elif 100 <= number_of_shirts <= 249:
        shirts_price = (number_of_shirts*9)*1.08875
    elif number_of_shirts >= 250:
        shirts_price = (number_of_shirts*8)*1.08875
elif color == 3:
    if 1 <= number_of_shirts <= 99:
        shirts_price = (number_of_shirts*11)*1.08875
    elif 100 <= number_of_shirts <= 249:
        shirts_price = (number_of_shirts*10)*1.08875
    elif number_of_shirts >= 250:
        shirts_price = (number_of_shirts*9)*1.08875
shirts_price_new = format(shirts_price, ".2f")
print(f"{number_of_shirts} shirts printed with 3 colors: ${shirts_price_new}")
