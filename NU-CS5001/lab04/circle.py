import math


def main():
    """
    Gets a `radius` value from the user.
    :return: a circle drawn with `O`
    """
    radius = int(input("Enter a value for radius: "))
    for i in range(1, 2 * radius):
        line = ""
        for j in range(1, 2 * radius):
            if (math.sqrt((radius - j)**2 + (radius-i)**2) > radius):
                line += " "
            else:
                line += "o"
        print(line)


main()
