# Take 3 positive integers input and print the greatest of them.

n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))
n3 = int(input("Enter number3: "))

# n1 is greatest
if n1 > n2 and n1 > n3:
    print(n1, "is the greatest number")
# n2 is the greatest
elif n2 > n1 and n2 > n3:
    print(n2, "is the greatest number")
# n3 is the greatest
else:
    print(n3, "is the greatest number")


# using nested if else statement
if n1 > n2:
    if n1 > n3:
        print(n1, "is greatest element")
    else:
        print(n3, "is greatest element")
else:
    if n2 > n3:
        print(n2, "is greatest element")
    else:
        print(n3, "is greatest element")
