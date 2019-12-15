#!/usr/bin/env python3

from day15.input import intcode_input
from day15.oxygen_system import *

explore = create_explorer(intcode_input)
coords = []


def sanitized_input():
    c = "invalid"
    mapping = {
        "w": "1",
        "a": "3",
        "s": "2",
        "d": "4"
    }
    while c == "invalid":
        c = mapping.get(input(), "invalid")
    return c


while len(coords) == 0 or coords[len(coords)-1][2] != "x":
    (coords, droid) = explore(sanitized_input)
    coords_with_droid = [(c[0], c[1], "D") if (
        (c[0], c[1]) == (droid[0], droid[1])) else c for c in coords]
    print(coords_to_map(coords_with_droid))

 ### ### ####### ####### ##### ### #####
#...#...#.......#.......#.....#...#.....#
#.#.#.#.#.#.#####.#.#.###.###.#.#.#.#.#.#
#.#...#...#...#...#.#.#...#.#...#.#.#.#.#
#.#### ######.#.###.###.###.#####.#.#.#.#
#.#...#.....#.#...#.....#.......#.#.#.#.#
#.#.#.#.###.#.###.#######.#####.#.#.#.##
#...#...#...#.....#.....#.#.....#.#.#...#
 ### ####.## ######.#.#.###.#####.#.###.#
#...#...#.#.#...#...#.#.....#.....#...#.#
#.#.###.#.#.#.#.#.###.#####.#.#.###.###.#
#.#.....#.#...#.....#...#...#.#.#...#...#
#.#.#####.#.######## ##.#.###.###.###.#.#
#.#.#...#.#.......#.....#...#.....#.#.#.#
#.###.#.#.#.#######.###.#####.#####.#.##
#.....#...#.#.......#...#...#...#...#...#
#.## ####.###.#####.#####.#.###.#.#.###.#
#...#...#.....#.....#.....#...#...#.#...#
 ##.#.#.#############.#######.###.###.#.#
#...#.#.........#.....#.#.....#...#...#.#
 ####.#########.#.#####.#.#####.###.####
#...#...#.....#.#.#..O#.#...#.#...#.....#
#.#.###.#.###.#.#.#.###.###.#.#.#######.#
#.#.....#...#.....#.#.....#.#...#.....#.#
#.#######.#######.#.#.###.#.#####.###.#.#
#.#...#...#.....#.#.#.#.#...#.....#.#...#
#.#.#.#####.###.###.#.#.#####.#####.###.#
#.#.#.#...#...#...#.#.#.......#...#.....#
#.#.#.#.#.###.###.#.#.#.#####.#.#.#.####
#...#...#.....#.#...#.#.#...#.#.#.#.#...#
 ####### ######.#####.###.#.#.#.#.#.#.#.#
#.......#.........#.#...#.#...#.#.#.#.#.#
#.###.#.#####.# #.#.###.#.#####.#.#.#.#.#
#.#...#.......# #.....#...#.....#.#.#.#.#
#.#.## #######   ####.#####.#####.#.###.#
#.#.#x..................#...#...#.#.#...#
#.#.## ######### ######.#.#.#.#.###.#.##
#.#...#.........#.....#.#.#...#.....#...#
#.###.#.#######.#.###.###.#### ##### ##.#
#...#.........#.....#...................#
 ### ######### ##### ###################

# 298
