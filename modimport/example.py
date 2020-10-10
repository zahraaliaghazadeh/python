# print(dir())

# if sth uses _ in the beginning , means it is private to that module
# if something starts with __ dont change it at all

# print(dir(__builtins__))

# for m in dir(__builtins__):
#     print(m)


import shelve

print(dir(shelve))
print()
print(dir(shelve))

for obj in dir(shelve.Shelf):
    if obj[0] != '_':
        print(obj)

# help(shelve) or command + click on shelve will open the original code