import sys


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


def calculate(file_path):
    with open(file_path, 'r') as file:
        engine_map = [list(line.strip()) for line in file.readlines()]

    total_sum = 0
    for i in range(len(engine_map)):
        for j in range(len(engine_map[i])):
            if engine_map[i][j] == '*':
                adjacent_numbers = get_adjacent_numbers(i, j, engine_map)
                if len(adjacent_numbers) == 2:
                    nums = list(adjacent_numbers)
                    total_sum += nums[0] * nums[1]
    return total_sum


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-s":
        file_path = "input.txt"
    else:
        file_path = "input_test.txt"

    result = calculate(file_path)
    print("Answer:", result)
