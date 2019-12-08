from day8.space_image_format import parse_layers, decode
from common.io import read


def test_solution_part2():
    imagesrc = read("src/day8/input.txt")
    layers = parse_layers(imagesrc, 25, 6)
    solution = decode(layers)

    # FHJUL
    expected = ("1111010010001101001010000"
                "1000010010000101001010000"
                "1110011110000101001010000"
                "1000010010000101001010000"
                "1000010010100101001010000"
                "1000010010011000110011110")

    assert solution == expected
