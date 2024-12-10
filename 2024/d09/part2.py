from typing import List


def solve(data: List[str]) -> int:
    idx = 0
    mmap = {}
    keys = []
    emptys = []

    for i, v in enumerate(data[0]):
        if i % 2 == 0:
            keys.append(i)
            mmap[i] = int(v) * [i // 2]
        else:
            emptys.append(i)
            mmap[i] = int(v) * [' ']
        idx += 1

    for k in keys[::-1]:
        file_blocks = mmap[k]
        file_length = len(file_blocks)

        tr = []
        for i in emptys:
            if i > k:
                break
            free_space_count = mmap[i].count(' ')
            if free_space_count == 0:
                tr.append(i)
            if file_length <= free_space_count:
                idx = mmap[i].index(' ')
                mmap[i] = mmap[i][:idx] + file_blocks + (free_space_count - file_length) * [' ']
                mmap[k] = file_length * [' ']
                break

        for i in tr:
            emptys.remove(i)

    result_list = []
    for i in mmap:
        result_list += mmap[i]

    checksum = 0
    for i, v in enumerate(result_list):
        if v != ' ':
            checksum += i * v

    return checksum


def get_test_data():
    return "2333133121414131402"