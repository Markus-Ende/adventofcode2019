import pytest
import day3.solution_part1


@pytest.mark.parametrize("path,expected", [
    (["R8","U5","L5","D3"], [(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(7,5),(6,5),(5,5),(4,5),(3,5),(3,4),(3,3),(3,2)])
])
def test_convert_path_to_coords(path, expected):
    assert day3.solution_part1.convert_path_to_coords(path) == expected

def test_manhattan_distance():
    assert day3.solution_part1.manhattan_distance((1,0), (8,1)) == 8

@pytest.mark.parametrize("coords,expected", [
    (set([(3,3),(6,5)]), 6)
])
def test_min_manhattan_distance(coords,expected):
    assert day3.solution_part1.min_manhattan_distance(coords) == expected

@pytest.mark.parametrize("path1,path2,expected", [
    (["R8","U5","L5","D3"], ["U7","R6","D4","L4"], 6),
    (["R75","D30","R83","U83","L12","D49","R71","U7","L72"], ["U62","R66","U55","R34","D71","R55","D58","R83"], 159),
    (["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"], ["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"], 135)
])
def test_find_dist_of_intersection_closest_to_origin(path1, path2, expected):
    assert day3.solution_part1.find_dist_of_intersection_closest_to_origin(path1, path2) == expected


def test_solution_part1():
    input_lines = read("src/day3/input.txt").splitlines()
    path1 = input_lines[0].split(",")
    path2 = input_lines[1].split(",")
    assert day3.solution_part1.find_dist_of_intersection_closest_to_origin(path1, path2) == 232

def read(file_path):
    input_file = open(file_path, 'r')
    input_raw = input_file.read()
    input_file.close()
    return input_raw