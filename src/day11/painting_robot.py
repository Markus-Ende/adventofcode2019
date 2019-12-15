from day9.intcode_interpreter import run as run_intcode
from common.map import coords_to_map


def paint_hull(intcode, starting_panel_color="0"):
    program_state = {"program": intcode}
    robot = (0, 0, "^")
    coords = {}
    current_panel_color = starting_panel_color

    while(program_state.get("ip", None) != -1):
        output = []
        while(len(output) < 2 and program_state.get("ip", None) != -1):
            program_state = run_intcode(
                program_state, True, [current_panel_color], lambda x: output.append(x))
        if (program_state.get("ip", None) == -1):
            break
        coords[(robot[0], robot[1])] = str(output[0])
        new_direction = "<^>v"[("<^>v".index(
            robot[2]) - 1) % 4] if output[1] == 0 else "<^>v"[("<^>v".index(robot[2]) + 1) % 4]

        move_forward = {
            "<": lambda r: (r[0] - 1, r[1], "<"),
            "^": lambda r: (r[0], r[1] - 1, "^"),
            ">": lambda r: (r[0] + 1, r[1], ">"),
            "v": lambda r: (r[0], r[1] + 1, "v"),
        }
        robot = move_forward[new_direction](robot)
        current_panel_color = coords.get((robot[0], robot[1]), "0")

    return {
        "amount_painted": len(coords),
        "picture": coords_to_map([(c[0], c[1], coords[c]) for c in coords], "0")}
