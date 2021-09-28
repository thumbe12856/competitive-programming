from collections import *
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))


def solve(N, nums):
    ans = 0
    vis = defaultdict(int)
    for i in range(N):
        ans += i - vis[nums[i]]
        vis[nums[i]] += 1

    return ans

N = int(input())
nums = get_ints()
print(solve(N, nums))
