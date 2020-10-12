import sys

height = int(sys.argv[1])
diamond = []
# append a string of (height - i) // 2 number of spaces
# to center it and i number of "*" to list
# i starts at 1, and then is incremented by 2,
# each increment a new line until, i or number of "*" == height,
# or if height is even until "*" == height - 1
for i in range(1, height + 1, 2):
    diamond.append(" " * ((height - i) // 2) + "*" * i)
# join each line with a new line char
# the join method is passed the diamond list, which is half
# of the diamond, combined with the diamond list in reverse
# which will give the other half of the diamond.
#
# for the reverse, if the height is even it needs to repeat the last element in
#  the list
# i.e. start at len(diamond) - 1 - 0
# if the height is odd, it needs to skip the last element (start from second
# last element)
# i.e. start at len(diamond) - 1 - 1
print("\n".join(diamond + diamond[len(diamond) - 1 - height % 2::-1]))
