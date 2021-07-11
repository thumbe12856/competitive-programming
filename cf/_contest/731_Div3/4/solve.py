import math
from bisect import *
from heapq import *
import sys
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, nums):
    ans = ["0"]
    for i in range(1, N):
        if nums[i] & nums[i - 1] != nums[i - 1]:
            val = (nums[i] & nums[i - 1]) ^ nums[i - 1]
            nums[i] = nums[i] ^ val
            ans.append(str(val))
        else:
            ans.append("0")

    return (" ").join(ans)

T = int(input())
for _ in range(T):
    N = int(input())
    nums = get_ints()
    print(solve(N, nums))
