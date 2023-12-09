import sys


def get_hand_strength(hand):
    trans_map = {"T": "a", "J": "b", "Q": "c", "K": "d", "A": "e"}
    hand_value = "".join(trans_map.get(card, card) for card in hand)
    card_count = {}
    for card in hand:
        card_count[card] = card_count.get(card, 0) + 1

    sorted_hand = sorted(card_count.items(), key=lambda x: x[1], reverse=True)
    hand_type_value = "".join(str(count) for _, count in sorted_hand)
    return int(hand_type_value.ljust(11, "0")) + int(hand_value, 16)


def calculate(file_path):
    with open(file_path) as file:
        strength_bets = [
            (get_hand_strength(line.split()[0]), line.split()[1])
            for line in file
        ]

    sorted_hands = sorted(strength_bets, key=lambda x: x[0])
    winnings = sum(int(bet) * (index + 1) for index, (_, bet) in enumerate(sorted_hands))
    return winnings


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-s":
        file_path = "input.txt"
    else:
        file_path = "input_test.txt"

    result = calculate(file_path)
    print("Answer:", result)
