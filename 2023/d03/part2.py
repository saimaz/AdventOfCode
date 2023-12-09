import argparse


def get_complete_number(i, j, engine_map):
    nj = j
    while nj > 0 and engine_map[i][nj - 1].isdigit():
        nj -= 1

    number_str = ''
    while nj < len(engine_map[0]) and engine_map[i][nj].isdigit():
        number_str += engine_map[i][nj]
        nj += 1
    return int(number_str) if number_str else None


def get_adjacent_numbers(i, j, engine_map):
    adjacent_numbers = set()
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(engine_map) and 0 <= nj < len(engine_map[0]) and engine_map[ni][nj].isdigit():
            number = get_complete_number(ni, nj, engine_map)
            if number is not None:
                adjacent_numbers.add(number)
    return adjacent_numbers


def calculate(data):
    engine_map = [list(line.strip()) for line in data.strip().split('\n')]

    total_sum = 0
    for i in range(len(engine_map)):
        for j in range(len(engine_map[i])):
            if engine_map[i][j] == '*':
                adjacent_numbers = get_adjacent_numbers(i, j, engine_map)
                if len(adjacent_numbers) == 2:
                    nums = list(adjacent_numbers)
                    total_sum += nums[0] * nums[1]
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
