for i in range(1,13):
     print("No.{0} squared is {1} and cubed is {2}".format(i, i **2, i**3))
     print("No.{0:2} squared is {1:3} and cubed is {2:4}".format(i, i **2, i**3))

print()
for i in range(1,13):
     print("No.{0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i **2, i**3))
# this will left align the numbers

     print("No.{0:2} squared is {1:^3} and cubed is {2:^4}".format(i, i **2, i**3))
#      this will center align them

print ( "pi is approximately {0:12}".format(22 / 7))      # 12 defaults your formatting to 12 decimals
print ( "pi is approximately {0:12f}".format(22 / 7))     # 12f will be 6 digits after the decimal points
print ( "pi is approximately {0:12.50f}".format(22 / 7))  # add a precision, 50 points after decimal , precision is more important than field width so will ignore the 12
print ( "pi is approximately {0:52.50f}".format(22 / 7))  # the effect becomes clear
print ( "pi is approximately {0:62.50f}".format(22 / 7))  #
print ( "pi is approximately {0:72.50f}".format(22 / 7))  #
print ( "pi is approximately {0:<72.50f}".format(22 / 7))
print ( "pi is approximately {0:<72.54f}".format(22 / 7))

# field number is optional

for i in range(1,13):
    print("No.{} squared is {} and cubed is {:4}".format(i, i **2, i**3))
# without field number is enough