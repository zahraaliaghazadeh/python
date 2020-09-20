# welcome = "Welcome to my Nightmare", "Alic Cooper", 1975
# bad = "Bad Company", "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Emilda May", 2011
# metallica = "Ride the lightning", "Metallica", 1984
#
# print(metallica)
#
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
# # indexing works the same as lists, still use [] for it
#
# # metallica[0] = "something else" #will give an error  because:
# # 'tuple' object does not support item assignment
# # tuples are immutable
#
# metallica2 = list(metallica)
# print(metallica2)
# # this made it a list
# metallica2[0] = "Master of Puppets"
# print(metallica2)
# # now we can change in the list
#
#
# title, artist, year = metallica
# print(title)
# print(year)
# print(year)
#
# table = ("Coffee table", 200, 100, 75, 34.50)
# print(table[1] * table[2])
#
# name, length, width, height, price = table
# print(length * width)

albums = [ ("Welcome to my Nightmare", "Alic Cooper", 1975),
             ("Bad Company", "Bad Company", 1974),
             ("Nightflight", "Budgie", 1981),
             ("More Mayhem", "Emilda May", 2011),
             ("Ride the lightning", "Metallica", 1984)
           ]

print(len(albums))

for name, artist, year in albums:
    print("Album: {}, Artist: {}, Years: {}"
          .format(name, artist, year))
#     album[0] and 1 and 2 could be also mentioned hear

for album in albums:
    name, artist, year = album
    print("Album: {}, Artist: {}, Year: {}"
          .format(albums[0], albums[1], albums[2]))

# homogenous vs heterogenous
