#!/usr/bin/env python3

from orbit_map import count_transits


def read(file_path):
    input_file = open(file_path, 'r')
    input_raw = input_file.read()
    input_file.close()
    return input_raw


input_text = read('input.txt')
print(count_transits("YOU", "SAN", input_text))
