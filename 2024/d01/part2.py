from collections import Counter


def solve(data):
    left_list = []
    right_list = []

    for line in data:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

    right_counts = Counter(right_list)

    similarity_score = 0
    for number in left_list:
        similarity_score += number * right_counts[number]

    return similarity_score


def get_test_data():
    return """
3 4
4 3
2 5
1 3
3 9
3 3
""".strip().split("\n")
