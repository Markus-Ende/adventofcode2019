from common.map import coords_to_map
from os import system, name
from day9.intcode_interpreter import run


def render_screen_breakout(coords):
    mapping = {
        0: " ",
        1: "▒",
        2: "▄",
        3: "═",
        4: "o",
    }
    return coords_to_map(coords, " ", mapping)


def run_game(intcode, render, update_score=lambda x: None, interactive=False, input_func=input):
    tile_coords = {}
    current_partial_tile_coord = []
    score = 0

    def render_buffered_output(output):
        nonlocal score
        if (len(current_partial_tile_coord) == 2):
            if (current_partial_tile_coord[0] == -1):
                score = output
                update_score(score)
            else:
                tile_coords[tuple(current_partial_tile_coord)] = output
                render([(tile[0], tile[1], tile_coords[tile])
                        for tile in tile_coords])
            current_partial_tile_coord.clear()
        else:
            current_partial_tile_coord.append(output)
        return

    intcode = "2"+intcode[1:] if interactive else intcode

    run({"program": intcode}, False, None, render_buffered_output,
        input_func if interactive else None)
    return score
