import sys


def preprocessing(len_table, input_table: list) -> list:
    len_table = len(input_table)
    sum_table = [[0] * len_table for _ in range(len_table)]
    for x in range(1, len_table):
        for y in range(1, len_table):
            sum_table[x][y] = input_table[x][y] + sum_table[x - 1][y] + sum_table[x][y - 1] - sum_table[x - 1][y - 1]
    return sum_table


si = sys.stdin.readline
N, M = list(map(int, si().split()))

D = [[0 for _ in range(N + 1)]]
for _ in range(N):
    D.append([0] + list(map(int, si().split())))

S = preprocessing(N, D)
for _ in range(M):
    x1, y1, x2, y2 = list(map(int, si().split()))
    print(S[x2][y2] - S[x1 - 1][y2] - S[x2][y1 - 1] + S[x1-1][y1-1])
