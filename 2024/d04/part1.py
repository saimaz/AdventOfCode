from typing import List


def solve(data: List[str]) -> int:
    rows = len(data)
    cols = len(data[0])
    xmas = "XMAS"
    xmas_l = len(xmas)
    answer = 0

    directions = [
        (0, 1),   # right
        (1, 0),   # down
        (1, 1),   # down right
        (1, -1),  # down left
        (0, -1),  # left
        (-1, 0),  # up
        (-1, -1), # up left
        (-1, 1),  # up right
    ]

    for row in range(rows):
        for col in range(cols):
            for dr, dc in directions:
                if 0 <= row + (xmas_l - 1) * dr < rows and 0 <= col + (xmas_l - 1) * dc < cols:
                    match = True
                    for i in range(xmas_l):
                        if data[row + i * dr][col + i * dc] != xmas[i]:
                            match = False
                            break
                    if match:
                        answer += 1

    return answer


def get_test_data():
    return """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""