# write a function that prints hello world

# def printHello():
#     # body of function
#     print("Hello world!!")


# printHello()


# function which takes 2 numbers as input and return their sum
# def add(n1, n2):
#     sum = n1 + n2
#     return sum


# x = 2
# y = 3
# print("The sum is", add(x, y))
# # positional argument
# print("The sum is", add(3, 4))
# # keyword argument
# print("The sum is", add(n2=2, n1=3))


# def add(n1, n2=0):
#     sum = n1 + n2
#     return sum


# # default argument
# print("The sum is", add(8))


# arbitary arguments
# def addAllNumbers(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum


# output = addAllNumbers(1, 2, 3, 4, 5)
# print("The Sum is", output)


def studentInfo(**kwargs):
    for x, y in kwargs.items():
        print(x, "is", y)


studentInfo(name="urvi", age=22, city="Delhi")
studentInfo(name="Ria", age=20, city="Bangalore")
