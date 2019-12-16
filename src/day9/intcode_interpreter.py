def run(initial_state, single_step=False, input_sequence=None, output_callback=None, input_func=None):
    """
    start of inner functions
    """
    def out(x):
        return print(x) if output_callback == None else output_callback(x)

    def execute_add(i, tokenized_program):
        parameter_modes = parse_parameter_modes(tokenized_program[i])

        operand1 = read_value(i+1, tokenized_program, parameter_modes[0])
        operand2 = read_value(i+2, tokenized_program, parameter_modes[1])
        write_value(operand1 + operand2, i+3,
                    tokenized_program, parameter_modes[2])
        return i+4

    def parse_parameter_modes(opcode):
        return list(map(lambda m: m, reversed(
            ("0000"+str(opcode))[:-2])))

    def read_value(i, tokenized_program, mode):
        if (mode == '0'):
            # position mode
            adr_target = tokenized_program[i]
            return tokenized_program[adr_target] if adr_target < len(tokenized_program) else 0
        elif (mode == '2'):
            # relative mode
            adr_target = relative_base + tokenized_program[i]
            return tokenized_program[adr_target] if adr_target < len(tokenized_program) else 0
        else:
            # direct mode
            return tokenized_program[i]

    def write_value(value, adr_parameter, tokenized_program, mode):
        # adr_parameter is the adress that stores the target adress to write into (adr_target)
        adr_target = tokenized_program[adr_parameter]
        if (mode == '2'):
            adr_target += relative_base
        if (adr_target >= len(tokenized_program)):
            # dynamically extend program memory with zeroes
            tokenized_program += [0 for _ in range(
                0, adr_target - len(tokenized_program) + 1)]
        tokenized_program[adr_target] = value

    def execute_multiply(i, tokenized_program):
        parameter_modes = parse_parameter_modes(tokenized_program[i])

        operand1 = read_value(i+1, tokenized_program, parameter_modes[0])
        operand2 = read_value(i+2, tokenized_program, parameter_modes[1])
        write_value(operand1 * operand2, i+3,
                    tokenized_program, parameter_modes[2])
        return i+4

    def execute_input(i, tokenized_program):
        parameter_modes = parse_parameter_modes(tokenized_program[i])
        userinput = int(next(input_generator)
                        if input_generator != None else input_func() if input_func != None else input())
        write_value(userinput, i+1, tokenized_program, parameter_modes[0])
        return i+2

    def execute_output(i, tokenized_program):
        parameter_modes = parse_parameter_modes(tokenized_program[i])

        value = read_value(i+1, tokenized_program, parameter_modes[0])
        out(value)
        return i+2

    def execute_jump_if_true(i, tokenized_program):
        parameter_modes = parse_parameter_modes(tokenized_program[i])

        condition = read_value(i+1, tokenized_program, parameter_modes[0])

        if (condition == 0):
            return i+3
        else:
            return read_value(i+2, tokenized_program, parameter_modes[1])

    def execute_jump_if_false(i, tokenized_program):
        parameter_modes = parse_parameter_modes(tokenized_program[i])

        condition = read_value(i+1, tokenized_program, parameter_modes[0])

        if (condition != 0):
            return i+3
        else:
            return read_value(i+2, tokenized_program, parameter_modes[1])

    def execute_less_than(i, tokenized_program):
        parameter_modes = parse_parameter_modes(tokenized_program[i])

        operand1 = read_value(i+1, tokenized_program, parameter_modes[0])
        operand2 = read_value(i+2, tokenized_program, parameter_modes[1])

        write_value(1 if operand1 < operand2 else 0, i+3,
                    tokenized_program, parameter_modes[2])

        return i+4

    def execute_equals(i, tokenized_program):
        parameter_modes = parse_parameter_modes(tokenized_program[i])

        operand1 = read_value(i+1, tokenized_program, parameter_modes[0])
        operand2 = read_value(i+2, tokenized_program, parameter_modes[1])

        write_value(1 if operand1 == operand2 else 0, i+3,
                    tokenized_program, parameter_modes[2])

        return i+4

    def execute_adjust_rbase(i, tokenized_program):
        parameter_modes = parse_parameter_modes(tokenized_program[i])

        parameter = read_value(i+1, tokenized_program, parameter_modes[0])

        nonlocal relative_base
        relative_base += parameter

        return i+2

    def execute_halt(i, tokenized_program):
        return -1

    def run_command(program_counter, tokenized_program):
        commands = {
            1: execute_add,
            2: execute_multiply,
            3: execute_input,
            4: execute_output,
            5: execute_jump_if_true,
            6: execute_jump_if_false,
            7: execute_less_than,
            8: execute_equals,
            9: execute_adjust_rbase,
            99: execute_halt
        }

        opcode = tokenized_program[program_counter]

        if(opcode > 99):
            opcode = int(str(opcode)[-2:])

        command = commands[opcode]
        return command(program_counter, tokenized_program)

    def tokenize_program(program):
        return list(map(lambda x: int(x), program.split(",")))
    """
    end of inner functions
    """

    input_generator = None if input_sequence == None else iter(input_sequence)
    if (initial_state.get("program") == None):
        raise Exception("initial_state has no key 'program'")

    tokenized_program = tokenize_program(initial_state.get("program"))
    instruction_pointer = initial_state.get("ip", 0)
    relative_base = initial_state.get("rbase", 0)

    if (single_step):
        instruction_pointer = run_command(
            instruction_pointer, tokenized_program)
    else:
        while (instruction_pointer >= 0):
            instruction_pointer = run_command(
                instruction_pointer, tokenized_program)
    return {"rbase": relative_base, "ip": instruction_pointer, "program": ", ".join(str(x) for x in tokenized_program)}
