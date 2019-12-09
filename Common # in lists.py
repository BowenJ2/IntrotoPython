#find common numbers in both lists and print them no repeats


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

number_list = []
for x in a:
    for y in b:
        if x == y:
            number_list.append(y)

new = set(number_list)
print(new)
