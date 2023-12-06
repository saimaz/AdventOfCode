import sys


def calculate(file_path):
    with open(file_path, 'r') as file:
        values = file.readlines()

    times = [int(x) for x in values[0].split(":")[1].split(" ") if x.strip()]
    distances = [int(x) for x in values[1].split(":")[1].split(" ") if x.strip()]

    total_ways = 1
    for time, distance in zip(times, distances):
        wins = 0
        for i in range(time):
            if i * (time - i) > distance:
                wins += 1
        total_ways *= wins

    return total_ways


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-s":
        file_path = "input.txt"
    else:
        file_path = "input_test.txt"

    result = calculate(file_path)
    print("Answer:", result)
