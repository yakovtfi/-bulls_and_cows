from typing import TypedDict


def score_guess(secret: str, guess: str) -> tuple[int, int]:
    bulls = sum(sec == gue for sec, gue in zip(secret, guess))
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls
    return bulls, cows


class GameState(TypedDict):
    secret: str
    length: int
    unique_digits: bool
    allow_leading_zero: bool
    max_attempts: int | float
    attempts: int
    history: set[str]


def init_state(secret: str, length: int, max_tries: int | None, unique_digits: bool, allow_leading_zero: bool) -> GameState:

    return {
        'secret': secret,
        'length': length,
        'unique_digits': unique_digits,
        'allow_leading_zero': allow_leading_zero,
        'max_attempts': max_tries if max_tries is not None else float('inf'),
        'attempts': 0,
        'history': set()
    }


def apply_guess(state: GameState, guess: str) -> tuple[int, int]:
    bulls, cows = score_guess(state['secret'], guess)
    state['attempts'] += 1
    state['history'].add(guess)
    return bulls, cows



