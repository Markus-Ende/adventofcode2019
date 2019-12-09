
from common.io import read
from day9.intcode_interpreter import run


def test_solution_part1():
    intcode = read("src/day9/input.txt")
    output = []
    run({"program": intcode}, False, [1], lambda x: output.append(x))
    assert len(output) == 1
    solution = output[0]
    assert solution == 3409270027
