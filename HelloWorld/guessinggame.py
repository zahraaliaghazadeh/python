# answer = 5
# print("please guess number between 1 and 10: ")
# guess = int(input())
#
# if guess < answer:
#     print("Please guess higher")
# elif guess > answer:
#     print ( "Please guess lower")
# else:
#     print("You got it first time")

answer = 5

print ("Please guess number between 1 and 10: ")
guess = int(input())

# when there is : we indent the code
if guess != answer:
    if guess < answer:
        print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it first time")
