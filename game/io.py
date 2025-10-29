from game.logic import GameState, score_guess


def prompt_guess(length: int) -> str:
    return input(f"Enter your guess ({length} digits): ").strip()



def print_feedback(guess: str, bulls: int, cows: int) -> None:
    print(f"Your guess: {guess} | Bulls: {bulls}, Cows: {cows}")



def print_status(state: GameState) -> None:
    print(f"\nAttempts: {state['attempts']}/{state['max_attempts']}")
    print("Previous guesses:")
    for guess in sorted(state['history']):
        bulls, cows = score_guess(state['secret'], guess)
        print(f"  {guess} -> Bulls: {bulls}, Cows: {cows}")


def print_result(state: GameState, won: bool) -> None:
    if won:
        print("\nCongratulations! You've guessed the secret code:", state['secret'])
    else:
        print("\nGame over. The secret code was:", state['secret'])


