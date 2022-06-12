import random


def play():
    continue_playing = True
    player_score = 0
    cpu_score = 0
    while continue_playing:
        player_choice = input(
            "Enter a choice ( rock, paper, scissors )").title()

        if player_choice not in ("Rock", "Paper", "Scissors", "R", "r", "P", "p", "S", "s"):
            print("Enter a valid choice")
        cpu_choice = random.choice(("Rock", "Paper", "Scissors"))

        if player_choice == cpu_choice:
            print(
                f"You chose {player_choice}, and CPU chose {cpu_choice}. Its a Tie!")
            print(f"Your score: {player_score}. \n CPU score: {cpu_score}.")
        elif player_choice == "Rock" and cpu_choice == "Paper":
            print(
                f"You chose {player_choice}, and CPU chose {cpu_choice}. You Lose! CPU Wins!")
            cpu_score += 1
            print(f"Your score: {player_score}. \n CPU score: {cpu_score}.")
        elif player_choice == "Rock" and cpu_choice == "Scissors":
            print(
                f"You chose {player_choice}, and CPU chose {cpu_choice}. You Win! CPU Loses!")
            player_score += 1
            print(f"Your score: {player_score}. \n CPU score: {cpu_score}.")
        elif player_choice == "Paper" and cpu_choice == "Scissors":
            print(
                f"You chose {player_choice}, and CPU chose {cpu_choice}. You Lose! CPU Wins!")
            cpu_score += 1
            print(f"Your score: {player_score}. \n CPU score: {cpu_score}.")
        elif player_choice == "Paper" and cpu_choice == "Rock":
            print(
                f"You chose {player_choice}, and CPU chose {cpu_choice}. You Win! CPU Loses!")
            player_score += 1
            print(f"Your score: {player_score}. \n CPU score: {cpu_score}.")
        elif player_choice == "Scissors" and cpu_choice == "Rock":
            print(
                f"You chose {player_choice}, and CPU chose {cpu_choice}. You Lose! CPU Wins!")
            cpu_score += 1
            print(f"Your score: {player_score}. \n CPU score: {cpu_score}.")
        elif player_choice == "Scissors" and cpu_choice == "Paper":
            print(
                f"You chose {player_choice}, and CPU chose {cpu_choice}. You Win! CPU Loses!")
            player_score += 1
            print(f"Your score: {player_score}. \n CPU score: {cpu_score}.")

        play_again = input("Will you Play again some more?")
        if play_again == "Yes" or play_again == 'yes' or play_again == 'y' or play_again == 'Y':

            continue_playing = True
        elif play_again == "No" or play_again == 'no' or play_again == 'n' or play_again == 'N':
            continue_playing = False
            print("Thank you for playing")
            print('game over')
            break

        else:
            print("enter a valid choice!")


def game_start():
    print("\n")
    print("----------------------- Welcome to --------------------------")
    print('\n')
    print("------ROCK -------------- PAPER -------------- SCISSORS------")
    print('\n')
    begin = input("Would you like to play?")
    if begin == "Yes" or begin == "yes" or begin == "y" or begin == 'Y':
        play()
    elif begin == "No" or begin == "no" or begin == "n" or begin == 'N':
        print("Game Over")
    else:
        print("Please enter a valid choice")


if __name__ == "__main__":
    game_start()
