print("Triangle Validity")
print()
choice = "yes"
while choice == "yes":
    print()
    point_X_1 = float(input("Enter the X position of point 1: "))
    while point_X_1 < 0:
        point_X_1 = float(input("Please enter a non-negative number: "))
    point_Y_1 = float(input("Enter the Y position of point 1: "))
    while point_Y_1 < 0:
        point_Y_1 = float(input("Please enter a non-negative number: "))
    print()

    point_X_2 = float(input("Enter the X position of point 2: "))
    while point_X_2 < 0:
        point_X_2 = float(input("Please enter a non-negative number: "))
    point_Y_2 = float(input("Enter the Y position of point 2: "))
    while point_Y_2 < 0:
        point_Y_2 = float(input("Please enter a non-negative number: "))
    print()

    point_X_3 = float(input("Enter the X position of point 3: "))
    while point_X_3 < 0:
        point_X_3 = float(input("Please enter a non-negative number: "))
    point_Y_3 = float(input("Enter the Y position of point 3: "))
    while point_Y_3 < 0:
        point_Y_3 = float(input("Please enter a non-negative number: "))

    distance_1_2 = ((point_X_1-point_X_2)**2+(point_Y_1-point_Y_2)**2)**0.5
    distance_2_3 = ((point_X_2-point_X_3)**2+(point_Y_2-point_Y_3)**2)**0.5
    distance_1_3 = ((point_X_1-point_X_3)**2+(point_Y_1-point_Y_3)**2)**0.5
    print()
    print("Here are the lengths of each side of the triangle.")
    distance_1_2_new = format(distance_1_2, ".2f")
    distance_2_3_new = format(distance_2_3, ".2f")
    distance_1_3_new = format(distance_1_3, ".2f")
    print(f"Side 1: {distance_1_2_new}")
    print(f"Side 2: {distance_2_3_new}")
    print(f"Side 3: {distance_1_3_new}")
    print()
    if (distance_1_2+distance_1_3 <= distance_2_3) or (distance_1_2+distance_2_3 <= distance_1_3) or (distance_2_3+distance_1_3 <= distance_1_2):
        print("This is not a valid triangle.")
        print()
        choice = input("Would you like to test another triangle? (yes/no): ")
    else:
        if distance_1_2 == distance_2_3 == distance_1_3:
            print("This is a valid triangle, it is equilateral.")
        elif (distance_1_2 == distance_2_3) or (distance_1_3 == distance_2_3) or (distance_1_2 == distance_1_3):
            print("This is a valid triangle, it is isosceles.")
        elif distance_1_2 != distance_2_3 != distance_1_3:
            print("This is a valid triangle, it is scalene.")
        print()
        choice = input("Would you like to test another triangle? (yes/no): ")
