import pytest
import day3.solution_part2


@pytest.mark.parametrize("coords,intersection,expected", [
    ([(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(7,5),(6,5),(5,5),(4,5),(3,5),(3,4),(3,3),(3,2)], (3, 3), 20)
])
def test_count_steps(coords, intersection, expected):
    assert day3.solution_part2.count_steps(coords, intersection) == expected



@pytest.mark.parametrize("path1,path2,expected", [
    (["R8","U5","L5","D3"], ["U7","R6","D4","L4"], 30),
    (["R75","D30","R83","U83","L12","D49","R71","U7","L72"], ["U62","R66","U55","R34","D71","R55","D58","R83"], 610),
    (["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"], ["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"], 410)
])
def test_find_min_combined_steps_needed_to_reach_intersection(path1, path2, expected):
    assert day3.solution_part2.find_min_combined_steps_needed_to_reach_intersection(path1, path2) == expected

def test_solution_part2():
    input_lines = read("src/day3/input.txt").splitlines()
    path1 = input_lines[0].split(",")
    path2 = input_lines[1].split(",")
    assert day3.solution_part2.find_min_combined_steps_needed_to_reach_intersection(path1, path2) == 6084


def read(file_path):
    input_file = open(file_path, 'r')
    input_raw = input_file.read()
    input_file.close()
    return input_raw
