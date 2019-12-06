import pytest
from day6.orbit_map import count_orbits
from common.io import read


@pytest.mark.parametrize("input,expected", [
    (
    """
    COM)B
    B)C
    C)D
    D)E
    E)F
    B)G
    G)H
    D)I
    E)J
    J)K
    K)L
    """, 42),
    # uncomment on your own risk, it's very inefficient x-D
    #(read("src/day6/input.txt"), 270768)
])
def test_count_orbits(input, expected):
    assert count_orbits(input) == expected
