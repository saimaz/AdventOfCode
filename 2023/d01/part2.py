import argparse


def change_letters_to_numbers(line):
    number_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    i = 0
    while i < len(line):
        replaced = False
        for word, digit in number_map.items():
            if line[i:].startswith(word):
                line = line[:i] + digit + line[i + len(word):]
                i += len(digit) - 1
                replaced = True
                break
        if not replaced:
            i += 1

    return line


def calculate(data):
    total_sum = 0
    for line in data.strip().split('\n'):
        line = change_letters_to_numbers(line)
        digits = [char for char in line if char.isdigit()]
        if digits:
            first_digit, last_digit = digits[0], digits[-1]
            total_sum += int(first_digit + last_digit)
    return total_sum


def parse_arguments():
    parser = argparse.ArgumentParser(description="Calculate the sum for Advent of Code.")
    parser.add_argument("-t", "--test", action="store_true", help="Run with test data")
    parser.add_argument("-i", "--input", default="input.txt", help="Input file path")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    test_data = """oneabc2
pqrthreesix
aonebtwocfour
trebsevenuchet"""

    if args.test:
        result = calculate(test_data)
    else:
        with open(args.input, 'r') as file:
            file_data = file.read()
        result = calculate(file_data)

    print("Answer:", result)