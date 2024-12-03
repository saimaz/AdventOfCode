from typing import List
import re


def solve(data: List[str]):
    data = ''.join(data)  # from list to 1 string line
    regex = r"mul\((\d+),(\d+)\)"
    matches = re.findall(regex, data)
    total = sum(int(x) * int(y) for x, y in matches)
    return total


def get_test_data():
    return """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""
