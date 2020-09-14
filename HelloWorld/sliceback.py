
letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25:0:-1]
print(backwards)

# backwards = letters[25:-1:-1] we requesting z not including z so we get nothing

backwards = letters[25::-1]
backwards = letters[::-1]

# make sure the stop value is greater than the start value

print("challenge1")
# qpo
backwards = letters[16:13:-1]
print(backwards)
backwards = letters[-10:-13:-1]  #qpo
print(backwards)

print()
# edcba
print("challenge2")
backwards = letters[4::-1]
print(backwards)

print()
# last 8 characters
print("challenge3")
backwards = letters[:-9:-1]
print(backwards)
print(letters[:-9:-1])

print(letters[-4:])    # last 4
print(letters[-1:])    # last item (z)
print(letters[:1])     # first char (a) better to use this than the next one
# because it will throw error if string is empty
print(letters[0])      # (a)







