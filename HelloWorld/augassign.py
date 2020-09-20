# augmented assignment in a loop
# early computers could only perform addition. In order to multiply one number by another they performed repeated addition.
# Use a for loop and augmented assignment to give answer the result of multiplying number by multiplier

number = 5
multiplier = 8
answer = 0

for i in range (multiplier):
    answer += number

print(answer)