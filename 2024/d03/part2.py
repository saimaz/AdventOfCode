from typing import List
import re


def solve(data: List[str]):
    data = ''.join(data)  # from list to 1 string line
    regex = r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))"
    matches = re.findall(regex, data)

    active = True
    total = 0

    for match in matches:
        if match[0] == "do()":
            active = True
        elif match[0] == "don't()":
            active = False
        elif "mul" in match[0] and active:
            total += int(match[1]) * int(match[2])

    return total


def get_test_data():
    return """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""
