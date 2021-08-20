def positive_divide(numerator, denominator):

    try:
        result = numerator / denominator

        if result < 0:
            raise ValueError

        if not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
            raise TypeError

    except ZeroDivisionError:
        return 0

    else:
        return result
