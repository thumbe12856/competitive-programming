import sys

def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(n, B, x, y):
    N = B // x
    if N >= n:
        return (0 + n * x) * (n + 1) // 2

    ans = (0 + N * x) * (N + 1) // 2
    n -= N + 1

    return ans

T = int(input())
for _ in range(T):
    n, B, x, y = get_ints()
    print(solve(n, B, x, y))

