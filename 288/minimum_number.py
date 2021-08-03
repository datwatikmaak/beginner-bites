from typing import List


def minimum_number(digits: List[int]) -> int:

    return 0 if not digits else int("".join(map(str, sorted(list(set(digits))))))
