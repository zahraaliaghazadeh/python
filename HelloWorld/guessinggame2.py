# import random
# highest = 10
# answer = random.randint(1, highest)
# # print(answer) # TODO: Remove after testing
# # this was to test the code by printing the random number
#
# print ("Please guess number between 1 and {}: ".format(highest))
# guess = int(input())
#
# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")



import random
highest = 10
answer = random.randint(1, highest)
# print(answer) # TODO: Remove after testing
# this was to test the code by printing the random number
guess = 0 # initialise to any number that doesn't equal the answer

print ("Please guess number between 1 and {}: ".format(highest))


while guess != answer:
    guess = int(input())

    if guess == answer:
        print("Well done, you guessed it")
    else:
        if guess < answer:
             print("Please guess higher")
        else:
             print("Please guess lower")



