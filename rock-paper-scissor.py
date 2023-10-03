import random
import os
os.system('cls')
player_wins = 0
computer_wins = 0
tied_amount = 0
options = ["R", "P", "S"]

while True:
    press = input("Press Q to quit, P to play. ").upper()
    if press == "Q":
        print("Goodbye!!!")
        break
    elif press == "P":
        player_move = input(
            "\nPress R for rock, P for paper, S for scissors. \n").upper()
        move_relation = {"R": "✊", "P": "🫱", "S": "✌️"}
        random_number = random.randint(0, 2)
        computer_move = options[random_number]
        if player_move not in options:
            continue
        else:
            print(
                f"You picked {move_relation[player_move]}. The computer picked {move_relation[computer_move]}.")
            if player_move == computer_move:
                print("It's a tie. \n ")
                tied_amount += 1
            else:
                if player_move == "R" and computer_move == "P":
                    player_state = "lost"
                    computer_state = "won"
                elif player_move == "R" and computer_move == "S":
                    player_state = "won"
                    computer_state = "lost"
                elif player_move == "P" and computer_move == "R":
                    player_state = "won"
                    computer_state = "lost"
                elif player_move == "P" and computer_move == "S":
                    player_state = "lost"
                    computer_state = "won"
                elif player_move == "S" and computer_move == "R":
                    player_state = "lost"
                    computer_state = "won"
                elif player_move == "S" and computer_move == "P":
                    player_state = "won"
                    computer_state = "lost"
                print(
                    f"You {player_state}. The computer {computer_state}." + "\n")
                if player_state == "won":
                    player_wins += 1
                elif computer_state == "won":
                    computer_wins += 1
        print(f"Your wins: {player_wins}.")
        print(f"Computer wins: {computer_wins}.")
        print(f"Tie: {tied_amount}" + "\n")
    else:
        continue  # restarts the loop
