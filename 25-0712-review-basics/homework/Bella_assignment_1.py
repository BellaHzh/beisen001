'''
# PartA
print("This program calculates the hypotenuse of a right-angled triangle.")
print()
side_1 = int(input("Enter the length of side 1: "))
side_2 = int(input("Enter the length of side 2: "))
print()
hypotenuse = (side_1**2+side_2**2)**0.5
print("The hypotenuse of the triangle is", format(hypotenuse, ".3f")+".")

# Part B
print("This program will project how much you can earn by investing money in a high-yield savings account over a period of four months.")
initial_value = float(input(
    "To begin, enter how much money you would like to initially invest (i.e. 500): "))
annual_interest = float(input(
    "Next, enter your projected annual interest rate. For example, enter 0.05 for 5%: "))
print()
print("Calculating . . .")
print()
interest_one_month = initial_value*(annual_interest/12)
amount_one_month = initial_value*(1+annual_interest/12)
interest_two_month = amount_one_month*(annual_interest/12)
amount_two_month = amount_one_month+interest_two_month
interest_three_month = amount_two_month*(annual_interest/12)
amount_three_month = amount_two_month+interest_three_month
interest_four_month = amount_three_month*(annual_interest/12)
amount_four_month = amount_three_month+interest_four_month
print(f"{'Month':<5}{'Starting Balance':>20}{'Interest':>15}{'Ending Balance':>20}")
initial_value_one = format(initial_value, ".2f")
interest_one_month_new = format(interest_one_month, ".2f")
amount_one_month_new = format(amount_one_month, ".2f")
interest_two_month_new = format(interest_two_month, ".2f")
amount_two_month_new = format(amount_two_month, ".2f")
interest_three_month_new = format(interest_three_month, ".2f")
amount_three_month_new = format(amount_three_month, ".2f")
interest_four_month_new = format(interest_four_month, ".2f")
amount_four_month_new = format(amount_four_month, ".2f")
print(f"{'1':>5}{initial_value_one:>20}{interest_one_month_new:>15}{amount_one_month_new:>20}")
print(f"{'2':>5}{amount_one_month_new:>20}{interest_two_month_new:>15}{amount_two_month_new:>20}")
print(f"{'3':>5}{amount_two_month_new:>20}{interest_three_month_new:>15}{amount_three_month_new:>20}")
print(f"{'4':>5}{amount_three_month_new:>20}{interest_four_month_new:>15}{amount_four_month_new:>20}")
'''