import random

def play_game():
    """
    Plays a game of Rock-Paper-Scissors against the computer using a while loop.
    """
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    # Start the game loop
    while True:
        # Get user input
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to end): ").lower()

        if user_choice == "quit":
            break  # Exit the while loop

        if user_choice not in choices:
            print("Invalid input. Please try again.")
            continue  # Skip to the next iteration of the loop

        # Get computer choice
        computer_choice = random.choice(choices)
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1
        
        # Display scores
        print(f"Score -> You: {user_score}, Computer: {computer_score}\n")

    # Game over
    print(f"\nGame over. Final Score -> You: {user_score}, Computer: {computer_score}")

if __name__ == "__main__":
    play_game()
