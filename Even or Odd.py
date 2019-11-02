number = int(input("Please enter a number: "))
even_or_odd = number%2
multiple_of_4 = number%4
if even_or_odd == 0:
    print("This is an even number")
elif multiple_of_4 == 0:
    print("This is a multiple of 4")
else:
    print("This is an odd number")
