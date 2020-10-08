
def height_input_validation(height):
    """

    :param height:
    :return:
    """
    while (height <= 2):
        height = int(input("Your value is too small! Enter again: "))
    return height


def width_input_validation(width):
    """

    :param width:
    :return:
    """
    while (width <= 2):
        width = int(input("Your value is too small! Enter again: "))
    return width


def rectangle_drawer():
    """

    :return:
    """
    symbol = input("Please enter the symbol you want to draw the rectangle: ")
    height = int(input("Please enter the height of the rectangle: "))
    height = height_input_validation(height)
    width = int(input("Please enter the width of the rectangle: "))
    width = width_input_validation(width)
    gap = " " * (width-2)

    print(symbol * (width))

    for _ in range(height-2):
        print(symbol, end="")
        print(gap, end="")
        print(symbol)

    print(symbol * (width))


def main():
    rectangle_drawer()


main()
