import argparse


def calculate(data):
    lines = data.strip().split('\n')

    times = [int(x) for x in lines[0].split(":")[1].split(" ") if x.strip()]
    distances = [int(x) for x in lines[1].split(":")[1].split(" ") if x.strip()]

    total_ways = 1
    for time, distance in zip(times, distances):
        wins = 0
        for i in range(time):
            if i * (time - i) > distance:
                wins += 1
        total_ways *= wins

    return total_ways


def parse_arguments():
    parser = argparse.ArgumentParser()
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
