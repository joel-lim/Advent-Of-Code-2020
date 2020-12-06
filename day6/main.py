"""
https://adventofcode.com/2020/day/6
"""
from functools import reduce

FILE = 'input.txt'

def main():
    groups = parse_input(FILE)
    any_yeses = [get_any_yes(group) for group in groups]
    print(f'Part 1: {sum(len(any_yes) for any_yes in any_yeses)}')
    all_yeses = [get_all_yes(group) for group in groups]
    print(f'Part 2: {sum(len(all_yes) for all_yes in all_yeses)}')


def parse_input(file):
    """
    Parses an input file to produce a list of sets of questions answered by each group
    """
    with open(file) as f:
        groups = []
        group = []
        for line in f:
            if line == '\n':
                groups.append(group)
                group = []
            else:
                group.append(line[:-1])
        groups.append(group)
        return groups

def get_any_yes(group):
    return set(qn for person in group for qn in person)

def get_all_yes(group):
    return reduce(lambda acc, person: set(qn for qn in person if qn in acc), group)

if __name__ == '__main__':
    main()
