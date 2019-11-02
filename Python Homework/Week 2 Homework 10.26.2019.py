#Week 2 Homework October 26th, 2019

#1.circle.py

from math import *
r = float(input("Enter the radius of the circle: "))
if r < 0:
    print("Sorry, I can't do a negative radius")
else:
    area = str(pi * r**2)
    print("The area of the circle is " + area)

#3. False, True, False, True, False, False, True, True, False, True


#4. Score reflection

number = float(input("Enter a number from 0-100: "))
if 0 > number or number > 100:
    print("Sorry, number is out of range.")
elif 0 <= number <= 50:
    str(number)
    print(number, " is not so good.")
elif 50 < number <= 65:
    str(number)
    print(number, " needs improvement.")
elif 65 < number <= 80:
    str(number)
    print(number, " is average.")
elif 80 < number <= 90:
    str(number)
    print(number, " is very good.")
elif 90 < number <= 100:
    str(number)
    print(number, " is excellent!")

#5. How many hundreds can fit in?

num = int(input("Enter a number: "))
how_many = str(num // 100)
remainder = str(num % 100)
if num >= 0:
    print(num, "= " + how_many + "*100 + " + remainder)
elif num < 0:
    how_many = -(-num // 100)
    remainder = -(-num % 100)
    print(num, "= ", how_many, "* 100", remainder)
