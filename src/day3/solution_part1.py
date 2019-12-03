import math
import sys


def manhattan_distance(x, y):
    return sum(abs(a-b) for a, b in zip(x, y))


def convert_path_to_coords(path):
    coords = set()
    current_x = 0
    current_y = 0
    for segment in path:
        direction = segment[0]
        amount = int(segment[1:])
        for _ in range(amount):
            if (direction == "R"):
                current_x = current_x + 1
            if (direction == "L"):
                current_x = current_x - 1
            if (direction == "U"):
                current_y = current_y + 1
            if (direction == "D"):
                current_y = current_y - 1
            coords.add((current_x, current_y))
    return coords


def min_manhattan_distance(coords):
    closest_dist = sys.maxsize

    for c in coords:
        dist = manhattan_distance((0, 0), c)
        if (dist < closest_dist):
            closest_dist = dist

    return closest_dist


def find_dist_of_intersection_closest_to_origin(path1, path2):
    coords1 = convert_path_to_coords(path1)
    coords2 = convert_path_to_coords(path2)
    intersections = coords1.intersection(coords2)
    return min_manhattan_distance(intersections)
