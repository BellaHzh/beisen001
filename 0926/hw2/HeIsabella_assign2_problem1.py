assignment = float(input("Enter overall assignments grade: "))
quiz = float(input("Enter overall quiz grade: "))
midterm = float(input("Enter midterm grade: "))
desire = float(input("What would you like your final grade to be?: "))

assign_weighted = assignment*0.3
quiz_weighted = quiz*0.1
midterm_weighted = midterm*0.3
final = (desire-assign_weighted-quiz_weighted-midterm_weighted)/0.3

# print("")  # No need to write this line, simply put \n in print to go to a new line, as shown below
print("\nYou need to receive a ", round(final, 2),
      "% on your final to get a", desire, "in the class.")

# You forgot to count the case where your calculated final grade is greater than 100%, implying that it would be impossible for the user to get their desire score. To fix this, simply add a conditional statement (i.e. if) below, and I'll still give you full credit.

# Write your code here~
