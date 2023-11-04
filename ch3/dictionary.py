# creating a dictionary

phones = {
    "John": 982628,
    "Ria": 468201,
    "Joy": 126830
}

# printing the dict

# print(phones)

# checking type of dict

# print(type(phones))

# checking the length of dict

# print(len(phones))

# access items of dict

# print(phones["John"])
# print(phones.get("John"))

# print keys

# print(phones.keys())

# update value in dict

# phones["John"] = 987654
# print(phones)

# add elements in dict

# phones["kia"] = 234567
# print(phones)

# add more dictionary in original dic

# more_phones = {
#     "Kia": 234567
# }
# phones.update(more_phones)
# print(phones)

# remove elements in a dict

# phones.pop("John")
# print(phones)

# phones.popitem()  # this will remove the last added item
# print(phones)

# phones.clear()  # this will empty the dict
# print(phones)


# printing values of a dict

# for x in phones:
#     print(phones[x])

# print key value both

# for x in phones.items():
#     print(x)

# for x, y in phones.items():
#     print(x, y)


# nested dictionaries

phones = {
    "Area1": {
        "x": 0,
        "y": 1,
        "z": 2
    },
    "Area2": {
        "a": 3,
        "b": 4,
        "c": 5
    }
}

print(phones["Area1"]["y"])
print(phones["Area2"]["c"])
