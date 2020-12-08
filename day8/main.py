"""
https://adventofcode.com/2020/day/8
"""
from console import Console, InstructionFactory

FILE = 'input.txt'

def main():
    console = parse_input(FILE)
    acc, status = console.run()
    print(f'Part 1: {acc}')
    print(f'Part 2: {console.repair()}')

def parse_input(file):
    """
    Parses an input file to create a console with instructions
    """
    with open(file) as f:
        console = Console()
        factory = InstructionFactory()
        for line in f:
            op, arg = line[:-1].split()
            instruction = factory.create_instruction(op, int(arg))
            console.add_instruction(instruction)
        return console

if __name__ == '__main__':
    main()
