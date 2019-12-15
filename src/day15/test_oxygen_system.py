import pytest
from day15.input import intcode_input, full_map
from day15.oxygen_system import create_explorer, oxygen_flooding


@pytest.mark.parametrize("input,expected", [
    (intcode_input,
     ([(0, -1, "#"), (0, 0, "s")], (0, 0)))
])
def test_create_explorer(input, expected):
    assert create_explorer(input)(lambda: "1") == expected


@pytest.mark.parametrize("input,expected", [
    (full_map,
     346)
])
def test_oxygen_flooding(input, expected):
    assert oxygen_flooding(input) == expected
