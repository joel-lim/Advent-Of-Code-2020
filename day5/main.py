"""
https://adventofcode.com/2020/day/5
"""

FILE = 'input.txt'

def main():
    passes = parse_input(FILE)
    highest_seat_id = max(pass_['seat_id'] for pass_ in passes)
    print(f'Part 1: {highest_seat_id}')
    my_seat = find_missing_seat(passes, highest_seat_id)
    print(f'Part 2: {my_seat}')


def parse_input(file):
    """
    Parses an input file to produce a list of boarding passes
    """
    passes = []
    with open(file) as f:
        for line in f:
            pass_ = make_pass(line[:-1])
            passes.append(pass_)
    return passes

def make_pass(code):
    row = parse_code(128, 'B', 'F', code[:7])
    col = parse_code(8, 'R', 'L', code[-3:])
    seat_id = row * 8 + col
    return {'row': row,
            'col': col,
            'seat_id': seat_id}

def parse_code(range_, upper, lower, code):
    low = 0
    high = range_ - 1
    for char in code:
        shift = (high - low + 1) // 2
        if char == lower:
            high -= shift
        elif char == upper:
            low += shift
        else:
            raise ValueError('Invalid code')
    return low

def find_missing_seat(passes, highest_seat_id):
    # Start from middle, search up and down for missing seat
    seat_ids = {pass_['seat_id'] for pass_ in passes}
    middle = highest_seat_id // 2
    max_offset = middle + 1
    for offset in range(max_offset):
        upper = middle + offset
        lower = middle - offset
        if upper not in seat_ids:
            return upper
        if lower not in seat_ids:
            return lower


if __name__ == '__main__':
    main()
