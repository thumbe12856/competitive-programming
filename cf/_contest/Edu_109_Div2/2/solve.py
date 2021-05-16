import math
import sys

def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))

def solve(N, nums):
    target = [i + 1 for i in range(N)]
    if nums == target:
        return 0

    if nums[0] == N and nums[-1] == 1:
        return 3

    elif nums[0] == 1 or nums[-1] == N:
        return 1

    return 2

T = int(input())
for _ in range(T):
    N = int(input())
    nums = get_ints()
    print(solve(N, nums))
