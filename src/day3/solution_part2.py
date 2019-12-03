import math
import sys
from day3.solution_part1 import convert_path_to_coords


def find_min_combined_steps_needed_to_reach_intersection(path1, path2):
    coords1 = convert_path_to_coords(path1)
    coords2 = convert_path_to_coords(path2)
    intersections = set(coords1).intersection(set(coords2))

    min_combined_steps = sys.maxsize

    for i in intersections:
        combined_steps = count_steps(coords1, i) + count_steps(coords2, i)
        if (combined_steps < min_combined_steps):
            min_combined_steps = combined_steps

    return min_combined_steps


def count_steps(coords, intersection):
    steps = 0
    for c in coords:
        steps = steps + 1
        if (c == intersection):
            return steps
    return -1
