# A
# AB
# ABC
# ABCD


n = int(input("Enter n: "))

for i in range(1, n+1):
    current_letter = ord('A')
    for j in range(1, i + 1):
        print(chr(current_letter), end="")
        current_letter += 1
    print()
