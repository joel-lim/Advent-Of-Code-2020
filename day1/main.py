"""
https://adventofcode.com/2020/day/1
"""
FILE = 'input.txt'
SUM = 2020

def get_expenses(filename):
    with open(filename) as f:
        return [int(line) for line in f]

def find_pair_sum(expenses, sum_):
    """
    Finds a pair of numbers in iterable expenses that add up to sum_
    """
    expense_set = set()
    for expense in expenses:
        complement = sum_ - expense
        if complement in expense_set:
            return expense, complement
        expense_set.add(expense)
    raise ValueError(f'No two entries summing to {sum_}')

def main():
    expenses = get_expenses(FILE)
    # Find product of 2 numbers adding to 2020
    a, b = find_pair_sum(expenses, SUM)
    print(f'Part 1: {a * b}')

    # Find product of 3 numbers adding to 2020
    expense_set = set(expenses)
    for expense in expense_set:
        try:
            # Remove current expense in case it is used more than once
            expenses.remove(expense)
            c, d = find_pair_sum(expenses, SUM - expense)
            print(f'Part 2: {c * d * expense}')
            return
        except ValueError:
            continue

if __name__ == '__main__':
    main()
