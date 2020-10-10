# Create a progrma that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.

# you can either enter the text from the keyboard or initialise
# a string variable with the string

sampleText = "Python is a very powerful"

vowels = frozenset("aeiou")
# vowels = {"a", "e", "i", "o", "u"}
finalSet = set(sampleText).difference(vowels)
print(finalSet)

finalList = sorted(finalSet)
print(finalList)