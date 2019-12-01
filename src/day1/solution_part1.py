import math


def calculate_fuel(mass):
    return math.floor(mass / 3) - 2


def parse_input(input_raw):
    return list(map(lambda x: int(x), input_raw.split()))


def sum_fuel(masses):
    return sum(list(map(lambda x: calculate_fuel(x), masses)))


def read(file_path):
    input_file = open(file_path, 'r')
    input_raw = input_file.read()
    input_file.close()
    return input_raw
