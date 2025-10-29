import random
def generate_secret(length: int = 4, *, unique_digits: bool = True, allow_leading_zero: bool = False, rng: random.Random | None = None) -> str:
    if rng is None:
        rng=random
    digits=list('0123456789')

    if unique_digits:
        if length >10:
            raise ValueError("Cannot generate a unique digit code longer than 10 digits.")
        if not allow_leading_zero:
            first_digit=rng.choice(digits[1:])
            digits.remove(first_digit)
            remaining_digits = rng.sample(digits, length - 1 )
            secret_code = first_digit + ''.join(remaining_digits)
        else:
            secret_code = ''.join(rng.sample(digits, length - 1))
    else:
        if not allow_leading_zero:
            first_digit = rng.choice(digits[1:])
            remaining_digits = ''.join(rng.choices(digits, k=length -1 ))
            secret_code = first_digit + remaining_digits
        else:
            secret_code = ''.join(rng.choices(digits, k=length))

    return secret_code



def is_new_guess(guess: str, history: set[str]) -> bool:
    return guess not in history