import sys


def parse_draw(draw):
    cubes = {}
    for part in draw.split(', '):
        count, color = part.split()
        cubes[color] = int(count)
    return cubes


def minimum_cubes_required(draws):
    min_cubes = {'red': 0, 'green': 0, 'blue': 0}
    for draw in draws:
        cubes = parse_draw(draw)
        for color in min_cubes:
            min_cubes[color] = max(min_cubes[color], cubes.get(color, 0))
    return min_cubes


def calculate_power(min_cubes):
    return min_cubes['red'] * min_cubes['green'] * min_cubes['blue']


def calculate(file_path):
    total_power_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            game_id, draw_data = line.strip().split(': ')
            draws = draw_data.split('; ')
            min_cubes = minimum_cubes_required(draws)
            total_power_sum += calculate_power(min_cubes)
    return total_power_sum


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-s":
        file_path = "input.txt"
    else:
        file_path = "input_test.txt"

    result = calculate(file_path)
    print("Answer:", result)
