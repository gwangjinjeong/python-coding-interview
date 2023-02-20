from itertools import accumulate
from collections import Counter
import sys

def sum_combination(n,r):
    data = 1
    for i in range(r):
        data = data * (n-i)/(r-i)
    return int(data)

si = sys.stdin.readline

N, M = list(map(int,si().split()))
A = list(map(int,si().split()))
# 누적합에 %3해서 0~i까지 그대로 떨어지는 경우의 수 구하기
S = list(accumulate(A))
S3 = list(map(lambda a: a % M, S))

# Counter를 통해서 요소별로 갯수를 구하기
count_S = Counter(S3)

# key가 0인것은 구간합(0~i)까지가 이미 나누어 떨어진다는것 이것을 초기값으로 두자
cnt = count_S[0]

# 그 밖에 구간합(i~j)가 나누어 떨어지는것을 확인하려면, 2개뽑아서 뺄 필요없이 조합 공식으로 구하면 된다.
# 순서에 의미가 있고, 중복이 허용되지 않기 때문에 조합이다.
for value in count_S.values():
    cnt = cnt + sum_combination(value,2)
print(cnt)
