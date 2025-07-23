import random

initial_throws = int(input("How many dart throws? "))
throws = initial_throws
while throws <= 0:
    initial_throws = int(input("Please enter a positive number: "))
    throws = initial_throws
green = 0
gray = 0
blue = 0
yellow = 0
red = 0
black = 0
miss = 0
print()
while throws > 0:
    x = random.uniform(0, 800)
    y = random.uniform(0, 500)
    if 300 <= x <= 800 and 50 <= y <= 150:
        green += 1
    elif (550 <= x <= 750 and 250 <= y <= 500) and (x not in range(350, 451)) and (y not in range(600, 701)):
        red += 1
    elif (((x-350)**2+(y-300)**2)**0.5) <= (45000)**0.5:
        yellow += 1
    elif (((x-100)**2+(y-100)**2)**0.5) <= (20000)**0.5:
        gray += 1
    elif (((x-100)**2+(y-250)**2)**0.5) <= (20000)**0.5:
        blue += 1
    else:
        if ((((x-100)**2+(y-100)**2)**0.5) <= (20000)**0.5) and ((((x-100)**2+(y-250)**2)**0.5) <= (20000)**0.5):
            black += 1
        else:
            miss += 1
    throws -= 1
print(f"Green: {green} ({round((green/initial_throws)*100,2)}%)")
print(f"Yellow: {yellow} ({round((yellow/initial_throws)*100,2)}%)")
print(f"Red: {red} ({round((red/initial_throws)*100,2)}%)")
print(f"Gray: {gray} ({round((gray/initial_throws)*100,2)}%)")
print(f"Blue: {blue} ({round((blue/initial_throws)*100,2)}%)")
print(f"Black: {black} ({round((black/initial_throws)*100,2)}%)")
print(f"Miss: {miss} ({round((miss/initial_throws)*100,2)}%)")
