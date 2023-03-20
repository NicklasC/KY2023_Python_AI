from random import randint

player_selection = ""


def generate_computer_selection():
    computer_selection = randint(0, 2)
    if computer_selection == 0:
        return "rock"
    elif computer_selection == 1:
        return "paper"
    else:
        return "sissor"


def player_won(computer_selection):
    print(f"Computer chose {computer_selection}. Player wins!")
    exit(0)


def computer_won(computer_selection):
    print(f"Computer chose {computer_selection}. Computer wins!")
    exit(0)


def noone_won():
    print("Computer chose the same as you. Try again!")


print('Rock paper sizzors game!')

while player_selection.capitalize() != "Q":
    print("rock paper or sissor? You choose! Press q to quit.")
    print(">>", end="")

    player_selection = input().lower()

    if player_selection == "rock" or player_selection == "paper" or player_selection == "sissor":

        computer_selection = generate_computer_selection()

        if player_selection == "rock":
            if computer_selection == "sissor":
                player_won(computer_selection)
            elif computer_selection == "rock":
                noone_won()
            else:
                computer_won(computer_selection)
        elif player_selection == "paper":
            if computer_selection == "sissor":
                computer_won(computer_selection)
            elif computer_selection == "rock":
                player_won(computer_selection)
            else:
                noone_won()
        elif player_selection == "sissor":
            if computer_selection == "sissor":
                noone_won()
            elif computer_selection == "rock":
                computer_won(computer_selection)
            else:
                player_won(computer_selection)
    else:
        print("Invalid input! Please try again.")
