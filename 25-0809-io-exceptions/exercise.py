# Exercise
# Given the file, datafile1.txt, what will be stored in the file at the end of this program?
# Note that every line has a line break at the end of it.

file_object = open("datafile1.txt")  # read mode if not specified
data = file_object.read()
file_object.close()

file_object2 = open("datafile1.txt", "a")
data = data.split("\n")

c = 0
for item in data:
    if c > 0:
        file_object2.write("," + item)
    else:
        file_object2.write(item)
    c += 1

file_object2.write("\n")
file_object2.close()
