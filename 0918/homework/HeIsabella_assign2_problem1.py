assignment=float(input("Enter overall assignments grade: "))
quiz=float(input("Enter overall quiz grade: "))
midterm=float(input("Enter midterm grade: "))
desire=float(input("What would you like your final grade to be?: "))
assign_weighted=assignment*0.3
quiz_weighted=quiz*0.1
midterm_weighted=midterm*0.3
final=(desire-assign_weighted-quiz_weighted-midterm_weighted)/0.3
print("")
print("You need to receive a ", round(final, 2), "% on your final to get a", desire, "in the class.")