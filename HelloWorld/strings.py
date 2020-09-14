print("Today is a good day to learn python")
print('python is fun')
print("Python 's string are easy to use")
print('We can even include "quotes" in strings')
print("hello" + "world")
greeting = "Hello"
# the input function is done first , when it finishes input then assigns it to name
# name = input("Please enter your name")

# name = "Bruce"
# if we want a space we can add that too
# print(greeting + ' ' + name)

splitString = "This string has been \nsplit over \nseveral \n lines"
print(splitString)
tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)
print('The pet shop owner said "No, no \'e\'s uh,...he\'s resting".')
print("The pet shop owner said \"No, no 'e's uh,...he's resting\".")
# using triple " no need to escape with \
print("""The pet shop owner said "No, no 'e's uh,...he's resting".""")
print("""The pet shop owner said "No, no \
'e's uh,...he's resting".""")

# prints on several lines
# anotherSplitString = """ This string has been
# split over
# several
# lines"""

# prints in one line
anotherSplitString = """ This string has been \
split over \
several \
lines"""

print(anotherSplitString)

# it is interpretting \t as tab and \n as new lines
# print("C:\Users\timbuchalka\notes.txt")

# raw strings by using r, and 2 backslashes
print(r"C:\\Users\\timbuchalka\\notes.txt")


age=24
print(age)

# print(type(greeting))
# print(type(age))

# age_in_words = " 2 years"
# print(name + "is" + age + "years old")
# print(type(age))
# will give error

parrot = "Norwegian Blue"
print(parrot[0])  #N

print ( parrot[3] + parrot[4] + " " +parrot[3] + parrot[6] + parrot[8] + ".")

print(parrot[-1])
print(parrot[-14])

print()
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])
# you ll get the same by negative , by subtracting 14


print(parrot[0:6]) # Norweg (it will slice up to but not including the last character)

print(parrot[3:5]) #
# these two have the same result
print(parrot[0:9])
print(parrot[:9])

print(parrot[10:14])
print(parrot[10:])
# the : is important , because otherwise it will be an index

# if the first is omitted from the beginning and
# if the second is omitted runs to the end of

print(parrot[:6])
print(parrot[6:])

print(parrot[:6] + parrot[6:])

print(parrot[:])

letters = "abcdefghijklmnopqrstwxyz"

# print(parrot[-4:2]) cant go back from the start
print(parrot[-4:-2]) # Bl
print(parrot[-4:12]) # Bl

print(parrot[0:6])      # Norweg
print(parrot[-14:-8])   # Norweg

print(parrot[0:6:2])    # Nre
print(parrot[0:6:3])    # Nw   #we step through the sequence in steps of 3

number1 ="9,223,372,036,854,775,807"
print(number1[1::4])

number2 ="9,223;372:036 854,775;807"
print(number2[1::4])

separators = number2[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number2).split()
print([int(val) for val in values])


# f string, just instead of using .format can use this
name = "Tim"
age_in_words = "2 years"
print(name + f" is { age} years old")
print(type(age))

print ( f"Pi is approximately {22/7:12.50f}")
pi = 22/7
print ( f"Pi is approximately {pi:12.50f}")

# string interpolation , like print f in C

# quiz question
print()
days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print (days[::5])  #MTWTFSS










