from copy import deepcopy


class Grid:
    """
    Represents seating positions
    """
    # Seat states
    EMPTY = 'L'
    OCCUPIED = '#'
    FLOOR = '.'
    # Pre-computed neighbours
    NEIGHBOURS = ((-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1))

    def __init__(self, rows):
        self.rows = rows

    def run_simulation1(self):
        """
        Runs a simulation of seating based on problem 1 rules and returns number of occupied seats in final state
        """
        def predicate_occupied(
            rows, i, j): return self.count_neighbours(rows, i, j) >= 4
        def predicate_empty(
            rows, i, j): return self.count_neighbours(rows, i, j) == 0
        return self._run_simulation(predicate_occupied, predicate_empty)

    def run_simulation2(self):
        """
        Runs a simulation of seating based on problem 2 rules and returns number of occupied seats in final state
        """
        def predicate_occupied(
            rows, i, j): return self.count_visible(rows, i, j) >= 5
        def predicate_empty(
            rows, i, j): return self.count_visible(rows, i, j) == 0
        return self._run_simulation(predicate_occupied, predicate_empty)

    def _run_simulation(self, predicate_occupied, predicate_empty):
        """
        Runs a simulation of seating based on provided rules
        """
        rows = self.rows
        stable = False
        while not stable:
            stable = True
            new_rows = deepcopy(rows)
            for i, row in enumerate(rows):
                for j, seat in enumerate(row):
                    if seat == Grid.OCCUPIED and predicate_occupied(rows, i, j):
                        new_rows[i][j] = Grid.EMPTY
                        stable = False
                    elif seat == Grid.EMPTY and predicate_empty(rows, i, j):
                        new_rows[i][j] = Grid.OCCUPIED
                        stable = False
            rows = new_rows
        return sum(row.count(Grid.OCCUPIED) for row in rows)

    def count_neighbours(self, rows, i, j):
        """
        Counts number of occupied neighbouring seats for a given position in rows
        """
        count = 0
        for x, y in Grid.NEIGHBOURS:
            new_i = i + x
            new_j = j + y
            # Check if in bounds and occupied
            if 0 <= new_i < len(rows) and 0 <= new_j < len(rows[0]) and rows[new_i][new_j] == Grid.OCCUPIED:
                count += 1
        return count

    def count_visible(self, rows, i, j):
        """
        Counts number of occupied visible seats for a given position in rows
        """
        count = 0
        for x, y in Grid.NEIGHBOURS:
            # Trace visibility until bounds are reached or a seat is encountered
            new_i = i + x
            new_j = j + y
            while 0 <= new_i < len(rows) and 0 <= new_j < len(rows[0]):
                if rows[new_i][new_j] == Grid.EMPTY:
                    break
                if rows[new_i][new_j] == Grid.OCCUPIED:
                    count += 1
                    break
                new_i += x
                new_j += y
        return count
