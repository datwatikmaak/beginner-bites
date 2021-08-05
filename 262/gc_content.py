from collections import Counter


def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    counter = Counter(sequence.lower())
    a = counter["a"]
    c = counter["c"]
    g = counter["g"]
    t = counter["t"]

    return round((g + c) / (a + t + g + c) * 100, 2)
