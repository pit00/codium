"""https://exercism.org/tracks/r/exercises/killer-sudoku-helper"""

from itertools import combinations


def solver(size, goal_sum, exclude=[]) -> list:
    """Solve cage for killer sudoku"""
    total = goal_sum
    if goal_sum > 9:
        total = 10

    numbs = list(range(1, total))
    # get combinations that equal to the sum
    result = [c for c in combinations(numbs, size) if sum(c) == goal_sum]
    result = [c for c in result if not any(x in exclude for x in c)]  # exclusions

    return result


solver(9, 45)  # [(1, 2, 3, 4, 5, 6, 7, 8, 9)]
solver(3, 7)  # [(1, 2, 4)]
solver(2, 10)  # [(1, 9), (2, 8), (3, 7), (4, 6)]
solver(2, 10, [1, 4])  # [(2, 8), (3, 7)]
