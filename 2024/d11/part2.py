from typing import List
from collections import Counter, defaultdict


def solve(data: List[str]):
    stones = Counter(list(map(int, data[0].split())))
    for _ in range(75):
        new_stones = defaultdict(int)
        for stone, count in stones.items():
            if stone == 0:
                new_stones[1] += count
            elif len(str(stone)) % 2 == 0:
                s = str(stone)
                new_stones[int(s[:len(s) // 2])] += count
                new_stones[int(s[len(s) // 2:])] += count
            else:
                new_stones[stone * 2024] += count

        stones = Counter(new_stones)

    return sum(stones.values())


def get_test_data():
    return """
0 1 10 99 999
"""
