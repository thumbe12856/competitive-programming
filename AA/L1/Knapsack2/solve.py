import sys


def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10000)


def solve(N, W, nums):
    dp = [[float('inf')] * (10 ** 5 + 1) for _ in range(N + 1)]
    for i in range(N + 1):
      dp[i][0] = 0

    for i in range(N):
        for j in range(10 ** 5 + 1):
            dp[i + 1][j] = min(dp[i][j], dp[i + 1][j])
            w, v = nums[i]

            if j >= v:
                dp[i + 1][j] = min(
                    dp[i + 1][j],
                    dp[i][j - v] + w
                )

    for i in range(10 ** 5, -1, -1):
        if dp[N][i] <= W:
            return i

N, W = get_ints()
nums = []
for _ in range(N):
    w, v = get_ints()
    nums.append((w, v))

print(solve(N, W, nums))
