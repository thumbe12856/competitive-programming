from math import gcd
from bisect import *
from heapq import *
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, nums):
    q = set()
    for i in range(N):
        j = (i + 1) % N
        if nums[j] >= nums[i] and nums[j] % nums[i] == 0:
            continue
        q.add(i)

    ans = 0
    while q:
        next_q = set()
        next_nums = {}
        for i in q:
            j = (i + 1) % N
            k = (i - 1 + N) % N
            val = gcd(nums[i], nums[j])
            next_nums[i] = val

        for i in q:
            nums[i] = next_nums[i]

        for i in q:
            j = (i + 1) % N
            k = (i - 1 + N) % N
            if nums[j] < nums[i] or (nums[j] > nums[i] and nums[j] % nums[i] != 0):
                next_q.add(i)
            if nums[i] < nums[k] or (nums[i] > nums[k] and nums[i] % nums[k] != 0):
                next_q.add(k)

        q = next_q
        ans += 1

    return ans

T = int(input())
for _ in range(T):
    N = int(input())
    nums = get_ints()
    print(solve(N, nums))
