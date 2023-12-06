import sys


def calculate(file_path):
    with open(file_path, 'r') as file:
        values = file.readlines()

    time = int(values[0].split(":")[1].replace(" ", ""))
    distance = int(values[1].split(":")[1].replace(" ", ""))

    wins = 0
    for i in range(1, time):
        if i * (time - i) > distance:
            wins += 1

    return wins


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-s":
        file_path = "input.txt"
    else:
        file_path = "input_test.txt"

    result = calculate(file_path)
    print("Answer:", result)
