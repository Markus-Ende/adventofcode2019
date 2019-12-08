def parse_layers(input, width, height):
    size = width * height
    layers = []

    start = 0
    stop = size

    while (stop <= len(input)):
        layers.append([int(i) for i in input[start:stop]])
        start += size
        stop += size

    return layers
