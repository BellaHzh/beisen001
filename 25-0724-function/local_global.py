radius = 5  # global variable


def area():
    import math
    area = math.pi * radius ** 2  # local variable
    return area


def change_radius(new_radius):
    global radius
    radius = new_radius


print(area())
change_radius(10)
print(area())
