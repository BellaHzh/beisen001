date = int(input("Enter a date (YYYYMMDD): "))
year = int(date/10000)
day = (date) % 100
daylast = day % 10
month = int(((date-day) % 10000)/100)
if month == 1:
    monthtype = "January"
elif month == 2:
    monthtype = "Feburary"
elif month == 3:
    monthtype = "March"
elif month == 4:
    monthtype = "April"
elif month == 5:
    monthtype = "May"
elif month == 6:
    monthtype = "June"
elif month == 7:
    monthtype = "July"
elif month == 8:
    monthtype = "August"
elif month == 9:
    monthtype = "September"
elif month == 10:
    monthtype = "October"
elif month == 11:
    monthtype = "November"
elif month == 12:
    monthtype = "December"
if year % 4 == 0:
    print(year, "is a leap year")
    yeartype = 1
else:
    print(year, "is NOT a leap year")
    yeartype = 0
if (month == 4 or 6 or 9 or 11) and (day >= 31):
    print("This is not a valid date in", year)
elif (yeartype == 1) and (month == 2) and (day >= 30):
    print("This is not a valid date in", year)
elif (yeartype == 0) and (month == 2) and (day >= 29):
    print("This is not a valid date in", year)
elif (month == 1 or 3 or 6 or 7 or 8 or 10 or 12) and (day >= 32):
    print("This is not a valid date in", year)
elif month not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
    print("This is not a valid date in", year)
else:
    if daylast == 1:
        daytype = "st"
    elif daylast == 2:
        daytype = "nd"
    elif daylast == 3:
        daytype = "rd"
    else:
        daytype = "th"
    print(monthtype, " ", day, daytype, " ", year, " is a valid date.", sep='')

# point deduction: minor error, not counting the cases when year % 4 == 0, year % 100 == 0, and year % 400 != 0 which indicates not a leap year. EXAMPLE: 1900, 2100, 2200
# Grade right now: 2.5/3, if fixed before deadline I will add back the points
