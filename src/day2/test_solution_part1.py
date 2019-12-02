import pytest
import day2.solution_part1


@pytest.mark.parametrize("program,expected", [
    ("1,0,0,0,99", [1, 0, 0, 0, 99]),
    ("2,3,0,3,99", [2, 3, 0, 3, 99]),
])
def test_tokenize_program(program, expected):
    assert day2.solution_part1.tokenize_program(program) == expected


@pytest.mark.parametrize("program,command_index,expected_return,expected_program", [
    ([1, 0, 0, 0], 0, 4, [2, 0, 0, 0]),
    ([1, 1, 2, 3], 0, 4, [1, 1, 2, 3]),
    ([2, 0, 2, 3], 0, 4, [2, 0, 2, 4]),
    ([99, 0, 2, 3], 0, -1, [99, 0, 2, 3]),
    ([0, 1, 1, 2, 3], 1, 5, [0, 1, 1, 2, 3]),
])
def test_run_command(program, command_index, expected_return, expected_program):
    assert day2.solution_part1.run_command(
        command_index, program) == expected_return
    assert program == expected_program


@pytest.mark.parametrize("program,expected", [
    ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
    ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
    ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
    ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]),
    ([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], [
     3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50])
])
def test_run_intcode(program, expected):
    assert day2.solution_part1.run_intcode(program) == expected


def test_solution_part1():
    intcode = read('src/day2/input.txt')
    tokenized = day2.solution_part1.tokenize_program(intcode)
    # before running the program, replace position 1 with the value 12 and replace position 2 with the value 2
    tokenized[1] = 12
    tokenized[2] = 2
    # What value is left at position 0 after the program halts?
    assert day2.solution_part1.run_intcode(tokenized)[0] == 7210630


def read(file_path):
    input_file = open(file_path, 'r')
    input_raw = input_file.read()
    input_file.close()
    return input_raw
