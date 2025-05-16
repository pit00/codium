"""https://www.codewars.com/kata/66e03a09eeaad7e94d9f40a9"""

import numpy as np


def max_earning(earnings, k) -> int:
    """Maximum cash"""
    days = len(earnings)
    off = days // k
    print(off)

    max_possible = np.sum(sorted(earnings)[off:])
    print(max_possible)
    min_days = sorted(earnings)[:off]
    print(min_days)

    # split = [earnings[i:i+4] for i in range(0, len(earnings), k + 1)]
    # print(split)
    # for group in split:
    #     total = total + sum(group[:k])

    print(earnings)
    total = 0
    # blocks = int(np.ceil(days / (k + 1)))
    print(days)
    print(k+1)
    print(days % (k+1))
    # print(blocks)
    for i in range(0, days, k + 1):
        # earnings[i:i+k]
        print(i)
        print(earnings[i:i+k])
        total = total + sum(earnings[i:i+k])

    if max_possible == total:
        return total

    # print(sorted(earnings)[:off])
    # print(np.sum(sorted(earnings)[:off]))
    return total


max_earning([60, 70, 80, 40, 80, 90, 100, 20], 3)  # 480, excluding [40, 20]
# max_earning([60, 70, 0, 40, 80, 90, 100, 0], 3)
max_earning([45, 12, 78, 34, 56, 89, 23, 67, 91], 4)  # 460, excluding [12, 23]
# bypass the lowest in order
