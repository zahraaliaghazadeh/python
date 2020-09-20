flowers = {
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily"
}

# for flower in flowers
#       print(flower)

separator = " | "
output = separator.join(flowers)
print(output)

separator = ", "
output = separator.join(flowers)
print(output)
# we didn't have to do for loop here. The join method does it for us

separator = ", "
output = separator.join(flowers)
print(output)

print(",".join(flowers))

# if we add a number in the end of our list, join will give an error
# it can not join an int to a string
