from itertools import combinations
from itertools import accumulate
import sys

si = sys.stdin.readline

N, M = list(map(int,si().split()))
A = list(map(int,si().split()))
S = [0] + list(accumulate(A))
S_combination = list(combinations(S, 2))
result = list(map(lambda x : 1 if (x[1] - x[0]) % M == 0 else 0, S_combination))
print(sum(result))
