name = input("Please enter your name: ")
age = int(input("Please enter your age"))
if name != "":
    if 18 <= age <=30:
        print("Welcome to the party")
    else:
        print("Not for you!")
else:
    print("You didn't enter a name bro!")