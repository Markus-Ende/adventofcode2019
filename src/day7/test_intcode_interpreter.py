import pytest
from day7.intcode_interpreter import run


@pytest.mark.parametrize("program,expected", [
    ("1, 0, 0, 0, 99", (-1, "2, 0, 0, 0, 99")),
    ("2, 3, 0, 3, 99", (-1, "2, 3, 0, 6, 99")),
    ("2, 4, 4, 5, 99, 0", (-1, "2, 4, 4, 5, 99, 9801")),
    ("1, 1, 1, 4, 99, 5, 6, 0, 99", (-1, "30, 1, 1, 4, 2, 5, 6, 0, 99")),
    ("1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50",
     (-1, "3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50")),
    ("5, 3, 1, 1, 0, 0, 0, 99", (-1, "10, 3, 1, 1, 0, 0, 0, 99")),
    ("105, 0, 1, 1, 0, 0, 0, 99", (-1, "210, 0, 1, 1, 0, 0, 0, 99")),
    ("5, 4, 1, 1, 0, 0, 0, 99", (-1, "10, 4, 1, 1, 0, 0, 0, 99")),
    ("6, 4, 3, 1, 0, 0, 0, 99", (-1, "12, 4, 3, 1, 0, 0, 0, 99")),
    ("1107, 1, 2, 0, 99", (-1, "1, 1, 2, 0, 99")),
    ("1107, 2, 2, 0, 99", (-1, "0, 2, 2, 0, 99")),
    ("1108, 1, 2, 0, 99", (-1, "0, 1, 2, 0, 99")),
    ("1108, 2, 2, 0, 99", (-1, "1, 2, 2, 0, 99")),
])
def test_run(program, expected):
    assert run(program) == expected


@pytest.mark.parametrize("program,ip,expected", [
    ("1, 0, 0, 0, 99", 0, (4, "2, 0, 0, 0, 99")),
    ("2, 0, 0, 0, 99", 4, (-1, "2, 0, 0, 0, 99"))
])
def test_run_single_step(program, ip, expected):
    assert run(program, ip, True) == expected


def test_run_echo_program(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: 1337)
    output = 0

    def store_argument(x):
        nonlocal output
        output = x
    monkeypatch.setattr('builtins.print', store_argument)

    run("3, 0, 4, 0, 99")
    assert output == 1337


def test_run_echo_program_with_predefined_input_and_output_callback(monkeypatch):
    output = 0

    def store_argument(x):
        nonlocal output
        output = x

    run("3, 0, 4, 0, 99", 0, False, [1337], store_argument)
    assert output == 1337
