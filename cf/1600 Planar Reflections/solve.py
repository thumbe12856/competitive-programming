MOD = 10 ** 9 + 7

def solve(N, K):
    last_dp = [1] * (N + 1)
    ans = 1
    turn = 0
    for _ in range(K - 1, 0, -1):
        dp = [0] * (N + 1)
        if turn == 0:
            for j in range(N - 1, -1, -1):
                dp[j] = last_dp[j] + dp[j + 1]
            ans += dp[0]
        else:
            for j in range(1, N + 1, 1):
                dp[j] = last_dp[j] + dp[j - 1]
            ans += dp[N]

        turn = 1 - turn
        last_dp = dp

    return ans % MOD

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    print(solve(N, K))
