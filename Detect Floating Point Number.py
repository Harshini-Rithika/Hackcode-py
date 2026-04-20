import re

def is_valid_float(s):
    pattern = r'^[+-]?\d*\.\d+$'
    return bool(re.match(pattern, s))
n = int(input())
for _ in range(n):
    print(is_valid_float(input()))