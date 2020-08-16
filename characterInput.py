name = input("Please enter your name:")
age = int(input("Please enter your age:"))

if type(name) == str:
    if type(age) == int:
        print(f"{name} you are {age} years old and you will be 100 after {100 - age} years")
    else:
        print("Please enter a valid number")
else:
    print("please enter your name")
