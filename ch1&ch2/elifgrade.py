# Take input percentage of a student and print the Grade according to marks:
# 81-100 very good
# 61-80 good
# 41-60 average
# <=40 fail

marks = int(input("Enter the marks: "))

if marks > 80:
    print("Very Good")
elif marks > 60:
    print("Good")
elif marks > 40:
    print("Average")
else:
    print("Fail")
