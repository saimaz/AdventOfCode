import argparse


def calculate(data):
    lines = data.strip().split('\n')

    time = int(lines[0].split(":")[1].replace(" ", ""))
    distance = int(lines[1].split(":")[1].replace(" ", ""))

    wins = 0
    for i in range(1, time):
        if i * (time - i) > distance:
            wins += 1

    return wins


def parse_arguments():
    parser = argparse.ArgumentParser(description="Calculate the number of wins for Advent of Code.")
    parser.add_argument("-t", "--test", action="store_true", help="Run with test data")
    parser.add_argument("-i", "--input", default="input.txt", help="Input file path")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    test_data = """
Time:      7  15   30
Distance:  9  40  200
"""

    if args.test:
        result = calculate(test_data)
    else:
        with open(args.input, 'r') as file:
            file_data = file.read()
        result = calculate(file_data)

    print("Answer:", result)
