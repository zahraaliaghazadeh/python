

def main():
    """
    This function takes three 3 digit numbers
    and will check whether or not the set of three numbers is a magic
    square meaning that in all directions, sum is 15.
    :return: if the set of numbers is magic square
    """
    print("Enter a 3 digit magic number")
    numbers = []
    for i in range(1, 4):
        numbers.append((input()))

    MAGICAL_SUM = 15
    vertical_sum = 0
    horizontal_sum = 0
    diagonal_sum = 0

    if ((int(numbers[0][0]) + int(numbers[0][1]) + int(numbers[0][2])
            != MAGICAL_SUM) or
        (int(numbers[1][0]) + int(numbers[1][1]) + int(numbers[1][2])
            != MAGICAL_SUM) or
        (int(numbers[2][0]) + int(numbers[2][1]) + int(numbers[2][2])
            != MAGICAL_SUM) or
        (int(numbers[0][0]) + int(numbers[1][0]) + int(numbers[2][0])
            != MAGICAL_SUM) or
        (int(numbers[0][1]) + int(numbers[1][1]) + int(numbers[2][1])
            != MAGICAL_SUM) or
        (int(numbers[0][2]) + int(numbers[1][2]) + int(numbers[2][2])
            != MAGICAL_SUM) or
        (int(numbers[0][0]) + int(numbers[1][1]) + int(numbers[2][2])
            != MAGICAL_SUM) or
        (int(numbers[0][2]) + int(numbers[1][1]) + int(numbers[2][0])
            != MAGICAL_SUM)):

        print("Not a magic square!")
    else:
        print("This is a magic square!")


main()
