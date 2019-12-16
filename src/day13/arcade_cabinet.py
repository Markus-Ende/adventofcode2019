from common.map import coords_to_map
from os import system, name
from day9.intcode_interpreter import run
import math


def render_screen_breakout(coords):
    mapping = {
        0: " ",
        1: "▒",
        2: "▄",
        3: "═",
        4: "o",
    }
    return coords_to_map(coords, " ", mapping)


def run_game(intcode, render, update_score=lambda x: None, insert_coin=False, interactive=False, input_func=input):
    tile_coords = {}
    current_partial_tile_coord = []
    score = 0
    current_ball_x = -1
    current_paddle_x = -1

    def render_buffered_output(output):
        nonlocal score
        nonlocal current_ball_x
        nonlocal current_paddle_x
        if (len(current_partial_tile_coord) == 2):
            if (current_partial_tile_coord[0] == -1):
                score = output
                update_score(score)
            else:
                tile_coords[tuple(current_partial_tile_coord)] = output
                if (output == 4):
                    current_ball_x = current_partial_tile_coord[0]
                if (output == 3):
                    current_paddle_x = current_partial_tile_coord[0]
                render([(tile[0], tile[1], tile_coords[tile])
                        for tile in tile_coords])
            current_partial_tile_coord.clear()
        else:
            current_partial_tile_coord.append(output)
        return

    intcode = "2"+intcode[1:] if insert_coin else intcode

    def paddle_input():
        if (current_ball_x == current_paddle_x):
            return 0
        direction = math.trunc(math.copysign(
            1, current_ball_x - current_paddle_x))
        # print("current_ball_x", current_ball_x,
        #       "current_paddle_x", current_paddle_x, "direction", direction)
        return direction

    run({"program": intcode}, False, None, render_buffered_output,
        input_func if interactive else paddle_input)
    return score
