from projects.modules import rps_game as rps


def main():
    again = "y"
    print("Rock, Paper, Scissors Game")
    while again.lower() == "y":
        computer = rps.computer_choice()
        player = rps.player_choice()
        computer_output, player_output = rps.output(computer, player)
        print()
        print(computer_output)
        print(player_output)
        print(rps.game(computer, player))
        print()
        again = input("Do you want to play again? \nY = yes, anything else = no: ")


if __name__ == '__main__':
    main()
