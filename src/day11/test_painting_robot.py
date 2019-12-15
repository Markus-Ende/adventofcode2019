import pytest
from .painting_robot import paint_hull
from .input import intcode_input


@pytest.mark.parametrize("input,expected", [
    ("3,0,104,1,104,1,99", 1),
    ("3,0,104,1,104,1,3,0,104,1,104,0,99", 2),
    # (intcode_input, 2276)
])
def test_paint_hull_amount_painted(input, expected):
    assert paint_hull(input)["amount_painted"] == expected


@pytest.mark.parametrize("input,expected", [
    ("3,0,104,1,104,1,99", "1"),
    ("3,0,104,1,104,1,3,0,104,1,104,0,99", "11"),
    (intcode_input,
     """0011001110010000111000011011110011001001000
0100101001010000100100001000010100101001000
0100001110010000100100001000100100001001000
0100001001010000111000001001000100001001000
0100101001010000100001001010000100101001000
0011001110011110100000110011110011000110000"""  # see solution_part2.pgm
     )
])
def test_paint_hull_picture(input, expected):
    assert paint_hull(input, "1")["picture"] == expected
