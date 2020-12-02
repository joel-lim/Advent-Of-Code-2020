"""
https://adventofcode.com/2020/day/2
"""
FILE = 'input.txt'

class Policy:
    def __init__(self, letter, lower, upper):
        self.letter = letter
        self.lower = lower
        self.upper = upper

    def test1(self, password):
        return self.lower <= password.count(self.letter) <= self.upper

    def test2(self, password):
        # Take logical XOR
        return (password[self.lower - 1] == self.letter) != (password[self.upper - 1] == self.letter)

def parse_input(line):
    """
    Parses an input line and produces a policy and password
    """
    limits, letter, password = line.split()
    lower, upper = limits.split('-')
    policy = Policy(letter[0], int(lower), int(upper))
    return policy, password

def main():
    num_valid_1 = 0
    num_valid_2 = 0
    with open(FILE) as f:
        for line in f:
            policy, password = parse_input(line)
            if policy.test1(password):
                num_valid_1 += 1
            if policy.test2(password):
                num_valid_2 += 1
    print(f'Part 1: {num_valid_1}')
    print(f'Part 2: {num_valid_2}')

if __name__ == '__main__':
    main()
