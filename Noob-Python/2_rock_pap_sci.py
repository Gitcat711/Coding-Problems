from random import randint
player_win = 0
computer_win = 0
winning_score = 3

while player_win < winning_score and computer_wins < winning_score:
    print(f"Player Score: {player_win} Computer Score: {computer_wins}")
    print("Rock/Paper/Scissors")

    player = input("Enter your choice): ").lower()
    if player == ("quit" or "q"):
        break
    random_num =  randint(0,2)
    if(random_num == 0):
        computer == "rock"
    if(random_num == 1):
        computer == "paper"
    else:
        computer == "scissors"

    print(f"The computer plays: {computer}")

    if player == computer:
        print("It's a Tie!")
    elif player == "rock":
        if computer == "paper":
            print("Computer Got You!!")
            computer_wins += 1
        else:
            print("You Win")
            player_wins += 1
    else:
        print("Enter valid move, dumba**")

if player_wins > computer_wins:
    print("Congrats, You Won")
elif player_wins == computer_wins:
    print("It's a Tie")
else:
    print("The Computer Won, Machine taking humanity")


