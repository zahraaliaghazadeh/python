low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press Enter to start")

guesses = 1
while True:
    # guess = low + (high - low) // 2
    # high_low = input("My guess is {}. Should I guess higher or lower? "
    #                  "Enter h or l, or c if my guess was correct "
    #                  .format(guess).casefold())

    print("\t Guessing in the range of {} to {}".format(low,high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                 "Enter h or l, or c if my guess was correct "
                 .format(guess).casefold())

    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess.
        # pass # this will make the code right when you ll replace it with code later
         low = guess + 1
    elif high_low == "l":
        # Guess lower. The high end of the range becomes one less than the guess.
        # pass
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l or c")

    # Python doesnt have switch case

    # augmented assignment is more efficient
    # Augmented Assignment = "The combination, in a single document of a binary operation and an assignment statement"

    # guesses = guesses + 1
    guesses += 1


