# Part A
# Firstly, I'll let the users to put the number they want to convert
# Secondly, I'll try to print the boundary. For example, the "-----" and the sapces.
# Thirdly, I'll try to use the format formula to convert the inputs into the numbers corresponding to different units.
# Then, I'll design the width of the table
# Finally, print them out

# Part B
ml = int(input("Enter an amount (in ML) to convert: "))
print("------------------------------------------------")
print(format("mL to US Fluid Volume Units ", ">35s"))
print("------------------------------------------------")
tsp = 0.202884*ml
tbsp = 1/3*int(tsp)
cup = 1/16*float(tbsp)
pint = 1/2*float(cup)
quart = 1/2*float(pint)
gallon = 1/4*float(quart)
floz = 1/29.5735*int(ml)
print(format("ml:", "<20s"), ml)
print(format("tsp:", "<20s"), tsp)
print(format("tbsp:", "<20s"), tbsp)
print(format("cup(s):", "<20s"), cup)
print(format("pint(s):", "<20s"), pint)
print(format("quart(s):", "<20s"), quart)
print(format("gallon(s):", "<20s"), gallon)
print(format("fl oz:", "<20s"), floz)
