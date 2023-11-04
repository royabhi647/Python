# # for converting characters to uppercase
# str1 = "new york"
# str2 = str1.upper()
# print(str2)

# # for converting characters to lowercase
# str3 = str2.lower()
# print(str3)

# # for capitalising the first character of my string
# str4 = str3.capitalize()
# print(str4)


# for stripping/removing any trailing whitespaces
# str1 = "     hello world!      "
# print(str1.strip())
# print(str1)


# replacing substring
# str1 = "Hello world, what a beautiful world this is!"
# print(str1.replace("world", "earth"))
# print(str1.replace("world", "earth", 1))


# splitting string
# str1 = "ria pia sia tia mia"
# list = str1.split()
# print(list)


# concatenation
# str1 = "Hello World!"
# str2 = "What a great place this is."
# print(str1 + str2)


# string formatting
# student_name = "Pallavi"
# student_marks = 98

# str1 = "The student name is {s}, and marks is {m}".format(
#     s=student_name, m=student_marks)
# print(str1)


text = "The unexpected always happens"
print(text)
print(len(text))
print(text.find('pp'))
print(text[:11])
print(text.replace('always', 'never'))
text2 = "no matter what"
new_text = text + text2
print(new_text)
