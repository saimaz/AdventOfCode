from typing import List


def solve(data: List[str]):
    def is_safe(report):
        levels = list(map(int, report.split()))
        diff = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

        all_increasing = all(0 < d <= 3 for d in diff)
        all_decreasing = all(-3 <= d < 0 for d in diff)

        return all_increasing or all_decreasing

    def is_safe_to_remove(report):
        levels = list(map(int, report.split()))
        for i in range(len(levels)):
            modified_levels = levels[:i] + levels[i + 1:]
            if is_safe(' '.join(map(str, modified_levels))):
                return True
        return False

    safe_reports = 0
    for report in data:
        if is_safe(report) or is_safe_to_remove(report):
            safe_reports += 1

    return safe_reports


def get_test_data():
    return """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

