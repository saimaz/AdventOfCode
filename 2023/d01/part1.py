import argparse


def calculate(data):
    total_sum = 0
    for line in data.strip().split('\n'):
        digits = [char for char in line if char.isdigit()]
        if digits:
            first_digit, last_digit = digits[0], digits[-1]
            total_sum += int(first_digit + last_digit)
    return total_sum


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", action="store_true", help="Run with test data")
    parser.add_argument("-i", "--input", default="input.txt", help="Input file path")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    test_data = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

    if args.test:
        result = calculate(test_data)
    else:
        with open(args.input, 'r') as file:
            file_data = file.read()
        result = calculate(file_data)

    print("Answer:", result)
