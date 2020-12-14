"""
https://adventofcode.com/2020/day/14
"""
from program import ProgramV1, ProgramV2

FILE = 'input.txt'


def main():
    program1 = ProgramV1()
    program2 = ProgramV2()
    instructions = parse_input(FILE)
    for instruction in instructions:
        program1.execute(instruction)
        program2.execute(instruction)
    print(f'Part 1: {program1.get_sum()}')
    print(f'Part 2: {program2.get_sum()}')


def parse_input(file):
    """
    Parses an input file to obtain a list of instructions
    """
    with open(file) as f:
        return [line[:-1] for line in f]


if __name__ == '__main__':
    main()
