def cap_vowels(sentence):
    answer = ""
    for letter in sentence:
        # check for vowels and make them uppercase
        if letter in "aeiouAEIOU":
            answer = answer + letter.upper()
        # check for consonants and make them uppercase
        else:
            answer = answer + letter.lower()
    return answer


print(cap_vowels(input("Enter a sentence: ")))


# def cap_vowels():
#     sentence = input("Enter a sentence: ")
#     vowels = "aeiouAEIOU"
#     answer = ""
#     for letter in sentence:
#         # check for vowels and make them uppercase
#         if letter in vowels:
#             answer = answer + letter.upper()
#         # check for consonants and make them uppercase
#         else:
#             answer = answer + letter.lower()
#     return answer


# print(cap_vowels())
