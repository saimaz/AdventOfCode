import sys
import re


def change_letters_to_numbers(line):
    number_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    i = 0
    while i < len(line):
        replaced = False
        for word, digit in number_map.items():
            if line[i:].startswith(word):
                line = line[:i] + digit + line[i + len(word):]
                i += len(digit) - 1
                replaced = True
                break
        if not replaced:
            i += 1

    return line


def calculate(file_path):
    total_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            line = change_letters_to_numbers(line.strip())
            digits = [char for char in line if char.isdigit()]
            if digits:
                first_digit, last_digit = digits[0], digits[-1]
                v = int(first_digit + last_digit)
                total_sum += v
                # print(line + " = " + str(v))
            # else:
                # print("########### NO NUMBERS - " + line)
    return total_sum


def test_lambda(file_path):
    result = sum([int(k[0] + k[-1]) for k in [''.join(filter(str.isdigit, final_list)) for final_list in [
        re.compile(r"(?=(one|two|three|four|five|six|seven|eight|nine))").sub(
            lambda x: {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
                       'eight': '8', 'nine': '9'}.get(x.group(1)), word_to_digit) for word_to_digit in
        [line.rstrip() for line in open(file_path)]]]])
    return result


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-s":
        file_path = "input_2.txt"
    else:
        file_path = "input_test_2.txt"

    result = calculate(file_path)
    print("Answer:", result)
