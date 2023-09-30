names = ["尾巴", "墨墨", "年糕"]
#       0, 1, 2, 3, 4
# index starts from 0
# multiple commenting: cmd + /

ints = [1, 2, 3, 4, 5]
sum = 0

for name in names:
    print(int)

# enumerate()
# stepwise
for index, int in enumerate(ints):
    sum += int
    print("Index:", index, "Int:", int, "Sum:", sum)

# range(start, stop, step)
for i in range(0, 4, 2):
    print(ints[i])
