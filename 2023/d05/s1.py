import sys


def map_seed(mappings, seed):
    mapped_value = seed
    for map_group in mappings:
        for dest_start, src_start, range_len in map_group:
            if src_start <= mapped_value < src_start + range_len:
                mapped_value = dest_start + (mapped_value - src_start)
                break
    return mapped_value


def calculate(filepath):
    with open(filepath, 'r') as file:
        lines = file.read().strip().split('\n')

    seeds = [int(x) for x in lines[0].split(': ')[1].split()]

    cat_maps = []
    curr_map = []
    for line in lines[3:]:
        if ':' in line:
            if curr_map:
                cat_maps.append(curr_map)
                curr_map = []
        elif line:
            curr_map.append(tuple(int(x) for x in line.split()))

    if curr_map:
        cat_maps.append(curr_map)

    locs = {map_seed(cat_maps, seed): seed for seed in seeds}
    min_loc = min(locs.keys())

    return min_loc


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-s":
        file_path = "input.txt"
    else:
        file_path = "input_test.txt"

    result = calculate(file_path)
    print("Answer:", result)
