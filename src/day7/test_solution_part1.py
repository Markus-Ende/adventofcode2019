from day7.amplification_circuit import thruster_output, max_thruster_output
from common.io import read


def test_solution_part1():
    intcode = read("src/day7/input.txt")
    assert max_thruster_output(intcode) == 38500
