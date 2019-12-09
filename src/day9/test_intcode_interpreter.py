import pytest
from day9.intcode_interpreter import run


@pytest.mark.parametrize("program,expected", [
    ("1, 0, 0, 0, 99", {"ip": -1, "program": "2, 0, 0, 0, 99", "rbase": 0}),
    ("2, 3, 0, 3, 99", {"ip": -1, "program": "2, 3, 0, 6, 99", "rbase": 0}),
    ("2, 4, 4, 5, 99, 0", {
     "ip": -1, "program": "2, 4, 4, 5, 99, 9801", "rbase": 0}),
    ("1, 1, 1, 4, 99, 5, 6, 0, 99",
     {"ip": -1, "program": "30, 1, 1, 4, 2, 5, 6, 0, 99", "rbase": 0}),
    ("1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50",
     {"ip": -1, "program": "3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50", "rbase": 0}),
    ("5, 3, 1, 1, 0, 0, 0, 99",
     {"ip": -1, "program": "10, 3, 1, 1, 0, 0, 0, 99", "rbase": 0}),
    ("105, 0, 1, 1, 0, 0, 0, 99",
     {"ip": -1, "program": "210, 0, 1, 1, 0, 0, 0, 99", "rbase": 0}),
    ("5, 4, 1, 1, 0, 0, 0, 99",
     {"ip": -1, "program": "10, 4, 1, 1, 0, 0, 0, 99", "rbase": 0}),
    ("6, 4, 3, 1, 0, 0, 0, 99",
     {"ip": -1, "program": "12, 4, 3, 1, 0, 0, 0, 99", "rbase": 0}),
    ("1107, 1, 2, 0, 99", {"ip": -1, "program": "1, 1, 2, 0, 99", "rbase": 0}),
    ("1107, 2, 2, 0, 99", {"ip": -1, "program": "0, 2, 2, 0, 99", "rbase": 0}),
    ("1108, 1, 2, 0, 99", {"ip": -1, "program": "0, 1, 2, 0, 99", "rbase": 0}),
    ("1108, 2, 2, 0, 99", {"ip": -1, "program": "1, 2, 2, 0, 99", "rbase": 0}),
])
def test_run(program, expected):
    assert run({"program": program}) == expected


@pytest.mark.parametrize("program,expected_rbase", [
    ({"program": "109,2,99"}, 2),
    ({"program": "9,1,99"}, 1),
    ({"rbase": 1, "program": "9,1,99"}, 2),
])
def test_adjust_relative_base(program, expected_rbase):
    assert run(program).get("rbase") == expected_rbase


@pytest.mark.parametrize("program,expected_output", [
    #             print mem10
    ({"program": "4,10,99    "}, 0),
    #             mem10 = 1+2,  print mem10
    ({"program": "1101,1,2,10,  4,10,99    "}, 3),
])
def test_accessing_memory_beyond_initial_program(program, expected_output):
    output = -1

    def store_argument(x):
        nonlocal output
        output = x

    run(program, False, None, store_argument)
    assert output == expected_output


@pytest.mark.parametrize("program,expected_output", [
    #             print rel(mem10)
    ({"rbase": 1, "program": "204,10,99    "}, 0),
    #             mem10 = 1+2,  print mem10
    ({"rbase": 1, "program": "21101,1,2,10,  4,11,99    "}, 3),
])
def test_relative_parameters(program, expected_output):
    output = -1

    def store_argument(x):
        nonlocal output
        output = x

    run(program, False, None, store_argument)
    assert output == expected_output


@pytest.mark.parametrize("program,ip,expected", [
    ("1, 0, 0, 0, 99", 0, {"ip": 4, "program": "2, 0, 0, 0, 99", "rbase": 0}),
    ("2, 0, 0, 0, 99", 4, {"ip": -1, "program": "2, 0, 0, 0, 99", "rbase": 0})
])
def test_run_single_step(program, ip, expected):
    assert run({"program": program, "ip": ip}, True) == expected


def test_run_echo_program_with_stdin_and_stdout(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: 1337)
    output = 0

    def store_argument(x):
        nonlocal output
        output = x
    monkeypatch.setattr('builtins.print', store_argument)

    run({"program": "3, 0, 4, 0, 99"})
    assert output == 1337


def test_run_echo_program_with_predefined_input_and_output_callback(monkeypatch):
    output = 0

    def store_argument(x):
        nonlocal output
        output = x

    run({"program": "3, 0, 4, 0, 99"}, False, [1337], store_argument)
    assert output == 1337


@pytest.mark.parametrize("program,expected_output", [
    ({"program": "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"},
     [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]),
    ({"program": "1102,34915192,34915192,7,4,7,99,0"},
     [1219070632396864]),
    ({"program": "104,1125899906842624,99"},
     [1125899906842624]),
])
def test_run_additional_given_day8_programs(program, expected_output):
    output = []

    run(program, False, None, lambda x: output.append(x))
    assert output == expected_output
