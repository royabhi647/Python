def print_1_to_n(n):

    # base case
    if n == 0:
        return

    # recursive case
    print_1_to_n(n - 1)
    print(n)


n = int(input("Enter n: "))
print_1_to_n(n)
