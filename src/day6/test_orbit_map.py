import pytest
from day6.orbit_map import count_orbits, count_transits
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


@pytest.mark.parametrize("input,from_token,to_token,expected", [
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
    K)YOU
    I)SAN
    """, "YOU", "SAN", 4),
    # uncomment on your own risk, it's very inefficient x-D
    #(read("src/day6/input.txt"), "YOU", "SAN", 451)
])
def test_count_transits(input, from_token, to_token, expected):
    assert count_transits(from_token, to_token, input) == expected
