import argparse


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


def calculate(data):
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}
    total_sum = 0
    for line in data.strip().split('\n'):
        game_id, draw_data = line.strip().split(': ')
        draws = draw_data.split('; ')
        if is_valid_game(draws, max_cubes):
            total_sum += int(game_id.split(' ')[1])
    return total_sum


def parse_arguments():
    parser = argparse.ArgumentParser(description="Calculate the sum for Advent of Code.")
    parser.add_argument("-t", "--test", action="store_true", help="Run with test data")
    parser.add_argument("-i", "--input", default="input.txt", help="Input file path")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    test_data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

    if args.test:
        result = calculate(test_data)
    else:
        with open(args.input, 'r') as file:
            file_data = file.read()
        result = calculate(file_data)

    print("Answer:", result)
