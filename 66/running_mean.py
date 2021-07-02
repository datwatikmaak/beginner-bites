import itertools


def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""

    sums = itertools.accumulate(sequence)
    averages = [accum / i for i, accum in enumerate(sums, start=1)]

    return [round(elem, 2) for elem in averages]


running_mean(sequence=[1, 2, 3])
