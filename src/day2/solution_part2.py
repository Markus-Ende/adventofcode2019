import day2.solution_part1


def run(noun, verb, program):
    memory = program.copy()
    memory[1] = noun
    memory[2] = verb
    return day2.solution_part1.run_intcode(memory)[0]


def find_solution(program):
    solution = -1

    for noun in range(0, 100):
        for verb in range(0, 100):
            if (run(noun, verb, program) == 19690720):
                solution = 100 * noun + verb
                break

    return solution
