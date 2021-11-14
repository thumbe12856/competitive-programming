import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10000)


MOD = 10 ** 9 + 7
def solve(N, C, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    C.sort()
    for i in range(C[0], target + 1, 1):
        for c in C:
            if i < c:
                break
            dp[i] += dp[i - c] % MOD

    return dp[-1] % MOD

N, target = get_ints()
C = get_ints()
print(solve(N, C, target))
