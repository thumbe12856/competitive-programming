import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10000)


def solve(N, W, nums):
    dp = [0] * (W + 1)
    nums.sort()
    for w, v in nums:
        next_dp = dp[:]
        for i in range(w, W + 1, 1):
            next_dp[i] = max(dp[i], dp[i - w] + v)

        dp = next_dp
    return dp[-1]

N, W = get_ints()
nums = []
for _ in range(N):
    w, v = get_ints()
    nums.append((w, v))

print(solve(N, W, nums))
