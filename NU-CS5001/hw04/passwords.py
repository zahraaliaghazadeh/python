# Zahra Ali Aghazadeh
# This function takes first name and last name and a favortie
# word from the user and then it creates a username and 3
# diverse suggested passwords.
import math
import random
UP_BOUND_RANDOM = 99
# Actually this is: 3! Ways to sort three things + 1
WAYS_TO_SORT_THREE = 7
# since randint is inclusive we have 6 , and not 7
MIN_LN_LEN = 6


def passwords():
    """ function prompts the user for `first_name`, `last_name`
    and their `favorite_word`. It will then create a user name
    and 3 suggested passwords for them.
    :return: returns 4 strings(1 username and 3 passwords).
    """
    print("Welcome to the username and password generator!")
    # User prompts
    first_name = input("Please Enter your first name: ")
    last_name = input("Please Enter your last name: ")
    favorite_word = input("Please Enter your favorite word: ")
    # user_name
    number_1_str = str(random.randint(1, UP_BOUND_RANDOM))
    while (len(last_name) < MIN_LN_LEN):
        last_name = last_name + ("*" * (MIN_LN_LEN-len(last_name)))
    user_name = (first_name[0].lower() + last_name[0:MIN_LN_LEN].lower()
                 + number_1_str)
    print("Thanks {}, your username is ".format(first_name) + user_name)
    # password_1
    # convert the first and last name to lowercase
    password_1_starter = (first_name.lower()
                          + str(random.randint(1, UP_BOUND_RANDOM))
                          + last_name.lower())
    password_1 = ""
    # loop through the lowercased string and
    # substitute certain alphabets with characters
    for c in password_1_starter:
        if c == "a":
            password_1 += "@"
        elif c == "o":
            password_1 += "0"
        elif c == "l":
            password_1 += "1"
        elif c == "s":
            password_1 += "$"
            # 2 extra conditions below
        elif c == "q":
            password_1 += "9"
        elif c == "h":
            password_1 += "#"
        else:
            password_1 += c
    print("Password 1: " + password_1)
    # password 2
    # lowercase first letters and uppercase last letters
    # then concat them in order
    # 0 slices the first char and -1 slices the last
    password_2 = (first_name[0].lower()
                  + first_name[-1].upper()
                  + last_name[0].lower()
                  + last_name[-1].upper()
                  + favorite_word[0].lower()
                  + favorite_word[-1].upper())
    print("Password 2 : " + password_2)
    # password 3
    random_length_fn = random.randint(1, len(first_name))
    random_length_ln = random.randint(1, len(last_name))
    random_length_fw = random.randint(1, len(favorite_word))
    # There are 6 ways to sort 3 things
    # Below are the conditions for each generated random number
    random_choice = random.randint(1, WAYS_TO_SORT_THREE)
    if (random_choice == 1):  # 1 2 3
        password_3 = (first_name[:random_length_fn]
                      + last_name[:random_length_ln]
                      + favorite_word[:random_length_fw])
    elif(random_choice == 2):  # 2 1 3
        password_3 = (last_name[:random_length_ln]
                      + first_name[:random_length_fn]
                      + favorite_word[:random_length_fw])
    elif(random_choice == 3):  # 3 1 2
        password_3 = (favorite_word[:random_length_fw]
                      + first_name[:random_length_fn]
                      + last_name[:random_length_ln])
    elif(random_choice == 4):  # 3 2 1
        password_3 = (favorite_word[:random_length_fw]
                      + last_name[:random_length_ln]
                      + first_name[:random_length_fn])
    elif(random_choice == 5):  # 2 3 1
        password_3 = (last_name[:random_length_ln]
                      + favorite_word[:random_length_fw]
                      + first_name[:random_length_fn])
    elif(random_choice == 6):  # 1 3 2
        password_3 = (first_name[:random_length_fn]
                      + favorite_word[:random_length_fw]
                      + last_name[:random_length_ln])
    print("Password 3: " + password_3)


def main():
    "main is to call our function"
    passwords()


main()
