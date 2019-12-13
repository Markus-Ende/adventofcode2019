from math import gcd, pi, atan2, degrees


def parse_asteroid_map(input):
    # coords = []
    # for y, line in enumerate(input.split()):
    #     for x, char in enumerate(line):
    #         if (char == "#"):
    #             coords.append((x, y))
    # return coords
    trimmed_lines = [l.strip() for l in input.split()]
    width = len(trimmed_lines[0])
    return [(i % width, i // width) for i, x in enumerate("".join(trimmed_lines)) if x == "#"]


def can_detect(asteroids, station, target):
    delta = (target[0] - station[0], target[1] - station[1])
    divisor = gcd(delta[0], delta[1])
    if (divisor == 1):
        return True
    delta_step = (delta[0] // divisor, delta[1] // divisor)
    check_pos = (station[0] + delta_step[0], station[1] + delta_step[1])
    while (check_pos != target):
        if (check_pos in asteroids):
            return False
        check_pos = (check_pos[0] + delta_step[0],
                     check_pos[1] + delta_step[1])
    return True


def count_detectable_asteroids(asteroids, station):
    counter = 0
    for a in [a for a in asteroids if a != station]:
        counter += 1 if can_detect(asteroids, station, a) else 0
    return counter


def find_best_station(asteroids):
    best_station = ((-1, -1), 0)
    for a in asteroids:
        detectable_asteroids = count_detectable_asteroids(asteroids, a)
        if (detectable_asteroids > best_station[1]):
            best_station = (a, detectable_asteroids)
    return best_station


def sort_for_laser_round(asteroids, station):
    def gradient_angle(a):
        gradient_angle = degrees(atan2(a[1] - station[1], a[0] - station[0]))
        asteroid_angle = (gradient_angle + 90) % 360
        return asteroid_angle

    def dist_to_station(a):
        return sum(abs(x-y) for x, y in zip(a, station))

    possible_targets = [(a, gradient_angle(a), dist_to_station(a))
                        for a in asteroids if a != station]
    possible_targets_sorted = sorted(
        possible_targets, key=lambda x: (x[1], x[2]))

    return [(a[0], a[1]) for a in possible_targets_sorted]


def shoot(asteroids, station):
    sorted_map = sort_for_laser_round(asteroids, station)
    shot_asteroids = []
    while (len(sorted_map) > 0):
        last_shot_angle = -1
        marked_indices_for_extinction = []
        for i, a in enumerate(sorted_map):
            if (a[1] != last_shot_angle):
                shot_asteroids.append(a[0])
                marked_indices_for_extinction.append(i)
                last_shot_angle = a[1]
        for i in reversed(marked_indices_for_extinction):
            sorted_map.pop(i)

    return shot_asteroids
