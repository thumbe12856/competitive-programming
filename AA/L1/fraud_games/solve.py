from collections import defaultdict
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, A, G, P):
    cnt = 0
    p_cnt = defaultdict(int)
    alive = N
    for i in range(G):
        idx = P[i] - 1
        val = i + 1
        A[idx] = A[idx] - (alive - 1) * val + (cnt - p_cnt[idx])
        if A[idx] < 0:
            alive -= 1
        cnt += val
        p_cnt[idx] = cnt

    for i in range(N):
        if A[i] >= 0 and i != P[-1] - 1:
            A[i] += cnt - p_cnt[i]
    print(*A)

N = int(input())
A = get_ints()
G = int(input())
P = get_ints()
solve(N, A, G, P)
