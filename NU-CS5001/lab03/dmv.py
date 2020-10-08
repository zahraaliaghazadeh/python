# import lib
import random

# Constant var
NEXT_YEAR = "21"

# welcome message
print("Welcome to the DMV (estimated wait time is 3 hours")
# input prompts
name = input("Please enter your first, middle, and last name: ")
dob = input("Enter date of birth: ")
# code to find space and break the name
name_break = name.rfind(' ')
first_and_middle = name[: name_break].capitalize()
last = name[name_break + 1:].capitalize()

# to assign a random 7 digit number
num = random.randint(1000000, 9999999)


print(
    "-" * 40 + "\n"
    "Washington Driver License" + "\n"
    "LN {}".format(last) + "\n"
    "DL {}".format(num) + "\n"
    "FN {}".format(first_and_middle) + "\n"
    "DOB {}".format(dob) + "\n"
    "Exp {}".format(dob[0:6] + NEXT_YEAR) +
    "\n" + "-" * 40
)
