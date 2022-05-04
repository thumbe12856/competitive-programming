import sys
from collections import defaultdict
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
sys.setrecursionlimit(10000)


def solve(N, nums):
    s = sum(nums)

    def dfs(idx, curr_s):
        if idx == N:
            return abs(s - curr_s - curr_s)

        return min(
            dfs(idx + 1, curr_s),
            dfs(idx + 1, curr_s + nums[idx])
        )

    return dfs(0, 0)


N = int(input())
nums = get_ints()
print(solve(N, nums))
