from typing import Iterable, Set, Any


def intersection(*args: Iterable) -> Set[Any]:
    # filter out the None and empty
    filtered_args = list(filter(None, args))
    if not filtered_args:
        return set()
    return set(filtered_args[0]).intersection(*filtered_args[1:])
