from typing import List, Tuple
from collections import deque, defaultdict


def find_perimeter(data: List[str], start: Tuple[int, int], visited: set) -> Tuple[int, int]:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    rows, cols = len(data), len(data[0])
    queue = deque([start])
    visited.add(start)
    region_char = data[start[0]][start[1]]

    area = 0
    perimeter = 0

    while queue:
        x, y = queue.popleft()
        area += 1

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                if data[nx][ny] == region_char and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
                elif data[nx][ny] != region_char:
                    perimeter += 1
            else:
                perimeter += 1

    return area, perimeter


def solve(data: List[str]):
    rows, cols = len(data), len(data[0])
    visited = set()
    total_price = 0

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                area, perimeter = find_perimeter(data, (r, c), visited)
                if area > 0:
                    total_price += area * perimeter

    return total_price


def get_test_data():
    return """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""