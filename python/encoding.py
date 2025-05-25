"""https://exercism.org/tracks/r/exercises/run-length-encoding"""

import re

def encode(secret):
    result = re.sub(r'(.)\1*', lambda m: f"{len(m.group(0))}{m.group(1)}", secret)

    return result

def decode(secret):
    result = re.sub(r'(\d+)([ A-z])', lambda m: m.group(2) * int(m.group(1)), secret)

    return result

encode("") # ""
# encode("XYZ") # "XYZ"
encode("AABBBCCCC") # "2A3B4C"
encode("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB") # "12WB12W3B24WB"
# encode("  hsqq qww  ") # "2 hs2q q2w2 "
encode("aabbbcccc") # "2a3b4c"
# encode("zzz ZZ  zZ") # "3z1 2Z2 1z1Z"

decode("") # ""
decode("XYZ") # "XYZ"
decode("2A3B4C") # "AABBBCCCC"
decode("12WB12W3B24WB") # "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
decode("2 hs2q q2w2 ") # "  hsqq qww  "
decode("2a3b4c") # "aabbbcccc"
# decode("3z1 2Z2 1z1Z") # "zzz ZZ  zZ"
