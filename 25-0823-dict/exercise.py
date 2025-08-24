foo = {"apple": 1.99, "pear": 2.99, "peach": 3.99}
bar = ["apple", "starfruit", "orange", "pear", "PEACH", "banana"]

for i in range(len(bar)):
    print(f"{i + 1} {bar[i]}:", end=" ")
    if bar[i] in foo:
        print(foo[bar[i]])
    else:
        print("?")

'''
1 apple: 1.99
2 starfruit: ?
3 orange: ?
4 pear: 2.99
5 PEACH: ?
6 banana: ?
'''
