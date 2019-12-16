import pytest
from .n_body import parse_system, simulate_steps, calculate_system_energy, calculate_steps_until_repetition
from .input import input_system


@pytest.mark.parametrize("input,expected", [
    ("""<x=-1, y=0, z=2>
        <x=2, y=-10, z=-7>
        <x=4, y=-8, z=8>
        <x=3, y=5, z=-1>""",
     [{"pos": {"x": -1, "y": 0, "z": 2},
       "vel": {"x": 0, "y": 0, "z": 0}},
      {"pos": {"x": 2, "y": -10, "z": -7},
       "vel": {"x": 0, "y": 0, "z": 0}},
      {"pos": {"x": 4, "y": -8, "z": 8},
       "vel": {"x": 0, "y": 0, "z": 0}},
      {"pos": {"x": 3, "y": 5, "z": -1},
       "vel": {"x": 0, "y": 0, "z": 0}}])])
def test_parse_system(input, expected):
    assert parse_system(input) == expected


@pytest.mark.parametrize("input,steps,expected", [
    (parse_system("""<x=-1, y=0, z=2>
        <x=2, y=-10, z=-7>
        <x=4, y=-8, z=8>
        <x=3, y=5, z=-1>"""), 1,
     [{"pos": {"x": 2, "y": -1, "z": 1}, "vel": {"x": 3, "y": -1, "z": -1}},
      {"pos": {"x": 3, "y": -7, "z": -4}, "vel": {"x": 1, "y": 3, "z": 3}},
      {"pos": {"x": 1, "y": -7, "z": 5}, "vel": {"x": -3, "y": 1, "z": -3}},
      {"pos": {"x": 2, "y": 2, "z": 0}, "vel": {"x": -1, "y": -3, "z": 1}}]),
    (parse_system("""<x=-1, y=0, z=2>
        <x=2, y=-10, z=-7>
        <x=4, y=-8, z=8>
        <x=3, y=5, z=-1>"""), 10,
     [{"pos": {"x": 2, "y":  1, "z": -3}, "vel": {"x": -3, "y": -2, "z": 1}},
      {"pos": {"x": 1, "y": -8, "z": 0}, "vel": {"x": -1, "y": 1, "z": 3}},
      {"pos": {"x": 3, "y": -6, "z": 1}, "vel": {"x":  3, "y": 2, "z": -3}},
      {"pos": {"x": 2, "y":  0, "z": 4}, "vel": {"x": 1, "y": -1, "z": -1}}]),
])
def test_simulate_steps(input, steps, expected):
    assert simulate_steps(input, steps) == expected


@pytest.mark.parametrize("input,expected", [
    ([{"pos": {"x": 2, "y":  1, "z": -3}, "vel": {"x": -3, "y": -2, "z": 1}},
      {"pos": {"x": 1, "y": -8, "z": 0}, "vel": {"x": -1, "y": 1, "z": 3}},
      {"pos": {"x": 3, "y": -6, "z": 1}, "vel": {"x":  3, "y": 2, "z": -3}},
      {"pos": {"x": 2, "y":  0, "z": 4}, "vel": {"x": 1, "y": -1, "z": -1}}], 179),
    (simulate_steps(parse_system(input_system), 1000), 12644)
])
def test_calculate_system_energy(input, expected):
    assert calculate_system_energy(input) == expected


@pytest.mark.parametrize("input,expected", [
    (parse_system("""<x=-1, y=0, z=2>
        <x=2, y=-10, z=-7>
        <x=4, y=-8, z=8>
        <x=3, y=5, z=-1>"""), 2772),
    # (parse_system(input_system), ?)
])
def test_calculate_steps_until_repetition(input, expected):
    assert calculate_steps_until_repetition(input) == expected
