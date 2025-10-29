def is_valid_guess(guess: str, length: int, *, unique_digits: bool = True) -> tuple[bool, str]:
    if len(guess)!=length:
        return False, f"Guess must be exactly {length} digits long."
    if not guess.isdigit():
        return False, "Guess must only contain digits."

    if unique_digits and len(set(guess)) != length:
        return False, "Guess must have all unique digits."

    return True, ""
print(is_valid_guess("1245", 4, unique_digits=True))


def is_new_guess(guess: str, history: set[str]) -> bool:
    return guess not in history