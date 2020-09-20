data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 192, 350, 360]
# TODO: set up test cases
# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 192, 350, 360]
# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 192, 350, 360]
# data = []

# del data[0:2]
# print(data)
# del data[14:0]
# print(data)

min_valid = 100
max_valid = 200

# for index, value in enumerate(data):
#     if (value < min_valid) or (value > max_valid):
#         del data[index]
#         # index -= 1
#
# print(data)
#  be careful of the size of the object you are iterating over it


# to solve that problem
# Process the low values in the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
print(stop) #for debugging
del data[:stop]
print(data)
# only after the loop terminates you can slice from data

# process the high values in the list
start = 0
for index in range(len(data) - 1, -1, -1):
    # print(index)
    if data[index] <= max_valid:
        # we have the index of the last item to keep
        # set 'start' to the position of the first
        # item to delete, which is 1 after 'index'.
        start = index
        break

print(start)     # for debugging
del data[start:]
print(data)


# edge case :
# An edge case is a problem or situation that occurs only at an extreme (maximum or minimum) operating parameter. For example, a stereo speaker might noticeably distort audio when played at maximum volume, even in the absence of any other extreme setting or condition.


# In programming, an edge case typically involves input values that require special handling in an algorithm behind a computer program. As a measure for validating the behavior of computer programs in such cases, unit tests are usually created; they are testing boundary conditions of an algorithm, function or method. A series of edge cases around each "boundary" can be used to give reasonable coverage and confidence using the assumption that if it behaves correctly at the edges, it should behave everywhere else.[1]
#
# For example, a function that divides two numbers might be tested using both very large and very small numbers. This assumes that if it works for both ends of the magnitude spectrum, it should work correctly in between.


# edge case vs corner case