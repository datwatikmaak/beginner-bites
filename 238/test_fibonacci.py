from fibonacci import fib
import pytest


# write one or more pytest functions below, they need to start with test_
@pytest.mark.parametrize("number, expected", [(2, 1), (4, 3), (10, 55)])
def test_fib(number, expected) -> None:
    assert fib(number) == expected


# test error
def test_fib_value_error() -> None:
    with pytest.raises(ValueError):
        assert fib(-1) == 1
