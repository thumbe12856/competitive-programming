from bisect import *
from heapq import *
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, l, r, nums):
    ans = 0
    nums.sort()
    # print(nums)
    q = []
    for n in nums:
        l_idx = bisect_left(q, l - n)
        r_idx = bisect_right(q, r - n)

        # print(q, l_idx, r_idx)
        if q:
            ans += r_idx - l_idx
        q.append(n)

    return ans

T = int(input())
for _ in range(T):
    N, l, r = get_ints()
    nums = get_ints()
    print(solve(N, l, r, nums))
