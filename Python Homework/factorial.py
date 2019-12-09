def factorial(n):
    if n == 1:
        return 1          #assigns 1 to n
    else:
        return n*factorial(n-1)
