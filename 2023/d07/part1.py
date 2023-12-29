import argparse


def get_hand_strength(hand):
    trans_map = {"T": "a", "J": "b", "Q": "c", "K": "d", "A": "e"}
    hand_value = "".join(trans_map.get(card, card) for card in hand)
    card_count = {}
    for card in hand:
        card_count[card] = card_count.get(card, 0) + 1

    sorted_hand = sorted(card_count.items(), key=lambda x: x[1], reverse=True)
    hand_type_value = "".join(str(count) for _, count in sorted_hand)
    return int(hand_type_value.ljust(11, "0")) + int(hand_value, 16)


def calculate(data):
    strength_bets = [
        (get_hand_strength(line.split()[0]), line.split()[1])
        for line in data.strip().split('\n')
    ]

    sorted_hands = sorted(strength_bets, key=lambda x: x[0])
    winnings = sum(int(bet) * (index + 1) for index, (_, bet) in enumerate(sorted_hands))
    return winnings


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--test", action="store_true", help="Run with test data")
    parser.add_argument("-i", "--input", default="input.txt", help="Input file path")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    test_data = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

    if args.test:
        result = calculate(test_data)
    else:
        with open(args.input, 'r') as file:
            file_data = file.read()
        result = calculate(file_data)

    print("Answer:", result)
