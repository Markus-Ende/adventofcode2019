import pytest
from .map import coords_to_map


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
