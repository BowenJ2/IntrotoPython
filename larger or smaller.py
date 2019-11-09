#ask user for number and if number is larger than goal number 0 - 100

g = 10
n = int(input("Enter a number: "))
while g != n:
    if n > g:
        print("The number is too large")
        n = int(input("Enter a number: "))

    elif n < g:
        print("The number is too small")
        n = int(input("Enter a number: "))
print("yup")
