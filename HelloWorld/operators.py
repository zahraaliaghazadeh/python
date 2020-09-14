a = 12
b = 3

print ( a + b)   # 15
print ( a - b)   # 9
print ( a * b)   # 36
print ( a / b)   # 4.0 result is float
print ( a // b)  # 4 integer division, rounded down towards minus infinity , result is integer
print ( a % b)   # 0 modulo: the remainder after integer division

print() # empty line

for i in range(1, 4):
    print(i)

for i in range(1, a//b):
    print(i)

for i in range(1, a/b):
    print(i) # will give a warning about int vs float

    # i=1
    # print(i)
    # i=2
    # print(i)
    # i=3
    # print(i)


