CM_PER_INCH = 2.54


def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    if fmt in {"cm", "CM"}:
        return round(value * CM_PER_INCH, 2)
    elif fmt in {"in", "IN"}:
        return round(value / CM_PER_INCH, 4)
    else:
        raise ValueError
