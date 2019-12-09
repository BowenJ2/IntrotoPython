#Program that asks user for number then prints out factors of number

number = int(input("Enter number here: "))
list_range = list(range(1,number+1))

divisor_list = []


for i in list_range:
    if number % i == 0:
        divisor_list.append(i)


print(divisor_list)
        
