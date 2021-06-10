from bisect import *
from heapq import *
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

T = int(input())
for _ in range(T):
    N = int(input())
    nums = get_ints()
    max_target = max(nums)
    min_target = min(nums)

    min_can, max_can = set(), set()
    for i in range(N):
        if nums[i] == max_target:
            max_can.add((i + 1, N - i))

        if nums[i] == min_target:
            min_can.add((i + 1, N - i))

    # print(max_can)
    # print(min_can)
    ans = -1
    if max_target == min_target:
        for l, r in max_can:
            ans = max(ans, l, r)
    else:
        for max_l, max_r in max_can:
            for min_l, min_r in min_can:
                ans = max(
                    ans,
                    min(
                        max(max_l, min_l),
                        max(max_r, min_r),
                        min_l + max_r,
                        max_l + min_r,
                    )
                )

    print(ans)