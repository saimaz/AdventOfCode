import argparse


def calculate(data):
    total_sum = 0
    for line in data.strip().split('\n'):
        total_sum += 1
    return total_sum


def parse_arguments():
    parser = argparse.ArgumentParser(description="Calculate the sum for Advent of Code.")
    parser.add_argument("-t", "--test", action="store_true", help="Run with test data")
    parser.add_argument("-i", "--input", default="input.txt", help="Input file path")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    test_data = """
aaa
bbb
ccc
"""

    if args.test:
        result = calculate(test_data)
    else:
        with open(args.input, 'r') as file:
            file_data = file.read()
        result = calculate(file_data)

    print("Answer:", result)
