import math


def round_to_next(number: int, multiple: int):
    if number % multiple == 0:
        return math.floor(number / multiple) * multiple
    else:
        return (math.floor(number / multiple) + 1) * multiple
