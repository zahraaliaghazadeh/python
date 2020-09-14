for i in range ( 1, 20):
    print("i is now {}".format(i))
    # the range is not including the last one

print("-" * 40)

for i in range(0, 10):
    print(i)

print("-" * 40)

for i in range(10):
    print("i is now {}".format(i))
# it starts from 0

print("-" * 40)

for i in range(0, 10, 2):
    print("i is now {}".format(i))
# increments by 2

print("-" * 40)


for i in range(10, 0, -2):
    print("i is now {}".format(i))
# decrements by 2

print("-" * 40)

# for loop with step
# write a program to print out all the numbers from 0 to 100 that are divisible by 7
# way 1
# for i in range(0, 101):
#     if i % 7 == 0:
#         print(i)
# way 2
for i in range(0, 101, 7):
    print(i)


