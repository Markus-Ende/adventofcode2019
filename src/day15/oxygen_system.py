import sys
import math
from day9.intcode_interpreter import run as run_intcode


def create_explorer(intcode):
    program_state = {"program": intcode}
    droid = (0, 0)
    coords = [(0, 0, "s")]

    def move_coord(coord, input):
        if (input == "1"):
            # north
            return (coord[0], coord[1] - 1)
        if (input == "2"):
            # south
            return (coord[0], coord[1] + 1)
        if (input == "3"):
            # west
            return (coord[0] - 1, coord[1])
        if (input == "4"):
            # east
            return (coord[0] + 1, coord[1])

    def step(input_func=input):
        nonlocal program_state
        nonlocal droid
        next_input = input_func()
        #print("input:", next_input)
        output = []
        while(len(output) == 0):
            program_state = run_intcode(program_state, True, [
                next_input], lambda out: output.append(out))

        markers = "#.x"
        out = output.pop(0)
        coord = move_coord(droid, next_input)
        coords.insert(0, (coord[0], coord[1], markers[out]))
        if (out > 0):
            droid = (coord[0], coord[1])

        return (coords, droid)

    return step


def oxygen_flooding(full_map):
    full_map_lines = full_map.split("\n")

    def flood():
        flooded_coords = []
        for y in range(0, len(full_map_lines)):
            for x in range(0, len(full_map_lines[0])):
                if (full_map_lines[y][x] == "O"):
                    if (full_map_lines[max(0, y-1)][x] == "."):
                        flooded_coords.append((x, y-1))
                    if (full_map_lines[min(len(full_map_lines) - 1, y+1)][x] == "."):
                        flooded_coords.append((x, y+1))
                    if (full_map_lines[y][max(0, x-1)] == "."):
                        flooded_coords.append((x-1, y))
                    if (full_map_lines[y][min(len(full_map_lines[0]), x+1)] == "."):
                        flooded_coords.append((x+1, y))
        for c in flooded_coords:
            line = full_map_lines[c[1]]
            full_map_lines[c[1]] = line[:c[0]]+"O"+line[c[0]+1:]

    minutes = 0
    while "." in "".join(full_map_lines):
        flood()
        minutes += 1
        # print(full_map_lines)

    return minutes
