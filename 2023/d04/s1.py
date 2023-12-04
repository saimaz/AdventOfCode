import sys


def calculate(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    total_points = 0

    for line in lines:
        parts = line.split('|')
        if len(parts) < 2:
            continue

        winning_numbers = parts[0].split()
        my_numbers = parts[1].split()

        winning_numbers = set(map(int, filter(str.isdigit, winning_numbers)))
        my_numbers = set(map(int, filter(str.isdigit, my_numbers)))

        matches = len(winning_numbers.intersection(my_numbers))
        if matches > 0:
            points = 2 ** (matches - 1)
        else:
            points = 0

        total_points += points

    return total_points


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-s":
        file_path = "input.txt"
    else:
        file_path = "input_test.txt"

    result = calculate(file_path)
    print("Answer:", result)
