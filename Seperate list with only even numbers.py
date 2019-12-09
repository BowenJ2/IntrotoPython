#make seperate list with only even numbers


a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even_list = []

for e in a:
    if e % 2 == 0:
        even_list.append(e)

print(even_list)
