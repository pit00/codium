"""https://exercism.org/tracks/r/exercises/armstrong-numbers"""

def armstrong(number) -> bool:
    """Check if a number is a armstrong number"""

    # convert to string, to easy handle, reconvert to int in sum
    numbs = str(number)
    digits = len(numbs)

    # sum of each number pow number of digits
    calc = sum(int(numb) ** digits for numb in numbs)

    if calc == number:
        return True
    return False

armstrong(0) # true
armstrong(5) # true
armstrong(10) # false
armstrong(153) # true
armstrong(100) # false
armstrong(9474) # true
armstrong(9475) # false
armstrong(9926315) # true
armstrong(9926314) # false
