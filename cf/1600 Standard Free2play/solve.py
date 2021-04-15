import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(H, N, P):
    if N == 1:
        return 0

    ans = 0
    idx = 0
    next_h = P[1] + 1
    while idx < N - 2:
        h = P[idx + 1] + 1
        diff = h - P[idx + 2]
        if diff > 2:
            next_h = P[idx + 2] + 1
            idx += 1
            ans += 1
        else:
            next_h = P[idx + 2]
            idx += 2

    if next_h > P[-1] and P[-1] + 1 >= 3:
        ans += 1
    return ans

T = int(input())
for _ in range(T):
    H, N = map(int, input().split())
    P = get_ints()
    print(solve(H, N, P))
