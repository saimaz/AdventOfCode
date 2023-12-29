import argparse


def get_hand_total_strength(s):
    trans_map = {"T": "a", "J": "b", "Q": "c", "K": "d", "A": "e"}
    s_len = len(s)
    hand_cards_value = ""
    hand = {}
    for i in range(s_len):
        c = s[i]
        if c in trans_map:
            hand_cards_value += trans_map[c]
        else:
            hand_cards_value += c
        hand[c] = 1 if c not in hand else hand[c] + 1
    joker = 0
    if "J" in hand and len(hand) > 1:
        joker = hand["J"]
        del hand["J"]
    sorted_hand = sorted(hand.items(), key=lambda x: x[1], reverse=True)
    sorted_hand[0] = (sorted_hand[0][0], sorted_hand[0][1] + joker)
    hand_type_value = ""
    for el in sorted_hand:
        hand_type_value += str(el[1])
    return int(hand_type_value.ljust(11, "0")) + int(hand_cards_value, 16)


def calculate(data):
    lines = data.strip().split('\n')
    strength_bets = []
    for line in lines:
        hand_bet = line.split()
        strength_bets.append(
            (get_hand_total_strength(hand_bet[0]), hand_bet[1], hand_bet[0])
        )
    sorted_hands = sorted(strength_bets, key=lambda x: x[0])
    winnings = 0
    for i in range(len(sorted_hands)):
        winnings += int(sorted_hands[i][1]) * (i + 1)
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
