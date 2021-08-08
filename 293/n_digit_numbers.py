from typing import List, TypeVar
T = TypeVar('T', int, float)


def convert(num, n):
    # check if num is negative
    # solve problem with decimal numbers
    if num < 0:
        # needs to be string, int isn't subscriptable
        # directly convert back to int
        return int(str(num * 10 ** n)[:n+1])
    else:
        return int(str(num * 10**n)[:n])


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    # raise ValueError if n <= 0
    if n <= 0:
        raise ValueError
    # else loop over numbers and use convert function to create new digits
    return [convert(num, n) for num in numbers]
