pangram = "the quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)


numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
# sorted creates a new list
print(numbers)

# The difference between sort and sorted

numbers.sort()
print(numbers)
# this method sorts them in place , no need to assign to a new variable

another_sorted_numbers = numbers.sort()
print(numbers)
print(another_sorted_numbers)
# this returns None because

# can also pass a literal
missing_letter = sorted ("The quick brown fox jumps over the lazy dog")
print(missing_letter)

# in line 8 , you should not name the variable sorted

missing_letter = sorted ("The quick brown fox jumps over the lazy dog",
                         key=str.casefold)
print(missing_letter)


names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"
         ]
names.sort(key=str.casefold)
print(names)