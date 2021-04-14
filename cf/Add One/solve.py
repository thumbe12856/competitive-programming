import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())

MOD = 10 ** 9 + 7
LIMIT = 200011
dp = [0] * LIMIT
for i in range(10):
    dp[i] = 1
for i in range(10, LIMIT, 1):
    dp[i] = (dp[i - 9] + dp[i - 10]) % MOD

def solve(N, M):
    ans = 0
    while N:
        ans = (ans + dp[N % 10 + M]) % MOD
        N //= 10
    return ans % MOD

T = int(input())
for _ in range(T):
    N, M = get_ints()
    print(solve(N, M))
