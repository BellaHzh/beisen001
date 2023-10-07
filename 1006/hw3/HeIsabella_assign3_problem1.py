import math
while True:
    x1 = float(input("Enter Point #1 - x position: "))
    y1 = float(input("Enter Point #1 - y position: "))
    x2 = float(input("Enter Point #2 - x position: "))
    y2 = float(input("Enter Point #2 - y position: "))
    x3 = float(input("Enter Point #3 - x position: "))
    y3 = float(input("Enter Point #3 - y position: "))
    side1 = math.sqrt((x3-x1)**2+(y3-y1)**2)
    side2 = math.sqrt((x2-x1)**2+(y2-y1)**2)
    side3 = math.sqrt((x3-x2)**2+(y3-y2)**2)
    print()
    print("The length of each side of your test shape is: ")
    print()
    print("Side 1: ", round(side1, 2))
    print("Side 2: ", round(side2, 2))
    print("Side 3: ", round(side3, 2))
    print()
    if side1+side2 <= side3 or side2+side3 <= side1 or side1+side3 <= side2:
        print("This is not a valid triangle")
    else:
        print("This is a valid triangle!")
        if side1 == side2 == side3:
            print("This is an equilateral triangle")
        elif (side1 == side2) or (side1 == side3) or (side2 == side3):
            print("This is an isosceles triangle")
        if (side1**2 > (side2**2+side3**2)) or (side2**2 > (side1**2+side3**2)) or (side3**2 > (side1**2+side2**2)):
            print("This is a scalene triangle")
        elif (side1**2 == (side2**2+side3**2)) or (side2**2 == (side1**2+side3**2)) or (side3**2 == (side1**2+side2**2)):
            print("This is a right triangle")
        else:
            print("This is an acute triangle")
        break
