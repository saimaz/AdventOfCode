import argparse


def is_symbol(ch):
    return ch not in '0123456789.'


def check_for_symbol(i, j, number_length, engine_map):
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    for n in range(number_length):
        for dx, dy in directions:
            nx, ny = i + dx, j + n + dy
            if 0 <= nx < len(engine_map) and 0 <= ny < len(engine_map[nx]) and is_symbol(engine_map[nx][ny]):
                return True
    return False


def calculate(data):
    engine_map = [list(line.strip()) for line in data.strip().split('\n')]

    total_sum = 0
    visited = set()

    for i in range(len(engine_map)):
        j = 0
        while j < len(engine_map[i]):
            if engine_map[i][j].isdigit() and (i, j) not in visited:
                number_str = ''
                k = j
                while k < len(engine_map[i]) and engine_map[i][k].isdigit():
                    number_str += engine_map[i][k]
                    visited.add((i, k))
                    k += 1

                if check_for_symbol(i, j, k - j, engine_map):
                    total_sum += int(number_str)

                j = k
            else:
                j += 1

    return total_sum


def parse_arguments():
    parser = argparse.ArgumentParser(description="Calculate the sum for Advent of Code.")
    parser.add_argument("-t", "--test", action="store_true", help="Run with test data")
    parser.add_argument("-i", "--input", default="input.txt", help="Input file path")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    test_data = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

    if args.test:
        result = calculate(test_data)
    else:
        with open(args.input, 'r') as file:
            file_data = file.read()
        result = calculate(file_data)

    print("Answer:", result)
