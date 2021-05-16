import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
from functools import lru_cache

def solve(N, M, K):
    if N > M:
        M, N = N, M
    lower = (N + 1) * (N - 2) + 1 + N + (M - N) * N
    upper = M * N - 1
    # print(lower, upper)
    if lower <= K <= upper:
        return "Yes"

    return "No"

T = int(input())
for _ in range(T):
    N, M, K = get_ints()
    print(solve(N, M, K))
