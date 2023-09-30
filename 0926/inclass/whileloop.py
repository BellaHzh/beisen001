max = 999
current = 2
power = 1

while (current < max):
    power += 1
    current *= 2
    if (current > max):
        power -= 1
        current /= 2
        break
    # current = current * current

print("current:", current, "power:", power)
