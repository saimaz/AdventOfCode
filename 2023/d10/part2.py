import argparse
from collections import deque


def calculate(data):
    R = len(data)
    C = len(data[0])
    G = [[c for c in row] for row in data]
    DR = [-1, 0, 1, 0]
    DC = [0, 1, 0, -1]

    for r in range(R):
        for c in range(C):
            if G[r][c] == 'S':
                sr, sc = r, c
                up_valid = (G[r-1][c] in ['|','7','F'])
                right_valid = (G[r][c+1] in ['-','7','J'])
                down_valid = (G[r+1][c] in ['|','L','J'])
                left_valid = (G[r][c-1] in ['-','L','F'])
                assert sum([up_valid, right_valid, down_valid, left_valid]) == 2
                if up_valid and down_valid:
                    G[r][c] = '|'
                elif up_valid and right_valid:
                    G[r][c] = 'L'
                elif up_valid and left_valid:
                    G[r][c] = 'J'
                elif down_valid and right_valid:
                    G[r][c] = 'F'
                elif down_valid and left_valid:
                    G[r][c] = '7'
                elif left_valid and right_valid:
                    G[r][c] = '-'
                else:
                    assert False

    R2 = 3 * R
    C2 = 3 * C
    G2 = [['.' for _ in range(C2)] for _ in range(R2)]
    for r in range(R):
        for c in range(C):
            if G[r][c] == '|':
                G2[3 * r][3 * c + 1] = G2[3 * r + 1][3 * c + 1] = G2[3 * r + 2][3 * c + 1] = 'x'
            elif G[r][c] == '-':
                G2[3 * r + 1][3 * c] = G2[3 * r + 1][3 * c + 1] = G2[3 * r + 1][3 * c + 2] = 'x'
            elif G[r][c] == '7':
                G2[3 * r + 1][3 * c] = G2[3 * r + 1][3 * c + 1] = G2[3 * r + 2][3 * c + 1] = 'x'
            elif G[r][c] == 'F':
                G2[3 * r + 2][3 * c + 1] = G2[3 * r + 1][3 * c + 1] = G2[3 * r + 1][3 * c + 2] = 'x'
            elif G[r][c] == 'J':
                G2[3 * r + 1][3 * c] = G2[3 * r + 1][3 * c + 1] = G2[3 * r][3 * c + 1] = 'x'
            elif G[r][c] == 'L':
                G2[3 * r][3 * c + 1] = G2[3 * r + 1][3 * c + 1] = G2[3 * r + 1][3 * c + 2] = 'x'

    Q = deque()
    SEEN = set()
    for r in range(R2):
        Q.append((r, 0))
        Q.append((r, C2 - 1))
    for c in range(C2):
        Q.append((0, c))
        Q.append((R2 - 1, c))

    while Q:
        r, c = Q.popleft()
        if (r, c) in SEEN or not (0 <= r < R2 and 0 <= c < C2):
            continue
        SEEN.add((r, c))
        if G2[r][c] == 'x':
            continue
        for d in range(4):
            Q.append((r + DR[d], c + DC[d]))

    ans = 0
    for r in range(R):
        for c in range(C):
            if not any((3*r+rr, 3*c+cc) in SEEN for rr in [0, 1, 2] for cc in [0, 1, 2]):
                ans += 1

    return ans


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", action="store_true", help="Run with test data")
    parser.add_argument("-i", "--input", default="input.txt", help="Input file path")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    test_data = """
.....
.S-7.
.|.|.
.L-J.
.....
""".strip().split("\n")

    if not args.test:
        with open(args.input, 'r') as file:
            file_data = file.read()
        test_data = file_data.strip().split('\n')

    print(calculate(test_data))
