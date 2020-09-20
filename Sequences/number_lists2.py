empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

digits = sorted("2312434346544")
print(digits)

# list is not a function but it is a class identifier
# but can be used as a function for now
digits = sorted("2312434346544")
print(digits)

# more_numbers = list(numbers)
# print(more_numbers)
# print(numbers is more_numbers)
# print(numbers == more_numbers)

# more_numbers = numbers[:]
# print(more_numbers)
# print(numbers is more_numbers)
# print(numbers == more_numbers)

# There are 12 different ways to copy a list

more_numbers = numbers.copy()
print(more_numbers)
print(numbers is more_numbers)
print(numbers == more_numbers)


# https://stackoverflow.com/questions/2612802/list-changes-unexpectedly-after-assignment-how-do-i-clone-or-copy-it-to-prevent/43220129#43220129

numbers = [even, odd]
print(numbers)

for number_list in numbers:
    print(number_list)

    for value in number_list:
        print(value)

# the code above lets you make nested lists