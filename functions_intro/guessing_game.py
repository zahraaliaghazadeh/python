import random

# python docstrings become an attribute of the function
def get_integer(prompt):
    """
    Get an integer from standard Input (Stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: The String that the user will see, when
        they 're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        # highlight input ctrl J on Mac
        # and ctrl Q on windows ctrl J on Mac , and ctrl click
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else is not needed because return would be executed
        # else:
        print("{0} is not a valid number".format(temp))


# lines below show the doc string of the function
print(input, __doc__)
print("*" * 80)
print(get_integer.__doc__)
print("*" * 80)

help(get_integer)
# ***********************

highest = 1000
answer = random.randint(1, highest)
guess = 0
print ("Please guess number between 1 and {}: ".format(highest))


while guess != answer:
    guess = get_integer(": ")

    if guess == answer:
        print("Well done, you guessed it")
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")



