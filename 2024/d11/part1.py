from typing import List


def solve(data: List[str]):
    stones = list(map(int, data[0].split()))

    for _ in range(25):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                mid = len(str(stone)) // 2
                left = int(str(stone)[:mid])
                right = int(str(stone)[mid:])
                new_stones.append(left)
                new_stones.append(right)
            else:
                new_stones.append(stone * 2024)
        stones = new_stones

    return len(stones)


def get_test_data():
    return """
0 1 10 99 999
"""
