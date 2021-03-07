from bisect import bisect_left
import math
from collections import defaultdict
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

T = int(input())
for _ in range(T):
    N = int(input())
    nums = get_ints()
    nums = [0] + nums

    dp = [0] * (N + 1)
    for i in range(1, N + 1, 1):
        for j in range(2 * i, N + 1, i):
            if nums[j] > nums[i]:
                dp[j] = max(dp[j], dp[i] + 1)

    print(max(dp) + 1)
