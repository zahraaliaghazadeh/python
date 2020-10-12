
def height_input_validation(height):
    """
    This function is to make sure height is less than 2
    :param height: user will input the height of rectangle
    :return: while loop will return the valid height value
    """
    while (height <= 2):
        height = int(input("Your value is too small! Enter again: "))
    return height


def width_input_validation(width):
    """
    This function is to make sure width         is less than 2
    :param width: user will enter a width for rectangle
    :return: while loop will return the valid width
    """
    while (width <= 2):
        width = int(input("Your value is too small! Enter again: "))
    return width


def rectangle_drawer():
    """
    This function gets a symbol, a height and a width from the user and
    it will then draw a rectangle with the symbol.

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
    """

    :return: calling the rectangle_drawer function.
    """
    rectangle_drawer()


main()
