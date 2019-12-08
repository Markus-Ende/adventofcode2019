
from day7.intcode_interpreter import run
from itertools import permutations


def thruster_output(intcode, phase_setting_sequence):
    input_signal = 0

    for phase_setting in phase_setting_sequence:
        def store_output(x):
            nonlocal input_signal
            input_signal = x
        run(intcode, 0, False, (phase_setting, input_signal), store_output)

    return input_signal


def max_thruster_output(intcode):
    max_thruster_output = 0

    for phase_setting_sequence in permutations((0, 1, 2, 3, 4)):
        max_thruster_output = max(
            max_thruster_output, thruster_output(intcode, phase_setting_sequence))

    return max_thruster_output
