"""
https://adventofcode.com/2020/day/13
"""
import math
from functools import reduce

FILE = 'input.txt'
INT_MAX = float('inf')


def main():
    timestamp, buses = parse_input(FILE)
    bus, bus_time = get_earliest_bus(timestamp, buses)
    print(f'Part 1: {bus * (bus_time - timestamp)}')
    print(f'Part 2: {get_special_timestamp(buses)}')


def parse_input(file):
    """
    Parses an input file to obtain a timestamp and a list of active buses
    """
    with open(file) as f:
        timestamp = int(f.readline())
        buses = [int(x) if x != 'x' else None for x in f.readline().split(',')]
        return timestamp, buses


def get_earliest_bus(timestamp, buses):
    """
    Gets the earliest bus that departs after timestamp
    """
    earliest_bus = None
    earliest_time = INT_MAX
    for bus in buses:
        if not bus:
            continue
        bus_time = lowest_multiple_above(bus, timestamp)
        if bus_time < earliest_time:
            earliest_bus = bus
            earliest_time = bus_time
    return earliest_bus, earliest_time


def lowest_multiple_above(x, min_):
    """
    Gets the lowest multiple of x that is larger than or equal to min_
    """
    return math.ceil(min_ / x) * x


def get_special_timestamp(buses):
    """
    Gets the first timestamp where buses depart by <offset> minutes from each other
    """
    valid_buses = [(i, bus) for i, bus in enumerate(buses) if bus]
    # Use idea from Chinese Remainder Theorem
    first_bus = valid_buses[0][1]
    ans = 0
    current_product = first_bus
    for i, bus in valid_buses[1:]:
        while (ans + i) % bus != 0:
            ans += current_product
        current_product *= bus
    return ans


if __name__ == '__main__':
    main()
