low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press Enter to start")

guesses = 1
while low != high:

    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h or l "
                     .format(guess).casefold())

    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    else:
        print("Please enter h, l ")

    guesses += 1
#     else means completed or no break. kinda confusing but you gotta know what else means here.
else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses!".format(guesses))


#     TODO: this has a bug, when I tried 900 or 800.




