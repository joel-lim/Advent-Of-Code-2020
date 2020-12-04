"""
https://adventofcode.com/2020/day/3
"""
FILE = 'input.txt'

class Map:
    TREE = '#'
    SQUARE = '.'

    def __init__(self, rows):
        self.rows = rows
        self.height = len(rows)
        self.width = len(rows[0]) - 1

    def traverse_slope(self, right, down):
        no_trees = 0
        x = 0
        for y in range(0, self.height, down):
            if self.rows[y][(x * right) % self.width] == Map.TREE:
                no_trees += 1
            x += 1
        return no_trees

def parse_map(file):
    """
    Parses an input file to produce a map of trees and squares
    """
    with open(FILE) as f:
        return Map([line for line in f])

def main():
    map_ = parse_map(FILE)
    print(f'Part 1: {map_.traverse_slope(3, 1)}')

    part_2 = 1
    for right, down in ((1,1),(3,1),(5,1),(7,1),(1,2)):
        part_2 *= map_.traverse_slope(right, down)
    print(f'Part 2: {part_2}')

if __name__ == '__main__':
    main()
