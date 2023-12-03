import sys


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


def calculate(file_path):
    with open(file_path, 'r') as file:
        engine_map = [list(line.strip()) for line in file.readlines()]

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


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-s":
        file_path = "input.txt"
    else:
        file_path = "input_test.txt"

    result = calculate(file_path)
    print("Answer:", result)
