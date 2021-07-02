import pprint
from typing import Any


def pretty_string(obj: Any) -> str:
    pp = pprint.PrettyPrinter(width=60, depth=2, compact=False, sort_dicts=True)
    return pp.pformat(obj)


pretty_string(obj=Any)
