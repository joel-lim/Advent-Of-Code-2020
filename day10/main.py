"""
https://adventofcode.com/2020/day/9
"""
FILE = 'input.txt'

def main():
    adapters = parse_input(FILE)
    adapters.sort()

    joltages = [0]
    joltages.extend(adapters)
    joltages.append(adapters[-1] + 3)

    differences = find_differences(joltages)
    print(f'Part 1: {differences[0] * differences[2]}')
    print(f'Part 2: {find_arrangements(joltages)}')

def parse_input(file):
    """
    Parses an input file to obtain a list of adapters
    """
    with open(file) as f:
        return [int(line[:-1]) for line in f]

def find_differences(sorted_nums):
    """
    Finds the distribution of differences between adjacent numbers in the given list
    """
    differences = [0] * 3
    for i in range(1, len(sorted_nums)):
        differences[sorted_nums[i] - sorted_nums[i - 1] - 1] += 1
    return differences

def find_arrangements(sorted_nums):
    """
    Finds no. arrangements such that the difference between every consecutive number is <=3
    Additional constraints: first num must be sorted_nums[0], last num must be sorted_nums[-1]
    """
    # Use dp to store no. arrangements from that idx
    dp = [0] * len(sorted_nums)
    dp[-1] = 1
    for i in range(-2, -len(dp) - 1, -1):
        arrangements = 0
        # Try arrangements with all connectable adapters
        j = i
        while j < 0:
            j += 1
            if sorted_nums[j] - sorted_nums[i] > 3:
                break
            arrangements += dp[j]
        dp[i] = arrangements
    return dp[0]

if __name__ == '__main__':
    main()
