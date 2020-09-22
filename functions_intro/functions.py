# def multiply():
#     result = 10.5 * 4
#     return result

def multiply(x, y):
    result = x * y
    return result


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
def is_palindrome(string):
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
def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
             string += char
             # print(string)
    return string[::-1].casefold() == string.casefold()


word = input("Please enter a word to check: ")
if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))
# "was it a car or a cat i saw" , is a palindrome