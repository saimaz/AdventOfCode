import argparse


def calculate(data):
    def find_next(numbers):
        seq = [numbers]
        while not all(d == 0 for d in seq[-1]):
            seq.append([seq[-1][i + 1] - seq[-1][i] for i in range(len(seq[-1]) - 1)])

        for i in range(len(seq) - 2, -1, -1):
            seq[i].append(seq[i][-1] + seq[i + 1][-1])

        return seq[0][-1]

    sum = 0
    for line in data:
        numbers = list(map(int, line.strip().split()))
        sum += find_next(numbers)

    return sum


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", action="store_true", help="Run with test data")
    parser.add_argument("-i", "--input", default="input.txt", help="Input file path")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    test_data = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
""".strip().split("\n")

    if not args.test:
        with open(args.input, 'r') as file:
            file_data = file.read()
        test_data = file_data.strip().split('\n')

    print(calculate(test_data))
