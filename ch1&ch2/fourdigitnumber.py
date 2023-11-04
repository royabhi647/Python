# Take positive integer input and tell if it is a four digit number or not.

number = int(input("Enter a number: "))

if number >= 1000 and number <= 9999:
    print("It is a 4 digit number")
else:
    print("Not a 4 digit number")
