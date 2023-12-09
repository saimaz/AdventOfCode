import sys


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


def calculate(file_path):
    with open(file_path) as f:
        lines = f.readlines()
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


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-s":
        file_path = "input.txt"
    else:
        file_path = "input_test.txt"

    result = calculate(file_path)
    print("Answer:", result)
