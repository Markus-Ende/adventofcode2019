from day7.amplification_circuit import thruster_output_with_feedback_loop, max_thruster_output
from common.io import read


def test_solution_part1():
    intcode = read("src/day7/input.txt")
    assert max_thruster_output(
        intcode, thruster_output_with_feedback_loop, (5, 6, 7, 8, 9)) == 33660560
