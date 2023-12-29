import argparse

moves = {'|':'NS', '-':'EW', 'L':'NE', 'J':'NW', '7':'SW', 'F':'SE', '.':''}
reverse_dir = {'N': 'S', 'S': 'N', 'E':'W', 'W':'E'}
tile_adjust = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}


def next_tile(maze, current, move_dir, start, start_tile):
    from_dir = reverse_dir[move_dir]
    current_tile = maze[current]
    if current == start:
        current_tile = start_tile
    directions = moves[current_tile]
    for move in directions:
        if move != from_dir:
            new_tile, new_pos = tile_at(maze, current, move)
            return new_pos, move
    return ''


def find_start_tile(maze, start):
    directions = ''
    for move in ('N', 'E', 'W', 'S'):
        from_dir = reverse_dir[move]
        next_ch, next_pos = tile_at(maze, start, move)
        if from_dir in moves[next_ch]:
            directions += move
    if directions in ('NS', 'SN'):
        return '|'
    elif directions in ('EW', 'WE'):
        return '-'
    elif directions in ('NE', 'EN'):
        return 'L'
    elif directions in ('NW', 'WN'):
        return 'J'
    elif directions in ('SW', 'WS'):
        return '7'
    elif directions in ('SE', 'ES'):
        return 'F'


def tile_at(maze, pos, move):
    x, y = pos
    a, b = tile_adjust[move]
    new_pos = (x + a, y + b)
    if new_pos in maze:
        ch = maze[new_pos]
    else:
        ch = '.'
    return ch, new_pos


def calculate(data):
    maze = {}

    for y, line in enumerate(data):
        for x, ch in enumerate(line):
            maze[(x, y)] = ch
            if ch == 'S':
                start = (x, y)

    steps = 0
    loop = set()
    current = start
    move = 'S'
    start_tile = find_start_tile(maze, start)
    path = []

    while True:
        loop.add(current)
        path.append(current)
        current, move = next_tile(maze, current, move, start, start_tile)
        steps += 1
        if current == start:
            break

    printMap(maze, path)

    furthest = int(steps / 2)
    return furthest


def printMap(tubesMap, nodes):
    tubeChar = {'|': '║', '-': '═', 'L': '╚', 'J': '╝', '7': '╗', 'F': '╔', 'S': '╬'}
    minX = min([x for x, _ in tubesMap])
    minY = min([y for y, _ in tubesMap])
    maxX = max([x for x, _ in tubesMap])
    maxY = max([y for y, _ in tubesMap])

    for y in range(minY, maxY+1):
        for x in range(minX, maxX+1):
            if (x, y) in tubesMap:
                c = tubesMap[(x, y)]
                print(tubeChar[c] if c in tubeChar else c, end='')
            elif (x, y) in nodes:
                print('o', end='')
            else:
                print('.', end='')
        print()


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", action="store_true", help="Run with test data")
    parser.add_argument("-i", "--input", default="input.txt", help="Input file path")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    test_data = """
.....
.S-7.
.|.|.
.L-J.
.....
""".strip().split("\n")

    if not args.test:
        with open(args.input, 'r') as file:
            file_data = file.read()
        test_data = file_data.strip().split('\n')

    print(calculate(test_data))