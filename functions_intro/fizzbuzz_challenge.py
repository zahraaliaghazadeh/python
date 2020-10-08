input("Play Fizz Buzz.  Press ENTER to start.")
print()
next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go: ")
    if players_answer != correct_answer:
        print(f"You lose, the correct answer was {correct_answer}")
        break
else:
    print(f"Well done, you reached {next_number}")