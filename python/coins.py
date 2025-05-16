"""https://projecteuler.net/problem=31"""

from itertools import combinations_with_replacement


def solver(goal) -> int:
    """Combinations of money to sum the goal (dynamic)"""
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [0] * (goal + 1)  # list of 0
    ways[0] = 1

    for coin in coins:
        for i in range(coin, goal + 1):
            ways[i]+=ways[i - coin]

    return ways[goal]


solver(5)  # 4
solver(10)  # 11
solver(17)  # 28
solver(25)  # 68
solver(50)  # 451
solver(100)  # 4563
solver(200)  # 73682


def slowver(goal) -> int:
    """Combinations of money to sum the goal"""
    coins = [1, 2, 5, 10, 20, 50, 100, 200]

    combs = 0
    for i in range(1, goal + 1):
        # print(i)
        result = [c for c in combinations_with_replacement(coins, i) if sum(c) == goal]
        if result:
            combs = combs + len(result)
            # print(result)
            # print(combs)
        # result.extend([c for c in combinations_with_replacement(coins, i) if sum(c) == goal])

    return combs


slowver(5)  # 4 combinations
slowver(10)  # 11 combinations
slowver(17)  # 28 combinations
slowver(25)  # 68 combinations
