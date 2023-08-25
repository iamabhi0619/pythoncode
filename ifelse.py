age = input("Enter your age")
age = int(age)
if age>=22:
    print("You are an adult")
    print("You can not vote")
    print("Now you have a right to merry")
elif age>= 18:
    print("You are an adult")
    print("You can vote")
else:
    print("You are not an adult")
    print("You can not vote")