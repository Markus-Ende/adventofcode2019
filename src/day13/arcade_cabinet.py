from common.map import coords_to_map
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


def run_game(intcode, render):
    tile_coords = {}
    current_partial_tile_coord = []

    def render_buffered_output(output):
        if (len(current_partial_tile_coord) == 2):
            tile_coords[tuple(current_partial_tile_coord)] = output
            render([(tile[0], tile[1], tile_coords[tile])
                    for tile in tile_coords])
            current_partial_tile_coord.clear()
        else:
            current_partial_tile_coord.append(output)
        return

    run({"program": intcode}, False, None, render_buffered_output)
