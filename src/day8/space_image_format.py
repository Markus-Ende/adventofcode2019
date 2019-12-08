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


def decode(layers):
    size = len(layers[0])
    pixels = []
    for i in range(0, size):
        for l in layers:
            if (l[i] != 2):
                pixels.append(l[i])
                break

    return "".join([str(p) for p in pixels])
