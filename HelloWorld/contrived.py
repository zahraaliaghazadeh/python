numbers = [1, 45, 32, 12, 60]

for number in numbers:
    if number % 8 == 0:
        # reject the list
       print("The numbers are unacceptable")
       break
# this else is associated with the loop and not with the if
else:
    print("All those numbers are fine")