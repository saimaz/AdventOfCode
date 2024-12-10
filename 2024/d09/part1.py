from typing import List


def solve(data: List[str]) -> int:
    disk_map = data[0]
    n = []

    for i, v in enumerate(disk_map):
        n.extend([' ' if i % 2 == 1 else i // 2] * int(v))

    idx, ide = 0, len(n) - 1

    while idx < ide:
        while idx < len(n) and n[idx] != ' ':
            idx += 1
        while ide >= 0 and n[ide] == ' ':
            ide -= 1
        if idx < ide:
            n[idx], n[ide] = n[ide], ' '

    checksum = 0
    for i, v in enumerate(n):
        if v != ' ':
            checksum += i * v

    return checksum


def get_test_data():
    return "2333133121414131402"
