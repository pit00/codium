"""https://projecteuler.net/problem=28"""


def powers(digits) -> bool:
    """Digit Fifth Powers"""

    5x5
    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13
    
    matrix = [
        [21, 22, 23, 24, 25],
        [21, 22, 23, 24, 25],
        [21, 22, 23, 24, 25],
        [21, 22, 23, 24, 25],
        [20,  7,  8,  9, 10],
        [19,  6,  1,  2, 11],
        [18,  5,  4,  3, 12],
        [17, 16, 15, 14, 13]
    ]
    size = len(matrix)
    base = 0
    total = 1 # last position
    while size > 1:
        print(size)
        # ↖
        # total += matrix[base][base]
        # print(matrix[base][base])
        # ↗
        pivot = matrix[base][size - 1]
        total += pivot
        print(pivot)
        total += (pivot - (size - 2))
        print(pivot - (size - 2))
        total += (pivot - ((size - 2) * 2))
        print(pivot - ((size - 2) * 2))
        total += (pivot - ((size - 2) * 3))
        print(pivot - ((size - 2) * 3))
        # print(matrix[base][size])
        # ↘
        # total += matrix[size][size]
        # print(matrix[size][size])
        # ↙
        # total += matrix[size][base]
        # print(matrix[size][base])
        base += 1
        size -= -4
