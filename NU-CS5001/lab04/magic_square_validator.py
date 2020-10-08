print("Enter a magic number")
numbers = []
for i in range(1, 4):
    numbers.append((input()))

sum = 0

MAGIC_NUMBER = 15

# for j in range(len(numbers)):
#     for k in range(len(numbers[0])):
#         sum += int(numbers[k])
        # if (sum == 15):

# for i, value in enumerate(numbers):
#     for j, j_value in value:
#         print(j)

vertical_sum = 0
horizontal_sum = 0
diagonal_sum = 0

# for i in range(3):
#     if i == 0:
#         if int(numbers[0][0]) + int(numbers[0][1]) + int(numbers[0][3]) != MAGIC_NUMBER or
#             int :
#     else:

if ((int(numbers[0][0]) + int(numbers[0][1]) + int(numbers[0][2]) != MAGIC_NUMBER) or
    (int(numbers[1][0]) + int(numbers[1][1]) + int(numbers[1][2]) != MAGIC_NUMBER) or
    (int(numbers[2][0]) + int(numbers[2][1]) + int(numbers[2][2]) != MAGIC_NUMBER) or
    (int(numbers[0][0]) + int(numbers[1][0]) + int(numbers[2][0]) != MAGIC_NUMBER) or
    (int(numbers[0][1]) + int(numbers[1][1]) + int(numbers[2][1]) != MAGIC_NUMBER) or
    (int(numbers[0][2]) + int(numbers[1][2]) + int(numbers[2][2]) != MAGIC_NUMBER) or
    (int(numbers[0][0]) + int(numbers[1][1]) + int(numbers[2][2]) != MAGIC_NUMBER) or
    (int(numbers[0][2]) + int(numbers[1][1]) + int(numbers[2][0]) != MAGIC_NUMBER)):
    print("Not a magic square!")
else:
    print("This is a magic square!")

    





    





