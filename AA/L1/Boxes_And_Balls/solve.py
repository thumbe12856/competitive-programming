import sys
from heapq import *


def get_ints():
    return list(map(int, sys.stdin.readline().strip().split()))


def solve(N, nums):
    ans = 0
    q = []
    for n in nums:
        heappush(q, n)

    if not (N & 1):
        heappush(q, 0)

    while len(q) > 1:
        print(q)
        s = heappop(q) + heappop(q) + heappop(q)
        ans += s
        heappush(q, s)

    return ans

N = int(input())
nums = get_ints()
print(solve(N, nums))
