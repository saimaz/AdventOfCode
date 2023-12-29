import argparse
import networkx as nx


def calculate(data):
    row, column = len(data), len(data[0])
    graph = nx.DiGraph()
    start, end = None, None

    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }

    for r in range(row):
        for c in range(column):
            if data[r][c] != '#':
                for dr, dc in directions.values():
                    if 0 <= r + dr < row and 0 <= c + dc < column and data[r + dr][c + dc] != '#':
                        if data[r][c] in directions and directions[data[r][c]] != (dr, dc):
                            continue
                        graph.add_edge((r, c), (r + dr, c + dc))

    for c in range(column):
        if data[0][c] == '.':
            start = (0, c)
        if data[row - 1][c] == '.':
            end = (row - 1, c)

    if start is None or end is None:
        return "not ok, think about it"

    max_length = [0]

    def dfs(start_node):
        stack = [(start_node, {start_node}, 0)]
        while stack:
            node, visited, length = stack.pop()
            if node == end:
                max_length[0] = max(max_length[0], length)
                continue
            for neighbor in graph.neighbors(node):
                if neighbor not in visited:
                    new_visited = visited.copy()
                    new_visited.add(neighbor)
                    stack.append((neighbor, new_visited, length + 1))

    dfs(start)
    return max_length[0]


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
