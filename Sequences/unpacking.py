a = b = c = d = e = f = 12
print(c)

x, y = 1, 2
print(x)
print(y)

print("Unpacking a tuple")

# this on the right is a tuple
x, y, z = 1, 2, 6
print(x)
print(y)
print(z)


print("Unpacking a list")
data_list = [12, 13, 14]
# data_list.append(15) # too many values to unpack (expected 3), you have to have as many variables or it will break
p, q, r = data_list
print(p)
print(q)
print(r)