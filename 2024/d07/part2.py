from typing import List


def solve(data: List[str]) -> int:
    def try_remake(target: int, current: int, operands: List[int]) -> bool:
        if not operands:
            return target == current
        next_operand = operands[0]
        remaining = operands[1:]
        return (
            try_remake(target, current + next_operand, remaining) or
            try_remake(target, current * next_operand, remaining) or
            try_remake(target, int(f"{current}{next_operand}"), remaining)
        )

    total_calibration = 0
    for line in data:
        if not line.strip():
            continue
        target, numbers = line.split(":")
        target = int(target.strip())
        operands = list(map(int, numbers.strip().split()))
        if try_remake(target, operands[0], operands[1:]):
            total_calibration += target

    return total_calibration


def get_test_data():
    return """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
