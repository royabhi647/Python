# creating a set
names = {"Sia", "Mia", "Tia"}

# print set
# print(names)

# check length of set
# print(len(names))

# check data type of set
# print(type(names))

# accessing items of set
# for x in names:
#     print(x)


# check if an item exists in a set
# if "Sia" in names:
#     print("Sia is in the set")


# add elements in a set
# names.add("Ria")
# print(names)


# add another sequence in a set
# names_list = ["Ria", "Kia"]
# names.update(names_list)
# print(names)


# removing element from a set
# names.remove("Tia")
# discard function will not throw an error if value is not present in set
# names.discard("Ria")
# print(names)


# joining 2 sets
s1 = {'a', 'b', 'c'}
s2 = {'d', 'e', 'a'}
print(s1, s2)

# s3 = s1.union(s2)
# print(s3)

# s1.update(s2)
# print(s1)


# keep only duplicates while joining
# s1.intersection_update(s2)
# print(s1)

# keep all values except duplicates
s1.symmetric_difference_update(s2)
print(s1)
