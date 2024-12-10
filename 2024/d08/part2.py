from typing import List
from collections import defaultdict
from itertools import combinations


def is_valid(p, max_x, max_y):
    return 0 <= p[0] < max_x and 0 <= p[1] < max_y


def generate_antinodes(p1, p2):
    # p1 - (p2 - p1)
    # p2 - (p1 - p2)

    np1 = p1[0] - (p2[0] - p1[0]), p1[1] - (p2[1] - p1[1])
    np2 = p2[0] - (p1[0] - p2[0]), p2[1] - (p1[1] - p2[1])

    return np1, np2


def generate_all_antinodes(p1, p2, max_x, max_y):
    antinodes = set()

    x1, y1 = p1
    x2, y2 = p2

    for y3 in range(max_y):
        for x3 in range(max_x):
            if abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0:
                antinodes.add((x3, y3))

    return antinodes


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
            all_antinodes = generate_all_antinodes((x1, y1), (x2, y2), max_x, max_y)
            antinodes.update(all_antinodes)

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
