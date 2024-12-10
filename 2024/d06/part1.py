from typing import List


def solve(data: List[str]) -> int:
    rows = len(data)
    cols = len(data[0])

    directions = [
        (-1, 0),  # up
        (0, 1),  # right
        (1, 0),  # down
        (0, -1),  # left
    ]

    guard_row, guard_col, guard_direction = None, None, None
    for r in range(rows):
        for c in range(cols):
            if data[r][c] in "^>v<":
                guard_row, guard_col = r, c
                guard_direction = "^>v<".index(data[r][c])
                break

    visited = set()
    visited.add(f"{guard_row},{guard_col}")

    while True:
        dr, dc = directions[guard_direction]
        next_row, next_col = guard_row + dr, guard_col + dc

        if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
            break  # out of grid

        if data[next_row][next_col] == "#":
            guard_direction = (guard_direction + 1) % 4
        else:
            guard_row, guard_col = next_row, next_col
            visited.add(f"{guard_row},{guard_col}")

    return len(visited)


def get_test_data() -> str:
    return """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""
