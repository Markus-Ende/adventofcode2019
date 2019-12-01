import pytest
import day1.solution_part2


@pytest.mark.parametrize("input_mass,expected", [
    (12, 2), (14, 2), (1969, 966), (100756, 50346)
])
def test_calculate_fuel_recursively(input_mass, expected):
    assert day1.solution_part2.calculate_fuel_recursively(
        input_mass) == expected


def test_solution_part2():
    input_raw = day1.solution_part1.read('src/day1/input.txt')
    masses = day1.solution_part1.parse_input(input_raw)
    solution = day1.solution_part2.sum_fuel(masses)
    assert solution == 5011553
