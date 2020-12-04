"""
https://adventofcode.com/2020/day/4
"""

FILE = 'input.txt'
MANDATORY_FIELDS = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
EYE_COLORS = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}


def parse_input(file):
    """
    Parses an input file to produce a list of passports
    """
    passports = []
    with open(file) as f:
        passport = {}
        for line in f:
            if line != '\n':
                data = line.split()
                for datum in data:
                    k, v = datum.split(':')
                    passport[k] = v
            else:
                passports.append(passport)
                passport = {}
        # Add the last passport
        passports.append(passport)
    return passports


def contains_mandatory_fields(passport):
    for field in MANDATORY_FIELDS:
        if field not in passport:
            return False
    return True


def byr_valid(passport):
    byr = passport.get('byr')
    return len(byr) == 4 and '1920' <= byr <= '2002'


def iyr_valid(passport):
    iyr = passport.get('iyr')
    return len(iyr) == 4 and '2010' <= iyr <= '2020'


def eyr_valid(passport):
    eyr = passport.get('eyr')
    return len(eyr) == 4 and '2020' <= eyr <= '2030'


def hgt_valid(passport):
    hgt = passport.get('hgt')
    unit = hgt[-2:]
    num = hgt[:-2]
    if unit == 'cm':
        return '150' <= num <= '193'
    elif unit == 'in':
        return '59' <= num <= '76'
    return False


def hcl_valid(passport):
    hcl = passport.get('hcl')
    if hcl[0] != '#':
        return False
    try:
        int(hcl[1:], 16)
        return True
    except ValueError:
        return False


def ecl_valid(passport):
    return passport.get('ecl') in EYE_COLORS


def pid_valid(passport):
    pid = passport.get('pid')
    return len(pid) == 9 and pid.isnumeric()


def is_valid(passport):
    predicates = (contains_mandatory_fields, byr_valid, iyr_valid,
                  eyr_valid, hgt_valid, hcl_valid, ecl_valid, pid_valid)
    for predicate in predicates:
        if not predicate(passport):
            return False
    return True


def main():
    passports = parse_input(FILE)
    no_valid_1 = sum(1 for passport in passports if contains_mandatory_fields(passport))
    print(f'Part 1: {no_valid_1}')
    no_valid_2 = sum(1 for passport in passports if is_valid(passport))
    print(f'Part 2: {no_valid_2}')


if __name__ == '__main__':
    main()
