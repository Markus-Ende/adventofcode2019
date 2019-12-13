import pytest
from day10.monitoring_station import parse_asteroid_map, can_detect, count_detectable_asteroids, find_best_station
from common.io import read


@pytest.mark.parametrize("input,expected", [
    ("""##.
        .#.
        ..#""", [(0, 0), (1, 0), (1, 1), (2, 2)])
])
def test_parse_asteroid_map(input, expected):
    assert parse_asteroid_map(input) == expected


@pytest.mark.parametrize("asteroids,station,target,expected", [
    (parse_asteroid_map(
     """.#..#
        .....
        #####
        ....#
        ...##"""), (3, 4), (1, 0), False),
    (parse_asteroid_map(
     """.#..#
        .....
        ##.##
        ....#
        ...##"""), (3, 4), (1, 0), True),
    (parse_asteroid_map(
     """.#..#
        .....
        #####
        ....#
        ...##"""), (3, 4), (0, 2), True)
])
def test_can_detect(asteroids, station, target, expected):
    assert can_detect(asteroids, station, target) == expected


@pytest.mark.parametrize("asteroids,station,expected", [
    (parse_asteroid_map(
     """.#..#
        .....
        #####
        ....#
        ...##"""), (3, 4), 8),
    (parse_asteroid_map(
     """.#..#
        .....
        #####
        ....#
        ...##"""), (4, 2), 5)
])
def test_count_detectable_asteroids(asteroids, station, expected):
    assert count_detectable_asteroids(asteroids, station) == expected


@pytest.mark.parametrize("asteroids,expected", [
    (parse_asteroid_map(
     """.#..#
        .....
        #####
        ....#
        ...##"""), ((3, 4), 8)),
    (parse_asteroid_map(
     """......#.#.
        #..#.#....
        ..#######.
        .#.#.###..
        .#..#.....
        ..#....#.#
        #..#....#.
        .##.#..###
        ##...#..#.
        .#....####"""), ((5, 8), 33)),
    (parse_asteroid_map(
     """#.#...#.#.
        .###....#.
        .#....#...
        ##.#.#.#.#
        ....#.#.#.
        .##..###.#
        ..#...##..
        ..##....##
        ......#...
        .####.###."""), ((1, 2), 35)),
    (parse_asteroid_map(
     """.#..#..###
        ####.###.#
        ....###.#.
        ..###.##.#
        ##.##.#.#.
        ....###..#
        ..#.#..#.#
        #..#.#.###
        .##...##.#
        .....#.#.."""), ((6, 3), 41)),
    (parse_asteroid_map(
     """.#..##.###...#######
        ##.############..##.
        .#.######.########.#
        .###.#######.####.#.
        #####.##.#.##.###.##
        ..#####..#.#########
        ####################
        #.####....###.#.#.##
        ##.#################
        #####.##.###..####..
        ..######..##.#######
        ####.##.####...##..#
        .#####..#.######.###
        ##...#.##########...
        #.##########.#######
        .####.#.###.###.#.##
        ....##.##.###..#####
        .#.#.###########.###
        #.#.#.#####.####.###
        ###.##.####.##.#..##"""), ((11, 13), 210)),
    (parse_asteroid_map(read("src/day10/input.txt")), ((11, 19), 253)),

])
def test_find_best_station(asteroids, expected):
    assert find_best_station(asteroids) == expected
