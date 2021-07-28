import pytest

from numbers_to_dec import list_to_decimal


@pytest.mark.parametrize("nums, expected", [([4, 5, 3, 1], 4531),
                                           ([0, 4, 2, 8], 428),
                                           ([1, 2], 12),
                                           ([3], 3)
                                           ])
def test_list_of_decimal(nums, expected) -> None:
    assert list_to_decimal(nums) == expected


@pytest.mark.parametrize("nums", [[6, 2, True], [3.6, 4, 1], ["4", 5, 3, 1]])
def test_type_error(nums) -> None:
    with pytest.raises(TypeError):
        output = list_to_decimal(nums)


@pytest.mark.parametrize("nums", [[-3, 12]])
def test_value_error_out_of_range(nums) -> None:
    with pytest.raises(ValueError):
        output = list_to_decimal(nums)
