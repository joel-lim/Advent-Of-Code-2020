"""
https://adventofcode.com/2020/day/9
"""
from xmas import Xmas

FILE = 'input.txt'

def main():
    xmas = Xmas(25)
    nums = parse_input(FILE)
    num = xmas.detect_error(nums)
    print(f'Part 1: {num}')
    print(f'Part 2: {xmas.crack(nums, num)}')

def parse_input(file):
    """
    Parses an input file to obtain a list of numbers
    """
    with open(file) as f:
        return [int(line[:-1]) for line in f]

if __name__ == '__main__':
    main()
