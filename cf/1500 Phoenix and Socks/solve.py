import sys
from collections import defaultdict

def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, L, R, colors):
    ans = 0
    socks = defaultdict(int)
    for i in range(L):
        socks[colors[i]] -= 1

    for i in range(L, N, 1):
        socks[colors[i]] += 1

    l, r = 0, 0
    cnt = abs(R - N // 2) # Change style and color count
    for c in socks:
        if cnt > 0:
            val = min(cnt, abs(socks[c]) // 2)
            if R > L and socks[c] > 1:
                cnt -= val
                socks[c] -= val * 2
            elif R < L and socks[c] < -1:
                cnt -= val
                socks[c] += val * 2

        if socks[c] < 0:
            l += abs(socks[c])
        else:
            r += abs(socks[c])

    # number of socks that need to change style and color +
    # number of socks that only need to change style +
    # number of socks that only need to change color
    ans = cnt * 2 + (abs(R - N // 2) - cnt) + min(l, r)
    return ans

T = int(input())
for _ in range(T):
    N, L, R = get_ints()
    colors = get_ints()
    print(solve(N, L, R, colors))
