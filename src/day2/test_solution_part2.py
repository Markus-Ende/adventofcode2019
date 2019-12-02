import day2.solution_part1
import day2.solution_part2


def test_solution_part2():
    intcode = read('src/day2/input.txt')
    tokenized = day2.solution_part1.tokenize_program(intcode)

    assert day2.solution_part2.find_solution(tokenized) == 3892


def read(file_path):
    input_file = open(file_path, 'r')
    input_raw = input_file.read()
    input_file.close()
    return input_raw
