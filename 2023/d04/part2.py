import argparse


def calculate(data):
    lines = data.strip().split('\n')

    card_counts = {}
    for i, line in enumerate(lines):
        parts = line.split('|')
        if len(parts) < 2:
            continue
        winning_numbers = parts[0].split()
        my_numbers = parts[1].split()

        winning_numbers = set(map(int, filter(str.isdigit, winning_numbers)))
        my_numbers = set(map(int, filter(str.isdigit, my_numbers)))

        matches = len(winning_numbers.intersection(my_numbers))
        card_counts[i] = {'count': 1, 'matches': matches}

    for card, info in card_counts.items():
        matches = info['matches']
        for card2 in range(card + 1, card + 1 + matches):
            if card2 in card_counts:
                card_counts[card2]['count'] += card_counts[card]['count']

    total_cards = sum(info['count'] for info in card_counts.values())

    return total_cards


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", action="store_true", help="Run with test data")
    parser.add_argument("-i", "--input", default="input.txt", help="Input file path")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    test_data = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

    if args.test:
        result = calculate(test_data)
    else:
        with open(args.input, 'r') as file:
            file_data = file.read()
        result = calculate(file_data)

    print("Answer:", result)
