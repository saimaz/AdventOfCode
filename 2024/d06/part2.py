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

    start_row, start_col, start_dir = None, None, None
    for r in range(rows):
        for c in range(cols):
            if data[r][c] in "^>v<":
                start_row, start_col = r, c
                start_dir = "^>v<".index(data[r][c])
                break

    def simulate_with_obstacle(obstacle_row, obstacle_col):
        guard_row, guard_col, guard_dir = start_row, start_col, start_dir
        visited = set()
        visited.add((guard_row, guard_col, guard_dir))

        while True:
            dr, dc = directions[guard_dir]
            next_row, next_col = guard_row + dr, guard_col + dc

            if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
                return False  # out of grid

            next_cell = (
                "#" if (next_row == obstacle_row and next_col == obstacle_col) else data[next_row][next_col]
            )
            if next_cell == "#":
                guard_dir = (guard_dir + 1) % 4  # right
            else:
                guard_row, guard_col = next_row, next_col  # forward

            state = (guard_row, guard_col, guard_dir)
            if state in visited:
                return True  # loop
            visited.add(state)

    valid_positions = 0
    for r in range(rows):
        for c in range(cols):
            if data[r][c] == "#" or (r == start_row and c == start_col):
                continue

            if simulate_with_obstacle(r, c):
                valid_positions += 1

    return valid_positions


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

