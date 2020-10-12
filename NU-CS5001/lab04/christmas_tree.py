import math


def main():
    """
    This main function will get a height from the user input
    and draw a christmas tree with * , `\\` and `/`
    :return: This function returns a christmas tree drawn
    """
    height = int(input("Please Enter a height: "))
    if(height % 2 == 0):
        print("Your input should be an odd number.")
    else:
        # half way through the base line
        print(" " * int(height/2) + "*")
        # next line is the for loop for after the * up to the one before
        # the last line
        for h in range(int(height/2)-1):  # 0 1 2 3 for the entry of 9
            # these are for / s
            # 3 2 1 0 spaces for the entry of 9
            for _ in range(h * -1 + int(height/2)-1):
                print(" ", end="")
            print("/", end="")
            # the end \ s are printed with this
            for i in range(h*2 + 1):
                print(" ", end="")
            print("\\")

            # for the base of the tree
        print("/", end="")
        print((height-2) * "_", end="")
        print("\\")


main()
