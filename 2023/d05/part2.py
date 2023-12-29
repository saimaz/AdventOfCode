import argparse


def calculate(data):
    lines = data.strip().split('\n')

    seed_info = [int(x) for x in lines[0].split(': ')[1].split()]
    seeds = [(seed_info[i], seed_info[i] + seed_info[i+1] - 1) for i in range(0, len(seed_info), 2)]

    cat_maps = []
    for line in lines[2:]:
        line = line.strip()
        if line.endswith(':'):
            cat_maps.append([])
        elif line:
            cat_maps[-1].append([int(x) for x in line.split()])

    res = 2**64
    for s, o in seeds:
        ranges = [(s, o)]
        for typemappings in cat_maps:
            newranges = []
            for l, h in ranges:
                found = False
                for md, ms, mo in typemappings:
                    if l >= ms and h < ms + mo:
                        newranges.append((l - ms + md, h - ms + md))
                        found = True
                    elif l < ms and h >= ms and h < ms + mo:
                        ranges.append((l, ms - 1))
                        newranges.append((md, md + h - ms))
                        found = True
                    elif l < ms + mo and h >= ms + mo and l >= ms:
                        ranges.append((ms + mo, h))
                        newranges.append((md + l - ms, md + mo - 1))
                        found = True
                    elif l < ms and h >= ms + mo:
                        ranges.append((l, ms - 1))
                        newranges.append((md, md + mo - 1))
                        ranges.append((ms + mo, h))
                        found = True
                    if found:
                        break
                if not found:
                    newranges.append((l, h))
            ranges = newranges.copy()
        res = min(res, min(ranges)[0])

    return res


def parse_arguments():
    parser = argparse.ArgumentParser(description="Calculate the sum for Advent of Code.")
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
