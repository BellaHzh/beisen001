from time import sleep

x = 5
i = 1

# infinite loop
# while x > 0:
#     print(x, i)
#     i += 1
#     sleep(0.1)

# while 1 == 2:
#     print('1 == 2')

# while False:
#     print('False!')
#     sleep(1)

# while True:
#     print('True!')
#     sleep(1)

# controlled loop
while x > 0:
    x -= 1  # x = x - 1
    print(x)
    sleep(1)
