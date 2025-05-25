"""https://projecteuler.net/problem=30"""

def powers(number) -> bool:
    """Digit Fifth Powers"""

    # convert to string, to easy handle, reconvert to int in sum
    numbs = str(number)
    digits = len(numbs)

    # sum of each number pow number of digits
    calc = sum(int(numb) ** digits for numb in numbs)

    if calc == number:
        return number
    return calc

powers(1634) # 1634
powers(8208) # 8208
powers(9474) # 9474

powers(1234) # 354
