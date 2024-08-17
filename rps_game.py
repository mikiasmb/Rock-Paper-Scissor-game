import random


def computer_choice():
    choice = ["Rock", "Paper", "Scissors"]
    computer = random.choice(choice)
    return computer


def player_choice():
    print("Select one to play")
    print("1.Rock 2.Paper 3.Scissors")
    try:
        player = int(input("Enter: "))
        if player in [1, 2, 3]:
            if player == 1:
                return "Rock"
            elif player == 2:
                return "Paper"
            elif player == 3:
                return "Scissors"
    except TypeError:
        print("Error: Type error.")
    except ValueError:
        print("Error: Value error input must be 1,2 or 3.")


def output(c, p):
    computer = f"Computer choice {c}"
    player = f"Player choice {p}"
    return computer, player


def game(c, p):
    if c == "Paper" and p == "Rock":
        return "Computer win\nPaper wraps Rock."
    elif c == "Rock" and p == "Paper":
        return "Player win\nPaper wraps Rock."
    elif c == "Rock" and p == "Scissors":
        return "Computer win\nRock smashes Scissors."
    elif c == "Scissors" and p == "Rock":
        return "Player win\nRock smashes Scissors."
    elif c == "Scissors" and p == "Paper":
        return "Computer win\nScissors cut Paper."
    elif c == "Paper" and p == "Scissors":
        return "Player win\nScissors cut Paper."
    elif c == p:
        return "Tie try again."
