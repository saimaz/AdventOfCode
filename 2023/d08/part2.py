import argparse
import re


def calculate(data):
    lines = data.strip().split("\n")
    ws = [re.findall("\w+", line) for line in lines]

    (dirs,), _, *moves = ws
    move = {
        "L": {start: l for start, l, _ in moves},
        "R": {start: r for start, _, r in moves},
    }

    starts = [start for start in move['L'] if start.endswith('A')]
    current_nodes = set(starts)

    i = 0
    while True:
        d = dirs[i % len(dirs)]
        current_nodes = {move[d][node] for node in current_nodes}
        if all(node.endswith('Z') for node in current_nodes):
            return i + 1
        i += 1


def parse_arguments():
    parser = argparse.ArgumentParser(description="Calculate the steps to reach ZZZ for Advent of Code.")
    parser.add_argument("-t", "--test", action="store_true", help="Run with test data")
    parser.add_argument("-i", "--input", default="input.txt", help="Input file path")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    test_data = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

    if args.test:
        result = calculate(test_data)
    else:
        with open(args.input, 'r') as file:
            file_data = file.read()
        result = calculate(file_data)

    print("Answer:", result)
