# Write a program that asks the user to enter the a starting number (integer), ending number (integer) and the word "even" or "odd". Then generate a customized printout based on their input. Here's a sample running of the program:

# Starting number: 5
# Ending number: 15
# Even or Odd?: even

# output
# 6
# 8
# 10
# 12
# 14
start=int(input("Starting number: "))
end=int(input("Ending number: "))
type=input("Even or Odd? (E)for Even, (O) for Odd: ")
print("")
while True:  
    if start%2==0:
        starttype="E"
    else:
        starttype="O"
    if type=="E":
        if starttype=="E":
            start=start
            break
        else:
            start+=1
            break
    elif type=="O":
        if starttype=="E":
            start+=1
            break
    else:
        type=input("Even or Odd? (E)for Even, (O) for Odd: ")

print("output")
while start<end:
    if start>end:
        break
    print(start)
    start+=2
    
        



