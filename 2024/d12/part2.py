from typing import List, Tuple
from collections import deque, defaultdict


def find_perimeter(grid: List[List[str]], start: Tuple[int, int], visited: set) -> Tuple[int, int, int]:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    rows, cols = len(grid), len(grid[0])
    queue = deque([start])
    visited.add(start)
    region_char = grid[start[0]][start[1]]

    area = 0
    region_cells = set()

    while queue:
        x, y = queue.popleft()
        area += 1
        region_cells.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == region_char and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

    sides = calculate_sides(region_cells, grid)
    return area, 0, sides


def calculate_sides(region_cells: set, grid: List[List[str]]) -> int:
    rows, cols = len(grid), len(grid[0])
    edges = 0

    min_i = min(i for i, _ in region_cells)
    max_i = max(i for i, _ in region_cells)
    min_j = min(j for _, j in region_cells)
    max_j = max(j for _, j in region_cells)

    for i in range(min_i, max_i + 1):
        top_was_edge = False
        bottom_was_edge = False
        for j in range(min_j, max_j + 1):
            top_is_edge = (i, j) in region_cells and (i - 1, j) not in region_cells
            bottom_is_edge = (i, j) in region_cells and (i + 1, j) not in region_cells

            if top_is_edge and not top_was_edge:
                edges += 1
            if bottom_is_edge and not bottom_was_edge:
                edges += 1

            top_was_edge = top_is_edge
            bottom_was_edge = bottom_is_edge

    for j in range(min_j, max_j + 1):
        left_was_edge = False
        right_was_edge = False
        for i in range(min_i, max_i + 1):
            left_is_edge = (i, j) in region_cells and (i, j - 1) not in region_cells
            right_is_edge = (i, j) in region_cells and (i, j + 1) not in region_cells

            if left_is_edge and not left_was_edge:
                edges += 1
            if right_is_edge and not right_was_edge:
                edges += 1

            left_was_edge = left_is_edge
            right_was_edge = right_is_edge

    return edges


def solve(data: List[str]):
    grid = [list(line) for line in data if line.strip()]
    rows, cols = len(grid), len(grid[0])
    visited = set()
    total_price = 0

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                area, _, sides = find_perimeter(grid, (r, c), visited)
                if area > 0:
                    total_price += area * sides

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
