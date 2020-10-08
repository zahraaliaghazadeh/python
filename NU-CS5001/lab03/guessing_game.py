import random
import math
# constant var
HIGHEST = 50
# assigning a number between 1 and highest
random_number = random.randint(1, HIGHEST)

# assiging a variable for users guess
user_guess = 0
print("Welcome to the Guessing Game!")
print("I picked a number between 1 and {}. Try and guess!".format(HIGHEST))
print("Please guess number between 1 and {}: ".format(HIGHEST))

# counter for tries
tries = 0


while user_guess != random_number:
    user_guess = int(input())
    tries += 1
    # difference , absolute value
    difference = abs(user_guess - random_number)

    # conditions to guide the user
    if user_guess == random_number:
        print("Well done, you guessed it")
    elif difference == 1:
        print("Scalding hot")
    elif difference == 2:
        print("extremely warm")
    elif difference == 3:
        print("very warm")
    elif difference == 5:
        print("warm")
    elif difference == 8:
        print("cold")
    elif difference == 13:
        print("very cold")
    elif difference == 20:
        print("extremely cold")
    elif difference > 20:
        print("icy freezing miserably cold")

    else:
        if user_guess < random_number:
            print("Please guess higher")
        else:
            print("Please guess lower")

print("Congratulations. You figured it out in {} tries.".format(tries))

# conditions for specific message based on number of tries
if 10 <= tries:
    print("You are the worst guesser I've ever seen.")
elif 8 <= tries and tries <= 9:
    print("This is not your game.")
elif tries == 7:
    print("Meh.")
elif 5 <= tries and tries <= 6:
    print("That was okay.")
elif 2 <= tries and tries <= 4:
    print("That was amazing!")
elif tries == 1:
    print("That was lucky!")
else:
    print("Trying to break my game?")
