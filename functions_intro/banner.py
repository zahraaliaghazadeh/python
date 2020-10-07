# def banner_text(text=" ", screen_width=80):
def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """ Print a string centred, with ** either side.
    :param text: The string to print.
       An asterisk (*) will result in a row of asterisks.
       The default will print a blank line, with a ** border at
       the left and right edges.
   :param screen_width: The overall width to print within
       (including the 4 spaces for the ** either side).
   :raises ValueError: if the supplied string is too long to fit.
   """
    # when combining argument annotation and default value use space around =
    # either use annotation on all or don't use it at all

    # screen_width = 80
    # screen_width = 50
    if len(text) > screen_width - 4:
        # To raise an exception in Python
        raise ValueError("String {0} is larger than specified width {1}"
                         .format(text, screen_width))
        # print("EEK!!")
        # print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")

    if text == "*":
        print("*" * screen_width)
    else:
        centered_text = text.center(screen_width -4)
        output_string = "**{0}**".format(centered_text)
        print(output_string)

# you have to put , 66 after the "" in these if you want to have
# a value for the 2 arguments, but when you put a default value
# inside the function definition, you dont have to pass in that value
# in the execution
banner_text("*")
banner_text("Always look on the bright side of life...")
banner_text("If life seems jolly rotten,")
banner_text("There s something you ve forgotten!")
banner_text("And that s to laugh and smile and dance and sing")
# if nothing is passed here you need to pass a default value for text
banner_text()
banner_text(screen_width=60)
banner_text("When you are feeling in the dumps")
banner_text("Don't be silly chumps,")
banner_text("Just purse your lips and whistle - that s the thing")
banner_text("And...always look on the bright side of life...")
banner_text("*")

    # result = banner_text("Nothing is returned")
    # print(result)
    #
    # numbers = [4, 4, 7, 5, 8, 3, 9, 6, 1]
    # print(numbers.sort())

# Tele Type
# Punch Card
# ANSI sequence
# ANSI escape code
