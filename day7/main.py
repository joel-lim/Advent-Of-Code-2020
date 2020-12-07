"""
https://adventofcode.com/2020/day/7
"""
from functools import reduce

FILE = 'input.txt'

class Bag:
    """
    Keeps track of what the bag can contain, and what bags can contain itself
    """
    def __init__(self, colour):
        self.colour = colour
        self.inners = {}
        self.outers = set()

    def add_inner(self, bag, qty):
        self.inners[bag] = qty
        bag.outers.add(self)

    def __eq__(self, other):
        return self.colour == other.colour

    def __hash__(self):
        return hash(self.colour)

def main():
    bags = parse_input(FILE)
    result = set()
    shiny_gold = bags['shiny gold']
    find_bags_that_hold(shiny_gold, result)
    print(f'Part 1: {len(result)}')
    print(f'Part 2: {find_num_bags_held(shiny_gold, {})}')

def parse_input(file):
    """
    Parses an input file to produce a map from colour to bag objects
    """
    with open(file) as f:
        bags = {}
        for line in f:
            outer, line = line.split(' bags ')
            bag = get_or_create_bag(outer, bags)
            line = line[8:]
            inner_lines = line.split(',')
            for inner_line in inner_lines:
                inner, qty = parse_inner(inner_line)
                if inner:
                    bag_inner = get_or_create_bag(inner, bags)
                    bag.add_inner(bag_inner, qty)
        return bags

def get_or_create_bag(colour, bags):
    """
    Add bag to the map if not already inside, then return the Bag object
    """
    if colour in bags:
        return bags[colour]
    bag = Bag(colour)
    bags[colour] = bag
    return bag

def parse_inner(inner_line):
    """
    Parses a line such as "4 dark fuchsia bags" into a colour and quantity
    If the line is "no other bags", return null for both colour and quantity
    """
    end_idx = inner_line.index(' bag')
    qty, colour = inner_line[:end_idx].strip().split(' ', 1)
    if qty == 'no':
        return None, None
    qty = int(qty)
    return colour, qty

def find_bags_that_hold(bag, result):
    """
    Returns all bags that could eventually hold the given bag 
    """
    for outer in bag.outers:
        if outer in result:
            continue
        result.add(outer)
        find_bags_that_hold(outer, result)

def find_num_bags_held(bag, dp):
    """
    Returns number of bags that are held by the given bag, with memoisation for repeated subproblems
    """
    if bag in dp:
        return dp[bag]
    num_held = 0
    for inner, qty in bag.inners.items():
        num_held += (1 + find_num_bags_held(inner, dp)) * qty
    dp[bag] = num_held
    return num_held

if __name__ == '__main__':
    main()
