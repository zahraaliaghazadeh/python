from nested_data import albums

# print(albums)
# this will execute the code in nested_data

# Constants
# they will not change their value , to tell that they are constant
# Their index in the data
SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    # print("Please choose your album (invalid choice exists):")
    # for index, (title, artist, year, songs) in enumerate(albums):
    #     print("{}: {}, {}, {}, {}"
    #           .format(index + 1, title, artist, year, songs))
    # break

    # for index, value in enumerate(albums):
    #     title, artist, year, songs = value
    #     print(index, title, artist, year, songs)
    # break

    print("Please choose your album (invalid choice exists):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title))

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]
    else:
        break

    # print(albums[choice - 1])
    # print(songs_list)
    # print()

    print("Please choose your song:")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
        print("playing {}".format(title))
    #     there is no else statement so it will run the for loop again

    # else:
    #     break

         # print("playing {}".format(title))
         # print("=" * 40)
