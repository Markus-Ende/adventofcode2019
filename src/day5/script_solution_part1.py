#!/usr/bin/env python3

from intcode_computer import tokenize_program, run_intcode


def read(file_path):
    input_file = open(file_path, 'r')
    input_raw = input_file.read()
    input_file.close()
    return input_raw


intcode = read('input.txt')
tokenized = tokenize_program(intcode)
run_intcode(tokenized)
