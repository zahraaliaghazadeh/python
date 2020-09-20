available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction, otherwise type quit: ")
    # Quit will work as well
    if chosen_exit.casefold() == "quit":
        print("Game Over")
        break
else:
    print( "Aren't you glad you got out of there" )


