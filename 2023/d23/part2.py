import argparse


def calculate(data):
    row, column = len(data), len(data[0])
    start, end = (0, data[0].index('.')), (row - 1, data[-1].index('.'))
    points = [start, end]

    directions = [
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0)
    ]

    for r in range(row):
        for c in range(column):
            if data[r][c] != '#':
                neighbors = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < column and data[nr][nc] != '#':
                        neighbors += 1
                if neighbors >= 3:
                    points.append((r, c))

    graph = {pt: {} for pt in points}
    for sr, sc in points:
        stack = [(0, sr, sc)]
        seen = {(sr, sc)}

        while stack:
            n, r, c = stack.pop()
            if n != 0 and (r, c) in points:
                graph[(sr, sc)][(r, c)] = n
                continue

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < column and data[nr][nc] != '#' and (nr, nc) not in seen:
                    stack.append((n + 1, nr, nc))
                    seen.add((nr, nc))

    visited = set()

    def dfs(pt):
        if pt == end:
            return 0

        m = -float("inf")
        visited.add(pt)
        for nx in graph[pt]:
            if nx not in visited:
                m = max(m, dfs(nx) + graph[pt][nx])
        visited.remove(pt)

        return m

    return dfs(start)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", action="store_true", help="Run with test data")
    parser.add_argument("-i", "--input", default="input.txt", help="Input file path")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    test_data = """
#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
""".strip().split("\n")

    if not args.test:
        with open(args.input, 'r') as file:
            file_data = file.read()
        test_data = file_data.strip().split('\n')

    print("Answer:", calculate(test_data))
