from itertools import permutations
from math import floor
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))


def cal(N, nums):
    ans = N
    for i in range(K - 1, -1, -1):
        ans = floor(ans - ans * nums[i] / 100)
    return N - ans


def solve(N, K, nums):
    ans = -1
    for num in permutations(nums):
        ans = max(ans, cal(N, num))
    return ans

Q = int(input())
for _ in range(Q):
    nums = get_ints()
    N, K, nums = nums[0], nums[1], nums[2:]
    print(solve(N, K, nums))
