print("Collatz Conjecture")
print()
number = int(input("Enter a positive integer: "))
init_number = number
largest_number = 0
while number <= 0:
    number = int(input("Please enter a positive integer: "))
print()
i = 1
silent_mode = input("Sildent mode? (yes/no): ")
while number != 1:
    if silent_mode == "no":
        if number % 2 != 0:
            print(f"{i}. {number} (odd): {number} * 3 + 1 = {number*3+1}")
            number = number * 3 + 1
            largest_number = max(number, largest_number)
        else:
            print(f"{i}. {number} (even): {number} / 2 = {number/2}")
            number /= 2
            largest_number = max(number, largest_number)
        i = i+1
    elif silent_mode == "yes":
        if number % 2 != 0:
            number = number * 3 + 1
            largest_number = max(number, largest_number)
        else:
            number /= 2
            largest_number = max(number, largest_number)
        i = i+1
    else:
        silent_mode = input('Please enter "yes" or "no": ')

print(
    f"The number {init_number} has a period of {i-1} in the Collatz conjecture.")
print(f"The highest number reached was {largest_number}")
