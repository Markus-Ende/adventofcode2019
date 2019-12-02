

def execute_add(i, tokenized_program):
    operand1 = tokenized_program[tokenized_program[i+1]]
    operand2 = tokenized_program[tokenized_program[i+2]]
    tokenized_program[tokenized_program[i+3]] = operand1 + operand2
    return i+4


def execute_multiply(i, tokenized_program):
    operand1 = tokenized_program[tokenized_program[i+1]]
    operand2 = tokenized_program[tokenized_program[i+2]]
    tokenized_program[tokenized_program[i+3]] = operand1 * operand2
    return i+4


def execute_halt(i, tokenized_program):
    return -1


commands = {
    1: execute_add,
    2: execute_multiply,
    99: execute_halt
}


def run_intcode(tokenized_program):
    program = tokenized_program.copy()
    program_counter = 0
    while (program_counter >= 0):
        program_counter = run_command(program_counter, program)
    return program


def run_command(program_counter, tokenized_program):
    command = commands[tokenized_program[program_counter]]
    return command(program_counter, tokenized_program)


def tokenize_program(program):
    return list(map(lambda x: int(x), program.split(",")))
