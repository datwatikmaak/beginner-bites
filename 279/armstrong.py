def is_armstrong(n: int) -> bool:
    length = len(str(n))
    digits = sum(int(x)**length for x in str(n))

    return digits == n
