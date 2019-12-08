import pytest
from common.io import read
from day8.space_image_format import decode


@pytest.mark.parametrize("input,width,height,expected", [
    ("123456789012", 3, 2, [[1, 2, 3, 4, 5, 6], [7, 8, 9, 0, 1, 2]]),
])
def test_decode(input, width, height, expected):
    assert decode(input, width, height) == expected
