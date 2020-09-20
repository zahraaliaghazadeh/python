# for index, character in enumerate("abcdefgh"):
#     print(index, character)


for t in enumerate("abcdefgh"):
    index, character = t
    print(index, character)
    print(t)
# the output has 8 tuples

# unpacking tuples is a valuable technique
index, character = [0, 'a']
print(index)
print(character)


