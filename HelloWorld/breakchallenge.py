
# 1) Modify the code so that it stops printing when it reaches a number greater than zero that's exactly divisible by 11
# The number should be the last value printed
# The code should print the same values as it currently does, but stop after printing a number that's also divisible by 11

# for i in range(0, 100, 7):
#     print(i)
#
#     if i % 11 == 0 and i > 0:
#         break


print("-"*40)
# 2) Write a program to print out all the numbers from 0 to 20 that aren't divisible by 3 or 5

for i in range(0, 20):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)
# It is skipping the rest of the code in for loop