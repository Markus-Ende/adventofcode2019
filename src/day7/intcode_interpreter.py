def run(intcode, initial_instruction_pointer=0, single_step=False, input_sequence=None, output_callback=None):
    input_generator = None if input_sequence == None else iter(input_sequence)

    def out(x):
        return print(x) if output_callback == None else output_callback(x)

    def execute_add(i, tokenized_program):
        parameter_modes = parse_parameter_modes(tokenized_program[i])

        operand1 = read_value(i+1, tokenized_program, parameter_modes[0])
        operand2 = read_value(i+2, tokenized_program, parameter_modes[1])
        tokenized_program[tokenized_program[i+3]] = operand1 + operand2
        return i+4

    def parse_parameter_modes(opcode):
        return list(map(lambda m: m, reversed(
            ("0000"+str(opcode))[:-2])))

    def read_value(i, tokenized_program, mode):
        if (mode == '0'):
            return tokenized_program[tokenized_program[i]]
        else:
            return tokenized_program[i]

    def execute_multiply(i, tokenized_program):
        parameter_modes = parse_parameter_modes(tokenized_program[i])

        operand1 = read_value(i+1, tokenized_program, parameter_modes[0])
        operand2 = read_value(i+2, tokenized_program, parameter_modes[1])
        tokenized_program[tokenized_program[i+3]] = operand1 * operand2
        return i+4

    def execute_input(i, tokenized_program):
        target_index = tokenized_program[i+1]
        userinput = int(next(input_generator)
                        if input_generator != None else input())
        tokenized_program[target_index] = userinput
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

        tokenized_program[tokenized_program[i+3]
                          ] = 1 if operand1 < operand2 else 0

        return i+4

    def execute_equals(i, tokenized_program):
        parameter_modes = parse_parameter_modes(tokenized_program[i])

        operand1 = read_value(i+1, tokenized_program, parameter_modes[0])
        operand2 = read_value(i+2, tokenized_program, parameter_modes[1])

        tokenized_program[tokenized_program[i+3]
                          ] = 1 if operand1 == operand2 else 0

        return i+4

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
            99: execute_halt
        }

        opcode = tokenized_program[program_counter]

        if(opcode > 99):
            opcode = int(str(opcode)[-2:])

        command = commands[opcode]
        return command(program_counter, tokenized_program)

    def tokenize_program(program):
        return list(map(lambda x: int(x), program.split(",")))

    tokenized_program = tokenize_program(intcode)
    instruction_pointer = initial_instruction_pointer
    if (single_step):
        instruction_pointer = run_command(
            instruction_pointer, tokenized_program)
    else:
        while (instruction_pointer >= 0):
            instruction_pointer = run_command(
                instruction_pointer, tokenized_program)
    return (instruction_pointer, tokenized_program)
