from day8.space_image_format import parse_layers
from common.io import read


def test_solution_part1():
    imagesrc = read("src/day8/input.txt")
    layers = parse_layers(imagesrc, 25, 6)
    layers.sort(key=lambda layer: len(list(filter(lambda x: x == 0, layer))))
    amount_of_1s = len(list(filter(lambda x: x == 1,  layers[0])))
    amount_of_2s = len(list(filter(lambda x: x == 2,  layers[0])))
    solution = amount_of_1s * amount_of_2s
    assert solution == 2250
