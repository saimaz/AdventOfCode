from typing import List
from collections import defaultdict


def solve(data: List[str]):
    parts = "\n".join(data).split("\n\n")
    rules = parts[0].splitlines()
    updates = parts[1].splitlines()
    priority = defaultdict(set)

    for rule in rules:
        x, y = map(int, rule.split('|'))
        priority[y].add(x)

    def validate(update):
        position = {page: idx for idx, page in enumerate(update)}
        for y, xs in priority.items():
            if y in position:
                for x in xs:
                    if x in position and position[x] > position[y]:
                        return False
        return True

    def middle(update):
        return update[len(update) // 2]

    total = 0
    for update in updates:
        pages = list(map(int, update.split(',')))
        if validate(pages):
            total += middle(pages)

    return total


def get_test_data():
    return """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

