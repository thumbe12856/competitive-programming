from collections import defaultdict
from bisect import *
from heapq import *
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, K, pos, temps):
    ans = [-1] * N
    q = []
    for i in range(K):
        heappush(q, (temps[i], pos[i] - 1))

    can = defaultdict(lambda: float('inf'))
    while q:
        t, idx = heappop(q)
        if ans[idx] != -1:
            continue

        ans[idx] = t
        for next_idx in [idx + 1, idx - 1]:
            if 0 <= next_idx < N and can[next_idx] > t + 1:
                can[next_idx] = t + 1
                heappush(q, (t + 1, next_idx))

    return (" ").join(map(str, ans))

T = int(input())
for _ in range(T):
    input()
    N, K = get_ints()
    pos = get_ints()
    temps = get_ints()
    print(solve(N, K, pos, temps))
