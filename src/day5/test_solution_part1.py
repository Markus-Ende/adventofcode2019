import day5.intcode_computer
import pytest


@pytest.mark.parametrize("program,expected", [
    ("1,0,0,0,99", [1, 0, 0, 0, 99]),
    ("2,3,0,3,99", [2, 3, 0, 3, 99]),
])
def test_tokenize_program(program, expected):
    assert day5.intcode_computer.tokenize_program(program) == expected


@pytest.mark.parametrize("program,command_index,expected_return,expected_program", [
    ([1, 0, 0, 0], 0, 4, [2, 0, 0, 0]),
    ([1, 1, 2, 3], 0, 4, [1, 1, 2, 3]),
    ([2, 0, 2, 3], 0, 4, [2, 0, 2, 4]),
    ([99, 0, 2, 3], 0, -1, [99, 0, 2, 3]),
    ([0, 1, 1, 2, 3], 1, 5, [0, 1, 1, 2, 3]),
])
def test_run_command(program, command_index, expected_return, expected_program):
    assert day5.intcode_computer.run_command(
        command_index, program) == expected_return
    assert program == expected_program


@pytest.mark.parametrize("program,command_index,expected_return,expected_program", [
    ([101, 42, 0, 0], 0, 4, [143, 42, 0, 0]),
    ([1002,4,3,4,33], 0 , 4, [1002,4,3,4,99])
])
def test_parameter_modes(program, command_index, expected_return, expected_program):
    assert day5.intcode_computer.run_command(
        command_index, program) == expected_return
    assert program == expected_program


@pytest.mark.parametrize("program,expected_return,expected_output", [
    ([4, 0],  2, 4),
    ([4, 1],  2, 1),
    ([104, 0],  2, 0),
    ([4, 2, 100],  2, 100),
])
def test_run_output_command(program, expected_return, expected_output, monkeypatch):
    output = 0

    def store_argument(x):
        nonlocal output
        output = x

    monkeypatch.setattr('builtins.print', store_argument)
    assert day5.intcode_computer.run_command(0, program) == expected_return
    assert output == expected_output


@pytest.mark.parametrize("program,input_int,expected_return,expected_program", [
    ([3, 0], 1, 2, [1, 0]),
    ([3, 0], 2, 2, [2, 0]),
    ([3, 1], 2, 2, [3, 2]),
])
def test_run_input_command(program, input_int, expected_return, expected_program, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: input_int)
    assert day5.intcode_computer.run_command(0, program) == expected_return
    assert program == expected_program


def test_run_echo_program(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: 1337)
    output = 0

    def store_argument(x):
        nonlocal output
        output = x
    monkeypatch.setattr('builtins.print', store_argument)

    day5.intcode_computer.run_intcode([3, 0, 4, 0, 99])
    assert output == 1337

# def test_run_inputcommand(monkeypatch):
#     monkeypatch.setattr('builtins.input', lambda: 1)
#     program = [3, 0]
#     assert day5.intcode_computer.run_command(0, program) == 2
#     assert program == [1, 0]


@pytest.mark.parametrize("program,expected", [
    ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
    ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
    ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
    ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]),
    ([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], [
     3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50])
])
def test_run_intcode(program, expected):
    assert day5.intcode_computer.run_intcode(program) == expected

