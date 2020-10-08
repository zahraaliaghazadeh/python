import math


def main():
    """

    :return:
    """
    height = int(input("Please Enter a height: "))
    if(height % 2 == 0):
        print("Your input should be an odd number.")
    else:
        print(" " * int(height/2) + "*")
        for h in range(int(height/2)-1):
            for _ in range(h * -1 + int(height/2)-1):
                print(" ", end="")
            print("/", end="")
            for i in range(h*2 + 1):
                print(" ", end="")
            print("\\")
        print("/", end="")
        print((height-2) * "_", end="")
        print("\\")


main()


# print((" " * (int(height/2)-1)) + "/"+ (" " * int(height/2) * 2) + "\\" + (" " * (int(height/2)-1)))
#     *
#    / \
#   /   \
#  /     \
# /_______\
