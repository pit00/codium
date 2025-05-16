"""https://exercism.org/tracks/r/exercises/luhn"""

import re
import numpy as np


def luhn(card) -> bool:
    """Credit card validation"""
    if isinstance(card, str):  # check if string
        card = card.replace(" ", "")  # trim spaces
        if re.fullmatch(r"\d{16}", card):  # check if 16 digits
            # Get digits at odd positions
            odd_digits = np.array([int(card[i]) for i in range(0, len(card), 2)])
            odd_digits = odd_digits * 2
            odd_digits = np.where(odd_digits > 9, odd_digits - 9, odd_digits)

            # Get digits at even positions
            even_digits = np.array([int(card[i]) for i in range(1, len(card), 2)])

            sum_digits = sum(odd_digits) + sum(even_digits)

            if sum_digits % 10 == 0:
                # print("Valid credit card number")
                return True

    # print("Invalid credit card number")
    return False


luhn("4539 3195 0343 6467")  # True
luhn("8273 1232 7352 0569")  # False
luhn("8273 123A 7352 0569")  # False
luhn("8273 123227352 0569")  # False
