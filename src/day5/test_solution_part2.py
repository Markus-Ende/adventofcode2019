import day5.intcode_computer
import pytest


@pytest.mark.parametrize("program,expected", [
    ([5, 3, 1, 1, 0, 0, 0, 99], [10, 3, 1, 1, 0, 0, 0, 99]),
    ([105, 0, 1, 1, 0, 0, 0, 99], [210, 0, 1, 1, 0, 0, 0, 99]),
    ([5, 4, 1, 1, 0, 0, 0, 99], [10, 4, 1, 1, 0, 0, 0, 99]),
    ([6, 4, 3, 1, 0, 0, 0, 99], [12, 4, 3, 1, 0, 0, 0, 99]),
    ([1107, 1, 2, 0, 99], [1, 1, 2, 0, 99]),
    ([1107, 2, 2, 0, 99], [0, 2, 2, 0, 99]),
    ([1108, 1, 2, 0, 99], [0, 1, 2, 0, 99]),
    ([1108, 2, 2, 0, 99], [1, 2, 2, 0, 99])
])
def test_run_intcode(program, expected):
    assert day5.intcode_computer.run_intcode(program) == expected
