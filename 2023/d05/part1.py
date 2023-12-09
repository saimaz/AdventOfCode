import argparse


def map_seed(mappings, seed):
    mapped_value = seed
    for map_group in mappings:
        for dest_start, src_start, range_len in map_group:
            if src_start <= mapped_value < src_start + range_len:
                mapped_value = dest_start + (mapped_value - src_start)
                break
    return mapped_value


def calculate(data):
    lines = data.strip().split('\n')

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


def parse_arguments():
    parser = argparse.ArgumentParser(description="Calculate the minimum location for Advent of Code.")
    parser.add_argument("-t", "--test", action="store_true", help="Run with test data")
    parser.add_argument("-i", "--input", default="input.txt", help="Input file path")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    test_data = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
    """

    if args.test:
        result = calculate(test_data)
    else:
        with open(args.input, 'r') as file:
            file_data = file.read()
        result = calculate(file_data)

    print("Answer:", result)
