import sys
from collections import defaultdict

MOD = 10 ** 9 + 7
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def npr(n, r):
    res = 1
    for i in range(n, (n - r), -1):
        res = (res * i) % MOD
    return res

def solve(N, A):
    ans = 0
    ca = defaultdict(int)
    min_val = float('inf')
    for a in A:
        ca[a] += 1
        min_val = min(min_val, a)

    if ca[min_val] < 2:
        return 0

    if min_val != 0:
        target = format(min_val, '030b')
        for n in ca:
            if n == min_val:
                continue

            curr = format(n, '030b')
            for i in range(30):
                if target[i] == "1" and curr[i] == "0":
                    return 0

    ans = npr(ca[min_val], 2)
    for i in range(2, N - 2 + 1, 1):
        ans = (ans * i) % MOD

    return ans

T = int(input())
for _ in range(T):
    N = int(input())
    A = get_ints()
    print(solve(N, A))
