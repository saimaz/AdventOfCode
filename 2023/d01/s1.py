import sys


def calculate(file_path):
    total_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            digits = [char for char in line if char.isdigit()]
            if digits:
                first_digit, last_digit = digits[0], digits[-1]
                total_sum += int(first_digit + last_digit)
    return total_sum


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-s":
        file_path = "input.txt"
    else:
        file_path = "input_test.txt"

    result = calculate(file_path)
    print("Answer:", result)
