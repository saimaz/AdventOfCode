import sys


def parse_draw(draw):
    cubes = {}
    for part in draw.split(', '):
        count, color = part.split()
        cubes[color] = int(count)
    return cubes


def is_valid_game(draws, max_cubes):
    for draw in draws:
        cubes = parse_draw(draw)
        if any(cubes.get(color, 0) > max_cubes[color] for color in max_cubes):
            return False
    return True


def calculate(file_path):
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}
    total_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            game_id, draw_data = line.strip().split(': ')
            draws = draw_data.split('; ')
            if is_valid_game(draws, max_cubes):
                total_sum += int(game_id.split(' ')[1])
    return total_sum


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-s":
        file_path = "input.txt"
    else:
        file_path = "input_test.txt"

    result = calculate(file_path)
    print("Answer:", result)
