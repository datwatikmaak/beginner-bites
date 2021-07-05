from itertools import combinations


def find_number_pairs(numbers, N=10):
    return [
        (var[0], var[1])
        for var in combinations(numbers, 2)
        if var[0] + var[1] == N
    ]