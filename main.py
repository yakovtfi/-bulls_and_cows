from game.secret import generate_secret
from game.logic import init_state, apply_guess
from game.validate import is_valid_guess, is_new_guess
from game.io import print_status, prompt_guess, print_feedback, print_result

def play(length: int = 4, max_tries: int | None = 12, *, unique_digits: bool = True, allow_leading_zero: bool = False) -> None:
    secret = generate_secret(length, unique_digits=unique_digits, allow_leading_zero=allow_leading_zero)
    state = init_state(secret, length, max_tries, unique_digits, allow_leading_zero)

    while state['attempts'] < state['max_attempts']:
        print_status(state)
        guess = prompt_guess(length)

        is_valid, error_msg = is_valid_guess(guess, length, unique_digits=unique_digits)
        if not is_valid:
            print("Invalid guess:", error_msg)
            continue

        if not is_new_guess(guess, state['history']):
            print("You've already guessed that number. Try again.")
            continue

        bulls, cows = apply_guess(state, guess)
        print_feedback(guess, bulls, cows)

        if bulls == length:
            print_result(state, won=True)
            return

    print_result(state, won=False)


if __name__ == "__main__":
    play()
