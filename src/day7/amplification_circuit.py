
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


def thruster_output_with_feedback_loop(intcode, phase_setting_sequence):
    states = [
        # current instruction pointer, current program code, next input
        [0, intcode, 0],
        [0, intcode, None],
        [0, intcode, None],
        [0, intcode, None],
        [0, intcode, None],
    ]

    # initialize amplifiers with phase settings
    for i, state in enumerate(states):
        (current_ip, current_intcode, _) = state
        (ip, intcode) = run(current_intcode,
                            current_ip, True, [phase_setting_sequence[i]])
        states[i] = [ip, intcode, states[i][2]]

    def is_terminated():
        return any(list(map(lambda x: x[0] == -1, states)))

    def run_until_next_output(amplifier_number):
        output = None

        def store_output(x):
            nonlocal output
            output = x

        current_state = states[amplifier_number]
        if (current_state[2] == None):
            raise Exception(
                "No input for amplifier {}".format(amplifier_number))
        while (output == None and current_state[0] != -1):
            next_state = run(current_state[1], current_state[0], True,
                             [current_state[2]], store_output)
            current_state[0] = next_state[0]
            current_state[1] = next_state[1]

        # current_state[2] = None  # current input is consumed
        states[(amplifier_number + 1) % len(states)][2] = output

    current_amplifier = 0

    while (not is_terminated()):
        run_until_next_output(current_amplifier)
        current_amplifier = (current_amplifier + 1) % len(states)

    thruster_output = states[0][2]

    return thruster_output


def max_thruster_output(intcode, thruster_output_func=thruster_output, phase_settings_range=(0, 1, 2, 3, 4)):
    max_thruster_output = 0

    for phase_setting_sequence in permutations(phase_settings_range):
        max_thruster_output = max(
            max_thruster_output, thruster_output_func(intcode, phase_setting_sequence))

    return max_thruster_output
