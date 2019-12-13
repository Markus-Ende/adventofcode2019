import pytest
from day10.monitoring_station import parse_asteroid_map, can_detect, count_detectable_asteroids, find_best_station, sort_for_laser_round, shoot
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


@pytest.mark.parametrize("asteroids,station,expected", [
    (parse_asteroid_map(
     """###
        ###
        ###"""), (1, 1), [((1, 0), 0.0), ((2, 0), 45.0), ((2, 1), 90.0), ((2, 2), 135.0), ((1, 2), 180.0), ((0, 2), 225.0), ((0, 1), 270.0), ((0, 0), 315.0)]),
    (parse_asteroid_map(
     """###
        ###
        ###"""), (0, 0), [((1, 0), 90.0), ((2, 0), 90.0), ((2, 1), 116.56505117707799), ((1, 1), 135.0), ((2, 2), 135.0), ((1, 2), 153.43494882292202), ((0, 1), 180.0), ((0, 2), 180.0)])
])
def test_sort_for_laser_round(asteroids, station, expected):
    assert sort_for_laser_round(asteroids, station) == expected


@pytest.mark.parametrize("asteroids,station,expected", [
    (parse_asteroid_map(
     """###
        ###
        ###"""), (1, 1), [(1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (0, 1), (0, 0)]),
    (parse_asteroid_map(
     """###
        ###
        ###"""), (0, 0), [(1, 0), (2, 1), (1, 1), (1, 2), (0, 1), (2, 0), (2, 2), (0, 2)])
])
def test_shoot(asteroids, station, expected):
    assert shoot(asteroids, station) == expected


@pytest.mark.parametrize("asteroids,station,expected", [
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
        ###.##.####.##.#..##"""), (11, 13), 802),
    (parse_asteroid_map(read("src/day10/input.txt")), (11, 19), 815),
])
def test_solution_part2(asteroids, station, expected):
    shot_asteroids = shoot(asteroids, station)
    asteroid200 = shot_asteroids[199]
    magic_number = asteroid200[0] * 100 + asteroid200[1]
    assert magic_number == expected
