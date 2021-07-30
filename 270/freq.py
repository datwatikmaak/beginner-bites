from collections import Counter


def freq_digit(num: int) -> int:
    # using Counter().most_common() to get a list of tuples with the most common digits
    counting_digits = Counter(str(num)).most_common()

    # create a list with the first item from the list of tuples = list with one string
    most_frequent = list(list(zip(*counting_digits))[0][0])

    return int("".join(most_frequent))
