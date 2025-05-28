"""https://exercism.org/tracks/r/exercises/run-length-encoding"""

import re


def encode(secret) -> str:
    """Encoding like AABBBCCCC to 2A3B4C"""
    result = re.sub(
        r"(.)\1*",  # /(.)\1*/g
        # lambda match: f"{len(match.group(0))}{match.group(1)}", # includes 1
        lambda m: (
            f"{m.group(1)}"
            if len(m.group(0)) == 1
            else f"{len(m.group(0))}{m.group(1)}"
        ),
        secret,
    )
    # group(0) [$&]: all match (AA|BBB|CCCC = 2|3|4)
    # group(1) [$1]: group match ([A]A[B]BB[C]CCC)
    # result: $&$1 (excluding $& == 1) => 2A3B4C (each match)

    return result


def decode(secret) -> str:
    """Decoding like 2A3B4C to AABBBCCCC"""

    result = re.sub(
        r"(\d+)([ A-z])",  # /(\d+)([ A-z])/g
        lambda m: m.group(2) * int(m.group(1)),
        secret,
    )
    # group(1) [$1]: [2]A[3]B[4]C
    # group(2) [$2]: 2[A]3[B]4C
    # result: $2 * int($1) => AABBBCCCC (each match)

    return result


encode("") # ""
encode("XYZ") # "XYZ"
encode("AABBBCCCC") # "2A3B4C"
encode("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB") # "12WB12W3B24WB"
encode("  hsqq qww  ") # "2 hs2q q2w2 "
encode("aabbbcccc") # "2a3b4c"
encode("zzz ZZ  zZ") # "3z 2Z2 zZ"

decode("") # ""
decode("XYZ") # "XYZ"
decode("2A3B4C") # "AABBBCCCC"
decode("12WB12W3B24WB") # "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
decode("2 hs2q q2w2 ") # "  hsqq qww  "
decode("2a3b4c") # "aabbbcccc"
decode("3z 2Z2 zZ") # "zzz ZZ  zZ"
