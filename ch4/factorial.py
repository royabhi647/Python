# function for calculating factorial of a number
def factorial(n):
    ans = 1
    if n == 0:
        ans = 1
    else:
        for i in range(1, n + 1):
            ans *= i

    return ans


n = int(input("Enter n: "))
output = factorial(n)
print("The factorial is:", output)
