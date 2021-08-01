from collections import Counter


def major_n_minor(numbers):
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """
    # major = (max(set(numbers), key=numbers.count))
    # minor = (min(set(numbers), key=numbers.count))

    major = Counter(numbers).most_common()[0][0]
    minor = Counter(numbers).most_common()[-1][0]

    return major, minor
