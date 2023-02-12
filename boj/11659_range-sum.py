import sys


def preprocessing(inlist: list) -> list:
    sum_list = []
    tmp = 0
    sum_list.append(tmp)
    for num in inlist:
        tmp = tmp + num
        sum_list.append(tmp)
    return sum_list


si = sys.stdin.readline
N, M = list(map(int, si().split()))

lst = list(map(int, si().split()))
if len(lst) != 5:
    raise Exception('입력값 부족')

sumList = preprocessing(lst)
for _ in range(M):
    i, j = list(map(int, si().split()))
    print(sumList[j] - sumList[i - 1])
