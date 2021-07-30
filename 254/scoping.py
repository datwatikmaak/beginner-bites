num_hundreds = -1


def sum_numbers(numbers: list) -> int:
    """Sums passed in numbers returning the total, also
       update the global variable num_hundreds with the amount
       of times 100 fits in total"""
    global num_hundreds
    total = sum(numbers)
    if total >= 100:
        hundreds = int(str(total)[:-2])
        num_hundreds += hundreds
    else:
        num_hundreds = num_hundreds

    return total
