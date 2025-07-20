# Day Timer

import time

for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, minutes, seconds, sep=':')
            time.sleep(1)  # pause program for 1 second
