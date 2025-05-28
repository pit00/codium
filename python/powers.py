"""https://projecteuler.net/problem=30"""


def powers(digits) -> bool:
    """Digit Fifth Powers"""

    total = 0
    # min = 10 ** (digits - 1)
    # max = 10 ** digits - 1
    range_min = 10  # above 1 digits

    count = 1
    while True:
        max_value = count * (9**digits)
        print(max_value)
        max_digits = len(str(max_value))
        if max_digits > digits:
            range_max = 10 ** (max_digits) - 1
            break
        count += 1

    # print(range_min)
    # print(range_max)
    for i in range(range_min, range_max):
        numbs = str(i)
        # digits = len(numbs)

        # sum of each number pow number of digits
        calc = sum(int(numb) ** digits for numb in numbs)

        if calc == i:
            print(i)
            total += calc

    return total


powers(1)  # 0 (none)
powers(2)  # 0 (none)
powers(3)  # 1301 (153 370 371 407)
powers(4)  # 19316 (1634 8208 9474)
powers(5)  # 443839 (4150 4151 54748 92727 93084 194979)
powers(6)  # 548834 (548834)
