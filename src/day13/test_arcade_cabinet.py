import pytest
from .input import breakout
from .arcade_cabinet import run_game, render_screen_breakout


def run_game_and_get_last_screen(input):
    renderings = []

    run_game(input, lambda x: renderings.append(x))
    last_screen = renderings[-1]
    return last_screen


@pytest.mark.parametrize("input,expected", [
    ([(0, 0, 0), (1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4)],
     ("     \n"
      " ▒   \n"
      "  ▄  \n"
      "   ═ \n"
      "    o")),
    (run_game_and_get_last_screen(breakout), (
        "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\n"
        "▒                                  ▒\n"
        "▒   ▄▄ ▄      ▄▄ ▄▄ ▄▄  ▄▄▄    ▄▄▄ ▒\n"
        "▒    ▄ ▄▄  ▄▄  ▄▄  ▄▄▄▄ ▄ ▄▄▄▄ ▄   ▒\n"
        "▒  ▄▄      ▄▄▄     ▄ ▄     ▄ ▄▄ ▄  ▒\n"
        "▒   ▄   ▄       ▄  ▄ ▄       ▄▄▄ ▄ ▒\n"
        "▒  ▄▄▄▄         ▄   ▄▄   ▄   ▄ ▄▄▄ ▒\n"
        "▒    ▄▄▄▄▄ ▄    ▄ ▄ ▄ ▄  ▄▄ ▄ ▄ ▄  ▒\n"
        "▒ ▄▄ ▄▄▄▄ ▄▄▄▄  ▄  ▄ ▄   ▄  ▄▄▄    ▒\n"
        "▒  ▄  ▄▄    ▄▄  ▄   ▄▄ ▄ ▄▄ ▄▄   ▄ ▒\n"
        "▒       ▄   ▄ ▄   ▄▄▄▄ ▄▄ ▄▄   ▄   ▒\n"
        "▒        ▄▄▄    ▄ ▄    ▄▄ ▄▄▄  ▄ ▄ ▒\n"
        "▒    ▄▄ ▄▄ ▄ ▄▄▄  ▄▄      ▄ ▄▄▄ ▄▄ ▒\n"
        "▒ ▄  ▄     ▄  ▄▄ ▄▄▄ ▄▄  ▄▄  ▄▄  ▄ ▒\n"
        "▒ ▄ ▄ ▄ ▄  ▄▄  ▄   ▄ ▄▄ ▄   ▄ ▄▄ ▄ ▒\n"
        "▒                                  ▒\n"
        "▒               o                  ▒\n"
        "▒                                  ▒\n"
        "▒                                  ▒\n"
        "▒                 ═                ▒\n"
        "▒                                  ▒"
    ))
])
def test_render_screen(input, expected):
    assert render_screen_breakout(input) == expected


@pytest.mark.parametrize("input,expected", [
    (breakout, 180),
])
def test_run_game(input, expected):
    last_screen = run_game_and_get_last_screen(input)
    amount_of_block_tiles = len([t for t in last_screen if t[2] == 2])
    print(render_screen_breakout(last_screen))
    assert(amount_of_block_tiles) == expected
