import pytest
from day15.input import intcode_input, full_map
from day15.oxygen_system import coords_to_map, create_explorer, oxygen_flooding


@pytest.mark.parametrize("input,expected", [
    ([(0, 0, "."), (0, -1, "."), (1, -1, "#"), (1, 0, "#"), (0, 1, "."), (-1, 0, "D")],
     " .#\n" +
     "D.#\n" +
     " . "),
    ([(0, 0, "D"), (-10, 1, ".")],
     "          D\n" +
     ".          "),

    ([(0, 0, "D"), (0, 5, ".")],
     "D\n" +
     " \n" +
     " \n" +
     " \n" +
     " \n" +
     ".")
])
def test_coords_to_map(input, expected):
    assert coords_to_map(input) == expected


@pytest.mark.parametrize("input,expected", [
    (full_map,
     346)
])
def test_oxygen_flooding(input, expected):
    assert oxygen_flooding(full_map) == expected
