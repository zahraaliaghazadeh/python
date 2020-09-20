# iterating backwards
# removing rogue vlues
# when an item 's removed from the list, all the later items are shuffled down, to fill in the gap
# That messes upu the index numbers, as we work forwards through the list
data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]
min_valid = 100
max_valid = 200
# for index in range(len(data) - 1, - 1, - 1):
#     if data[index] < min_valid or data[index] > max_valid:
#         print(index, data)
#         print(index)
#         del data[index]
# print(data)

# this does the same thing as the one in outlier


# another way
top_index = len(data) -1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]
print(data)