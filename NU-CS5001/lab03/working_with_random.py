import random

num = random.random()
print("Random number between 0.0 and 1.0:", num)

num = random.randint(5, 20)
print("Random integer between 5 and 20: ", num)

my_string = "Hello World!"
print("A random character picked from", my_string + ":",
      random.choice(my_string))

print(random.choice(["red", "yellow", "green", "blue"]))
