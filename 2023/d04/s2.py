import sys


def calculate(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

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


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-s":
        file_path = "input.txt"
    else:
        file_path = "input_test.txt"

    result = calculate(file_path)
    print("Answer:", result)
