import pytest
from day4.solution_part1 import count_valid_passwords
from day4.solution_part2 import check_valid_password, check_new_rule


@pytest.mark.parametrize("password,expected", [
    ([1, 1, 1, 1, 1], False),
    ([1, 1, 1, 1, 1, 1], False),
    ([2, 2, 3, 4, 5, 0], False),
    ([1, 2, 3, 7, 8, 9], False),
    ([1, 1, 2, 2, 3, 3], True),
    ([1, 2, 3, 4, 4, 4], False),
    ([1, 1, 1, 1, 2, 2], True),
])
def test_check_valid_password(password, expected):
    assert check_valid_password(password) == expected


@pytest.mark.parametrize("password,expected", [
    ([1, 1, 1, 1, 1, 1], False),
    ([1, 1, 1, 1, 2, 2], True),
])
def test_check_new_rule(password, expected):
    assert check_new_rule(password) == expected


@pytest.mark.parametrize("min,max,expected", [
    ("111120", "111124", 1),
    ("153517", "630395", 1172)
])
def test_count_valid_passwords(min, max, expected):
    assert count_valid_passwords(min, max, check_valid_password) == expected
