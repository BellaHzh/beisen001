a = int(input('Enter an integer: '))
is_prime = True
for number in range(2, a):
    if a % number == 0:
        is_prime = False
        break

if is_prime == True:
    print(f"{a} is a prime number.")
else:
    print(f"{a} is not a prime number.")
