#HotDog = $2.50
#Drink = $1.50

#How much are prices
#No change

print("Welcome to Bowen's hot dog stand!")
print("We sell hot dogs and drinks")
option = input("Would you like to see the menu? ")
if option == "yes":
          print("asdf")
HotDogs = int(input("How many hot dogs would you like? "))
Drinks = int(input("How many drinks would you like? "))
Total = HotDogs * 2.50 + Drinks * 1.50
total = str(HotDogs * 2.50 + Drinks * 1.50)
Payment = float(input("It will cost " + total + " dollars. How much would you like to pay? "))
if Total < Payment:
    PP = str(Payment - Total)
    print("Your change is " + PP + " dollars")
elif Total > Payment:
    NP = str(Total - Payment)
    print("You owe us " + NP + " dollar(s)")
elif Total == Payment:
    print("That is the exact change")
else:
    print("Please try again")

print("Thank you and come again!")
