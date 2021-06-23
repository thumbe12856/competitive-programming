from bisect import *
from heapq import *
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, nums):
    s = sum(nums)
    if s % N != 0:
        return -1

    ans = 0
    target = s // N
    for n in nums:
        if n > target:
            ans += 1
    return ans

T = int(input())
for _ in range(T):
    N = int(input())
    nums = get_ints()
    print(solve(N, nums))
