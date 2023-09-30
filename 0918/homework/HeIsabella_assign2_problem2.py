print("This program will project how much you can earn by investing \n money in a high-yield savings account over a 3 month period.")
print("")
invest=int(input("To begin, enter how much money you would like\nto initially invest (i.e. 500): "))
interest=int(input("Next, enter your projected annual interest rate.\n For example, enter 5 for 5%:"))
print("")
print("------------------ Calculating ------------------")
print("")
print(format("Month","<10s"),format("Starting Balance","<20s"),format("Interest","<20s"),format("Interest Ending Balance","<20s"))
interest1=invest*(interest/100)/12
ending1=invest+interest1
interest2=ending1*(interest/100)/12
ending2=ending1+interest2
interest3=ending2*(interest/100)/12
ending3=ending2+interest2
print(format("1","<10s"),format(round(invest,2),"<10f"),format(round(interest1,2),"<30f"),format(round(ending1,2),"<20f"))
print(format("2","<10s"),format(round(ending1,2),"<10f"),format(round(interest2,2),"<30f"),format(round(ending2,2),"<20f"))
print(format("3","<10s"),format(round(ending2,2),"<10f"),format(round(interest3,2),"<30f"),format(round(ending3,2),"<20f")) 