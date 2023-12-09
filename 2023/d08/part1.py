import argparse
import re


def calculate(data):
    lines = data.strip().split("\n")
    dirs = re.findall("\w", lines[0])
    moves = [re.findall("\w+", line) for line in lines[2:]]

    move = {
        "L": {start: l for start, l, _ in moves},
        "R": {start: r for start, _, r in moves},
    }

    here = 'AAA'
    i = 0

    while here != 'ZZZ':
        d = dirs[i % len(dirs)]
        here = move[d][here]
        i += 1

    return i


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
