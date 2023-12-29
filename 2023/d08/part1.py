import argparse
import re


def calculate(data):
    dirs = data[0]
    moves = {}
    for line in data[2:]:
        # print(line)
        node, left, right = re.findall("(\w+)", line)
        moves[node] = {'L': left, 'R': right}

    current_node = 'AAA'
    steps = 0

    while current_node != 'ZZZ':
        direction = dirs[steps % len(dirs)]
        current_node = moves[current_node][direction]
        steps += 1

    return steps


def parse_arguments():
    parser = argparse.ArgumentParser()
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
    """.strip().split("\n")

    if not args.test:
        with open(args.input, 'r') as file:
            file_data = file.read()
        test_data = file_data.strip().split('\n')

    print(calculate(test_data))
