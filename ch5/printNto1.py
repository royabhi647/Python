def print_n_to_1(n):

    # base case
    if n == 0:
        return

    print(n)
    # recursive case
    print_n_to_1(n - 1)


n = int(input("Enter n: "))
print_n_to_1(n)
