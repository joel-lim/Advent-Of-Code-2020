"""
https://adventofcode.com/2020/day/12
"""
from ship import Ship, ShipWithWaypoint

FILE = 'input.txt'


def main():
    ship1 = Ship()
    ship2 = ShipWithWaypoint()
    instructions = parse_input(FILE)
    for instruction in instructions:
        ship1.read(instruction)
        ship2.read(instruction)
    print(f'Part 1: {ship1.manhattan_distance()}')
    print(f'Part 2: {ship2.manhattan_distance()}')


def parse_input(file):
    """
    Parses an input file to obtain a list of instructions
    """
    with open(file) as f:
        return [line[:-1] for line in f]


if __name__ == '__main__':
    main()
