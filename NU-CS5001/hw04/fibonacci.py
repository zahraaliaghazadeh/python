import sys


def fibonacci():
    """
    This function takes a `num`
    from the user and then returns the fibonnaci
    sequence up to that number.
    :return: a list `fib_list` containing the
    fibonnaci sequence less than that number
    """
    a, b = 0, 1
    fib_list = [a, b]
    num = int(sys.argv[1])
    if num == 1:
        print([a])
    elif num <= 0:
        print('Input must be positive')
    else:
        while len(fib_list) < num:
            sum = a + b
            a, b = b, sum
            fib_list.append(sum)
        print(fib_list)


fibonacci()
