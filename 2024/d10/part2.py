from typing import List, Tuple, Set
from collections import deque


def solve(data: List[str]) -> int:
    grid = [list(row) for row in data]
    rows, cols = len(grid), len(grid[0])
    score = 0

    def get_neighbors(x: int, y: int) -> List[Tuple[int, int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                neighbors.append((nx, ny))
        return neighbors

    def count_trails(start: Tuple[int, int]) -> int:
        queue = deque([(start, [start])])
        all_trails = set()

        while queue:
            (x, y), path = queue.popleft()
            current_height = int(grid[x][y])

            for nx, ny in get_neighbors(x, y):
                neighbor_height = int(grid[nx][ny])

                if neighbor_height == current_height + 1:
                    new_path = path + [(nx, ny)]
                    if neighbor_height == 9:
                        all_trails.add(tuple(new_path))
                    else:
                        queue.append(((nx, ny), new_path))

        return len(all_trails)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "0":
                score += count_trails((i, j))

    return score


def get_test_data():
    return """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""
