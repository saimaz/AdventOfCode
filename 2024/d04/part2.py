from typing import List


def solve(data: List[str]) -> int:
    rows = len(data)
    cols = len(data[0])
    answer = 0

    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if data[i][j] == 'A':
                d1 = data[i-1][j-1] + 'A' + data[i+1][j+1]
                d2 = data[i-1][j+1] + 'A' + data[i+1][j-1]
                if (d1 == 'MAS' or d1 == 'SAM') and (d2 == 'MAS' or d2 == 'SAM'):
                    answer += 1

    return answer


def get_test_data():
    return """
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
"""