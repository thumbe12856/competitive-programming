import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10000)
MOD = 998244353

def solve(N, A, B):

    dp = [0] * N
    for i in range(N - 1, -1, -1):
        dp[i] = B[i] - A[i] + 1

    print(dp)
    ans = 1
    for i in range(N - 1, -1, -1):
        ans = dp[i] * ans
        print(ans)

    return ans % MOD


N = int(input())
A = get_ints()
B = get_ints()
print(solve(N, A, B))
