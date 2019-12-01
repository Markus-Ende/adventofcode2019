import pytest
import day1.solution_part1


@pytest.mark.parametrize("input_mass,expected", [
    (12, 2), (14, 2), (1969, 654), (100756, 33583)
])
def test_calculate_fuel(input_mass, expected):
    assert day1.solution_part1.calculate_fuel(input_mass) == expected


def test_parse_input():
    input = ("12 \n"
             "14\n"
             "1969\n"
             "100756\n")
    assert day1.solution_part1.parse_input(input) == [12, 14, 1969, 100756]


def test_sum_fuel():
    assert day1.solution_part1.sum_fuel(
        [12, 14, 1969, 100756]) == 2+2+654+33583


def test_solution_part1():
    input_raw = day1.solution_part1.read('src/day1/input.txt')
    masses = day1.solution_part1.parse_input(input_raw)
    solution = day1.solution_part1.sum_fuel(masses)
    assert solution == 3342946
