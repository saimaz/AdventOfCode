import argparse


def calculate(data):
    def find_previous_value(numbers):
        layers = [numbers]
        while not all(d == 0 for d in layers[-1]):
            layers.append([layers[-1][i + 1] - layers[-1][i] for i in range(len(layers[-1]) - 1)])

        for i in range(len(layers) - 2, -1, -1):
            layers[i].insert(0, layers[i][0] - layers[i + 1][0])

        return layers[0][0]

    sum_of_previous_values = 0

    for line in data:
        numbers = list(map(int, line.strip().split()))
        sum_of_previous_values += find_previous_value(numbers)

    return sum_of_previous_values


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
