fruits = ["apple", "mango", "cherry", "banana"]  # create a list
# print(fruits)   # print a list
# print(type(fruits))  # check type of list
# print(len(fruits))  # check length of list

# checking if an item is present in the list
# if "banana" in fruits:
#     print("Banana is a part of the list")

# checking if an item is not present in the list
# if "Kiwi" not in fruits:
#     print("Kiwi is not part of the list")


# Indexing in list
# print(fruits[1])  # mango
# print(fruits[-3])  # mango

# print(fruits[1:3])  # ['mango', 'cherry']
# print(fruits[-3:-1])  # ['mango', 'cherry']


# adding elements to a list
# fruits.append("kiwi")
# print(fruits)

# inserting element to a list
# fruits.insert(2, "kiwi")
# print(fruits)

# extends new list at the end of original list
# more_fruits = ["kiwi", "papaya"]
# fruits.extend(more_fruits)
# print(fruits)


# removing element from the list
# fruits.remove("banana")
# print(fruits)

# fruits.pop(1)
# print(fruits)

# fruits.pop()
# print(fruits)


# changing/updating items in a list

# fruits[1] = "kiwi"
# print(fruits)

# fruits[1:3] = ["papaya"]
# print(fruits)


# sorting a list

# fruits.sort()  # by default ascending
# print(fruits)

# fruits.sort(reverse=True)
# print(fruits)

# fruits.reverse()
# print(fruits)


# list comprehension

# new_fruits = [fruit for fruit in fruits if "a" in fruit]
# print(new_fruits)

# copy a list

# new_fruits = fruits.copy()
# print(new_fruits)

# concat new list
# new_fruits = fruits.copy()
# new_fruits = fruits + new_fruits
# print(new_fruits)


# nested list
fruits.insert(2, ["kiwi", "papaya"])
print(fruits)
print(fruits[2][0])
