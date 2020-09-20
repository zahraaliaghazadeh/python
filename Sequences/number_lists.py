even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

print(min(even))
print(max(even))
print(min(odd))
print(max(odd))

print()
print(len(even))
print(len(odd))

print()
# to count how many times s is repeated in the word
print("mississippi".count("s"))     #4
print("mississippi".count("issi"))  #1

even.extend(odd)
print(even)
another_even = even
print(another_even)

even.sort()
print(even)

even.sort(reverse=True)
print(even)
print(another_even)
# mutated the list by sorting it first

# https://docs.python.org/3.8/library/functions.html#any