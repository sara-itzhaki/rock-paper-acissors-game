import random


def get_winner(user_choice: str, computer_choice: str) -> str:
    """
    Determines the winner based on the classic game rules.

    Args:
        user_choice (str): The choice made by the player (rock, paper, or scissors).
        computer_choice (str): The randomly generated choice by the computer.

    Returns:
        str: A message indicating whether it's a win, loss, or tie.
    """
    if user_choice == computer_choice:
        return "It's a tie!"
    win_conditions: dict[str, str] = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }

    if win_conditions[user_choice] == computer_choice:
        return "You win! Well done."
    else:
        return "The computer wins. Maybe next time!"


def play_game() -> None:
    """
    Main function to run the game loop and handle user interaction.
    """
    options: list[str] = ['rock', 'paper', 'scissors']

    print("--- Welcome to Rock, Paper, Scissors! ---")

    while True:
        user_input: str = input(
            "\nEnter rock, paper, or scissors [or 'q' to quit]: ").lower()

        if user_input == 'q':
            print("Thanks for playing! Goodbye.")
            break

        if user_input not in options:
            print("Invalid choice, please try again.")
            continue

        computer_choice: str = random.choice(options)
        print(f"The computer chose: {computer_choice}")

        result: str = get_winner(user_input, computer_choice)
        print(result)


if __name__ == "__main__":
    play_game()
