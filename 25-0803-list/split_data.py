rolls = "3,1,6,4,1,4,1,3,1,1,6,4,5,6,6,3,3,5,2,4,6,5,5,4,5,5,1,5,1,4,3,1,4,1,3,1,3,3,5,3,3,5,2,4,6,4,6,6,5,1,2,6,5,4,5,4,1,6,4,2,1,6,4,4,5,5,4,2,4,5,5,4,3,4,4,2,2,2,3,6,6,6,2,3,2,4,3,1,5,3,4,4,4,3,2,3,5,6,4,6,4,4,3,1,2,4,3,3,5,6,5,1,5,4,1,6,6,2,4,6"
numbers = rolls.split(',')
total = []
for i in numbers:
    new_i = int(i)
    total.append(new_i)
sum_numbers = sum(total)
count = len(numbers)
average_total = sum_numbers/count
print(sum_numbers, average_total)

# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
