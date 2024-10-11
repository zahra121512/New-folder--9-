age = int(input("Enter your age: "))

if 10 <= age:
    if age <= 20:
        print("Your age is within the valid range. ")
    else:
        print("Your age is not within the valid range.")
else:
    print("Your age is not greater than 10.")