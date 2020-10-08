numbers = (0, 1 , 2, 3, 4, 5)
print(numbers, sep=";")     # doesn't unpack, prints tuple
print(*numbers, sep=";")    # unpacks the sequence (like spread)
def test_star(*args):
    print(args)     # args without a *, packs it and prints as a tuple
    for x in args:
        print(x)
test_star(0, 1, 2, 3, 4, 5)
print()
test_star()