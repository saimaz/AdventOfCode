import sys


def calculate(filepath):
    with open(filepath, 'r') as file:
        lines = file.read().strip().split('\n')

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


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-s":
        file_path = "input.txt"
    else:
        file_path = "input_test.txt"

    result = calculate(file_path)
    print("Answer:", result)


