#ask for sentence and determine if it is a palindrome or not

sentence = str(input("Enter your sentence: "))

x = ""
for i in range(len(sentence)):
    x += sentence[len(sentence)-1-i]

if x == sentence:
    print("This is a palindrome")
else:
    print("This is not a palindrome")
