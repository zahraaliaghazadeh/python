import sys


def triangular():
    """
    Function takes an input from command line
    :return: the sum from 1 up to that number
    """
    sum = 0
    num = int(sys.argv[1])
    # for i in range(1, num+1):
    #     sum += i
    # print(sum)
    # ============
    # this formula calculates the sum too
    print((num * (num+1)) / 2)


triangular()
