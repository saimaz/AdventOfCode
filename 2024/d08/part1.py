from typing import List
from collections import defaultdict
from itertools import combinations


def solve(data: List[str]) -> int:
    antennas = defaultdict(set)
    max_y = len(data)
    max_x = len(data[0]) if max_y > 0 else 0

    for y, line in enumerate(data):
        for x, char in enumerate(line.strip()):
            if char != ".":
                antennas[char].add((x, y))

    antinodes = set()

    for points in antennas.values():
        for (x1, y1), (x2, y2) in combinations(points, 2):
            antinodes.add((x1 - (x2 - x1), y1 - (y2 - y1)))
            antinodes.add((x2 - (x1 - x2), y2 - (y1 - y2)))

    return sum(0 <= x < max_x and 0 <= y < max_y for x, y in antinodes)


def get_test_data():
    return """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""
