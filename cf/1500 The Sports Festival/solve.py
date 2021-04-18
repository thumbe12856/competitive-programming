import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, nums):
    nums.sort()
    print(nums)
    dp = [[0 for i in range(N)] for j in range(N + 1)]
    for i in range(N - 1, -1, -1):
        for j in range(i + 1, N, 1):
            dp[i][j] = nums[j] - nums[i] + min(dp[i + 1][j], dp[i][j - 1])
    return dp[0][N - 1]

N = int(input())
nums = get_ints()
print(solve(N, nums))
