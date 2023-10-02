print("This program will project how much you can earn by investing \n money in a high-yield savings account over a 3 month period.")
print("")
invest = int(input(
    "To begin, enter how much money you would like\nto initially invest (i.e. 500): "))
interest = int(input(
    "Next, enter your projected aual interest rate.\n For example, enter 5 for 5%:"))
print("")
print("------------------- Calculating ---------------------")
print("")
print(f"{'Month' : <8}{'Starting Balance': <20}{'Interest' : <10}{'Ending Balance' : <25}")
interest1 = invest*(interest/100)/12
ending1 = invest+interest1
interest2 = ending1*(interest/100)/12
ending2 = ending1+interest2
interest3 = ending2*(interest/100)/12
ending3 = ending2+interest2

# This is way to complicated and repetitive, there are easiser ways of doing this (see below), and you did not include the attributes for the interest part, as it is showing nothing.
# print(format("1", "<10s"), format(round(invest, 2), "<10f"), format(
#     round(interest1, 2), "<30f"), format(round(ending1, 2), "<20f"))
# print(format("2", "<10s"), format(round(ending1, 2), "<10f"), format(
#     round(interest2, 2), "<30f"), format(round(ending2, 2), "<20f"))
# print(format("3", "<10s"), format(round(ending2, 2), "<10f"), format(
#     round(interest3, 2), "<30f"), format(round(ending3, 2), "<20f"))

# First, we store the interests and ending balances in lists, and use a for loop to print them out
# and you don't need 10 spaces for month! I changed to 5 below
interests = [interest1, interest2, interest3]
endings = [invest, ending1, ending2, ending3]

for i in range(3):
  # Don't freak out about this. This is simply saying print, and format it so that {i : <8} (id takes 8 spaces, left align as < indicates), etc. Note that the '%.2f' % endings[i] formats the float entry at ending[i] into two decimal places.
    print(
        f"{i : <8}{'%.2f' % endings[i]: <20}{'%.2f' % interests[i] : <10}{'%.2f' % endings[i+1] : <25}")
