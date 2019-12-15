import pytest
from .painting_robot import paint_hull
from .input import intcode_input


@pytest.mark.parametrize("input,expected", [
    ("3,0,104,1,104,1,99", 1),
    ("3,0,104,1,104,1,3,0,104,1,104,0,99", 2),
    # (intcode_input, 2276)
])
def test_paint_hull(input, expected):
    assert paint_hull(input) == expected
