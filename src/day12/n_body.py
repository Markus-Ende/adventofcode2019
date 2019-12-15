import re


def parse_system(input):
    lines = [l.strip() for l in input.split("\n")]
    system = []
    for l in lines:
        match = re.fullmatch("<x=(?P<x>.*), y=(?P<y>.*), z=(?P<z>.*)>", l)
        system.append({"pos": {"x": int(match.group("x")), "y": int(match.group("y")), "z": int(match.group("z"))},
                       "vel": {"x": 0, "y": 0, "z": 0}})
    return system


def simulate_steps(system, steps=1):
    def exectute_single_step(system):
        for i, moon in enumerate(system):
            other_moons = [m for j, m in enumerate(system) if i != j]
            gravity = {"x": 0, "y": 0, "z": 0}
            for other_moon in other_moons:
                for dim in "xyz":
                    if other_moon["pos"][dim] > moon["pos"][dim]:
                        gravity[dim] += 1
                    elif other_moon["pos"][dim] < moon["pos"][dim]:
                        gravity[dim] -= 1
            for dim in "xyz":
                moon["vel"][dim] += gravity[dim]
        for moon in system:
            for dim in "xyz":
                moon["pos"][dim] += moon["vel"][dim]

        return system

    for _ in range(0, steps):
        system = exectute_single_step(system)
    return system


def calculate_system_energy(system):
    energy = 0
    for moon in system:
        pot = 0
        kin = 0
        for dim in "xyz":
            pot += abs(moon["pos"][dim])
            kin += abs(moon["vel"][dim])
        energy += pot*kin
    return energy
