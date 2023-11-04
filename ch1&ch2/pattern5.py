#    1
#   123
#  12345
# 1234567

n = int(input("Enter n: "))

for i in range(1, n + 1):   # loops for rows
    # printing spaces
    print(" " * (n - i), end="")

    # printing digits
    for j in range(1, 2 * i):
        print(j, end="")
    print()
