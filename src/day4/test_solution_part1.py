import pytest
import day4.solution_part1


@pytest.mark.parametrize("password,expected", [
    ([1, 1, 1, 1, 1], False),
    ([1, 1, 1, 1, 1, 1], True),
    ([2, 2, 3, 4, 5, 0], False),
    ([1, 2, 3, 7, 8, 9], False)
])
def test_check_valid_password(password, expected):
    assert day4.solution_part1.check_valid_password(password) == expected


@pytest.mark.parametrize("min,max,expected", [
    ("111110", "111112", 2),
    ("153517", "630395", 1729)
])
def test_count_valid_passwords(min, max, expected):
    assert day4.solution_part1.count_valid_passwords(min, max) == expected
