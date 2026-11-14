import random

MOVES = ["rock", "paper", "scissors"]


def winner(player, computer):
    if player == computer:
        return "draw"
    if (player == "rock" and computer == "scissors") or \
       (player == "paper" and computer == "rock") or \
       (player == "scissors" and computer == "paper"):
        return "win"
    return "lose"


def main():
    score = {"player": 0, "cpu": 0}
    print("Game: rock, paper, scissors")
    print("Enter your move (rock, paper, scissors) or 'quit' to exit.\n")

    while True:
        player = input("Your move: ").strip().lower()

        if player == "quit":
            print("BYE.")
            break

        if player not in MOVES:
            print("Invalid option. Use: rock, paper, or scissors.")
            continue

        computer = random.choice(MOVES)
        result = winner(player, computer)

        if result == "win":
            score["player"] += 1
            print(f"You chose {player} | CPU chose {computer} -> You win!")
        elif result == "lose":
            score["cpu"] += 1
            print(f"You chose {player} | CPU chose {computer} -> CPU wins!")
        else:
            print(f"You chose {player} | CPU chose {computer} -> Draw!")

        print(f"Score: You {score['player']} - {score['cpu']} CPU\n")


if __name__ == "__main__":
    main()
