import pytest
from day4.solution_part1 import *


@pytest.mark.parametrize("password,expected", [
    ([1, 1, 1, 1, 1], False),
    ([1, 1, 1, 1, 1, 1], True),
    ([2, 2, 3, 4, 5, 0], False),
    ([1, 2, 3, 7, 8, 9], False)
])
def test_check_valid_password(password, expected):
    assert check_valid_password(password) == expected


@pytest.mark.parametrize("min,max,expected", [
    ("111110", "111112", 2),
    ("153517", "630395", 1729)
])
def test_count_valid_passwords(min, max, expected):
    assert count_valid_passwords(min, max, check_valid_password) == expected
