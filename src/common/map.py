import sys


# Converts coordinates (that hold a character) to a string map.
# A coordinate must be specified as follows: (x, y, char)
# Coordinates are relative to an arbitrary center at (0,0).
# The map bounds will automatically be chosen to contain all coordinates.
def coords_to_map(coords, default_char=" ", mapping={}):
    min_x = sys.maxsize
    min_y = sys.maxsize
    max_x = -sys.maxsize
    max_y = -sys.maxsize
    map_dict = {}
    map = []
    for c in coords:
        min_x = min(min_x, c[0])
        min_y = min(min_y, c[1])
        max_x = max(max_x, c[0])
        max_y = max(max_y, c[1])
        map_dict[(c[0], c[1])] = mapping.get(c[2], c[2])
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            # print("get", x, y)
            map.append(map_dict.get((x, y), default_char))
        map.append("\n")
    if (len(map) > 0):
        map.pop(len(map)-1)
    map_as_string = "".join(map)
    # print(map_as_string)
    return map_as_string
