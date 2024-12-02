def solve(data):
    left_list = []
    right_list = []

    for line in data:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

    left_list.sort()
    right_list.sort()

    total_distance = 0
    for i in range(len(left_list)):
        total_distance += abs(left_list[i] - right_list[i])

    return total_distance


def get_test_data():
    return """
3 4
4 3
2 5
1 3
3 9
3 3
"""
