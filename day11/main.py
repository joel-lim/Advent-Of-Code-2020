"""
https://adventofcode.com/2020/day/11
"""
from grid import Grid

FILE = 'input.txt'


def main():
    grid = parse_input(FILE)
    print(f'Part 1: {grid.run_simulation1()}')
    print(f'Part 2: {grid.run_simulation2()}')


def parse_input(file):
    """
    Parses an input file to obtain a grid of seats
    """
    with open(file) as f:
        rows = [[seat for seat in line[:-1]] for line in f]
        return Grid(rows)


if __name__ == '__main__':
    main()
