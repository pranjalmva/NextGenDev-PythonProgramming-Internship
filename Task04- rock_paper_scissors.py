import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice! Please try again.")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}\n")

    result = determine_winner(user_choice, computer_choice)
    print(result)

def play_again():
    while True:
        response = input("Do you want to play again? (y/n): ").lower()
        if response == "y":
            return True
        elif response == "n":
            return False
        else:
            print("Invalid response! Please try again.")

def main():
    print("Welcome to Rock Paper Scissors!")
    print("Enter 'rock', 'paper', or 'cissors' to make your choice.")

    score = {"user": 0, "computer": 0}

    while True:
        play_game()
        if determine_winner(get_user_choice(), get_computer_choice()) == "You win!":
            score["user"] += 1
        elif determine_winner(get_user_choice(), get_computer_choice()) == "Computer wins!":
            score["computer"] += 1

        print(f"\nScore - User: {score['user']}, Computer: {score['computer']}\n")

        if not play_again():
            break

if __name__ == "__main__":
    main()