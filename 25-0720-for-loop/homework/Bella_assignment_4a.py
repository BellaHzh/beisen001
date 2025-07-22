city_number = int(
    input("How many cities would you like to enter temperature data for? "))
print()
day_number = int(
    input("How many days would you like to enter temperature data for? "))
while day_number <= 0:
    print("Invalid number, please try again.")
    day_number = int(
        input("How many days would you like to enter temperature data for? "))
print()
print("Ok, let's begin . . . ")
print()
average_all = 0
max_temp = 0
for city in range(1, city_number+1):
    print(f"- City {city} -")
    total = 0
    for day in range(1, day_number+1):
        temp = float(input(f"Enter high temperature for day {day}:"))
        max_temp = max(max_temp, temp)
        total += temp
        average_temp = total/day_number
    print(f"Average high temperature: {round(average_temp,1)}")
    print()
    average_all += average_temp
print()
print(
    f"The average high temperature for all cities was: {round(average_all/city_number,1)}")
print(f"The highest temperature recorded was: {round(max_temp,1)}")
