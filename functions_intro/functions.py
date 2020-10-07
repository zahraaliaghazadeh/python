# def multiply():
#     result = 10.5 * 4
#     return result

def multiply(x: float, y: float) -> float:
    """
   Multiply 2 numbers.
   Although this function is intended to multiply 2 numbers,
   you can also use it to multiply a sequence.  If you pass
   a string, for example, as the first argument, you'll get
   the string repeated `y` times as the returned value.
   :param x: The first number to multiply.
   :param y: The number to multiply `x` by.
   :return: The product of `x` and `y`.
   """
    result = x * y
    # return result


answer = multiply(10.5, 4)
print(answer)
# There should always be two blank lines before and after functions

forty_two = multiply(6, 7)
print(forty_two)

print()

for val in range(1, 5):
    two_times = multiply(2, val)
    print(two_times)

# call by sharing and call by reference
# https://docs.python.org/3/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference
# https://en.wikipedia.org/wiki/Evaluation_strategy#Call_by_sharing

# palindrome use in genetics
# https://pubmed.ncbi.nlm.nih.gov/11700586/
# https://www.sciencedirect.com/science/article/pii/S0304397508008852


# palindrome function
def is_palindrome(string: str) -> bool:
    """
    Check if a string is a palindrome.
    A palindrome is a string that reads the same forwards as backwards.
    :param string: The string to check.
    :return: True if `string` is a palindrome, False otherwise.
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


# word = input("Please enter a word to check: ")
# if is_palindrome(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))

    # three string methods can be used for the uppercase bug
    # .upper and .lower and .casefold to use


#     To check if sentence is palindrome
#  hint: use isalnum() and isalpha() from the string methods
def palindrome_sentence(sentence: str) -> bool:
    """
    Check if a sentence is a palindrome.
    The function ignores whitespace, capitalisation and
    punctuation in the sentence.
    :param sentence: The sentence to check.
    :return: True if `sentence` is a palindrome, False otherwise.
    """
    string = ""
    for char in sentence:
        if char.isalnum():
             string += char
             # print(string)
    return string[::-1].casefold() == string.casefold()


# word = input("Please enter a word to check: ")
# if palindrome_sentence(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))
# "was it a car or a cat i saw" , is a palindrome

answer = multiply(18, 3)
print(answer)
# this function does not return anything , it says None if
# you comment out return in multiply function


def fibonnacci(n: int) -> int:
    """Return the `n` th Fibbonacci number, for positive `n`."""
    # Economy of Expression 7.2.5, in the Python documents
    # put a space after ` because single alphabets will show a back tick right before n
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n-1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result
    return result
# error: local variable result might be referenced before assignment
# you gotta handle negative numbers for this error to go away


for i in range(36):
    print(i, fibonnacci(i))
# ctrl J after highlighting fibonnacci


p = is_palindrome()
q = palindrome_sentence()

# q = palindrome_sentence(654)
# it is good so that intelliJ will give error warnings of typehints