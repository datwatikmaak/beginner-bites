from typing import List, TypeVar
import math

T = TypeVar('T', int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    digits = []
    for num in numbers:
        if num > 0:
            digits.append(int(math.log10(num)) + 1)
        elif num == 0:
            digits.append(1)
        else:
            digits.append(int(math.log10(-num)) + 2)  # +1 if you don't count the '-'

    print(digits)


n_digit_numbers([-1.1, 2.22, -3.333], 2)
