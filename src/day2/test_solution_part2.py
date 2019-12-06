import day2.solution_part1
import day2.solution_part2
from common.io import read


def test_solution_part2():
    intcode = read('src/day2/input.txt')
    tokenized = day2.solution_part1.tokenize_program(intcode)

    assert day2.solution_part2.find_solution(tokenized) == 3892
