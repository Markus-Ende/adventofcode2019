#!/usr/bin/env python3

from sys import stdin
import tty
import termios

from day13.input import breakout
from day13.arcade_cabinet import run_game, render_screen_breakout


def input_single_char():
    fileno = stdin.fileno()
    stored_settings = termios.tcgetattr(fileno)
    try:
        tty.setraw(stdin.fileno())
        char = stdin.read(1)
    finally:
        termios.tcsetattr(fileno, termios.TCSADRAIN, stored_settings)
    return char


def sanitized_input():
    c = "invalid"
    mapping = {
        "w": "0",
        "a": "-1",
        "s": "0",
        "d": "1"
    }
    while c == "invalid":
        pressed_key = input_single_char()
        if (pressed_key == "t"):
            print("exit.")
            exit(0)
        c = mapping.get(pressed_key, "invalid")
    return c


print("Use 'w','s','a','d' to move.")
print("Press 't' to exit.")

score = 0


def print_screen(tiles):
    print(chr(27) + "[2J")
    global score
    print("__BREAKOUT__________________SCORE:", score, "\n")
    print(render_screen_breakout(tiles))
    print("___________________Press 't' to exit\n")


def update_score(points):
    global score
    score = points


run_game(breakout, print_screen, update_score, True, sanitized_input)
