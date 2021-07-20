def countdown():
    """Write a generator that counts from 100 to 1"""
    for n in reversed(range(101)):
        if n > 0:
            yield n


countdown()
