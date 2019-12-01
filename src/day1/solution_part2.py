import math
import day1.solution_part1


def calculate_fuel_recursively(mass):
    current_fuel_input = mass
    total_fuel = 0
    while True:
        new_fuel = day1.solution_part1.calculate_fuel(current_fuel_input)
        if (new_fuel <= 0):
            return total_fuel
        total_fuel += new_fuel
        current_fuel_input = new_fuel


def sum_fuel(masses):
    return sum(list(map(lambda x: calculate_fuel_recursively(x), masses)))
